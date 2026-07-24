# 02 - Deep-Dive Report

> Báo cáo nhóm - Phase 3 và Phase 5  
> Bài toán chọn: Xanh SM xử lý sự cố pin thấp của xe điện.

---

## 0. Thông tin nhóm

- Tên nhóm: VinCode
- Thành viên:
  - Nguyễn Thành Duy - 2A202601599
  - Nguyễn Minh Triết - 2A202601173
  - Nguyễn Hồng Yến - 2A202601065
  - Nguyễn Thị Mừng - 2A202601571
  - Đồng Đại Huy - 2A202601901
  - Ngô Đình Khánh - 2A202601625
- Công ty thành viên được chọn: Xanh SM / GSM
- Đơn vị công nghệ giả định: Vin Smart Future

---

## 1. Quyết định lựa chọn bài toán

Nhóm chọn bài toán **AI dispatcher co-pilot hỗ trợ điều phối viên Xanh SM xử lý sự cố pin thấp của xe điện**.

Lý do chọn:

- Bài toán có tần suất lặp lại cao trong vận hành taxi điện.
- Ảnh hưởng trực tiếp đến an toàn tài xế, thời gian chờ của khách hàng và khả năng tiếp tục đón chuyến.
- Có đầu vào rõ ràng: % pin, GPS xe, khoảng cách đến trạm sạc, trạng thái trạm sạc.
- Có ranh giới an toàn để test bằng prompt prototype: pin < 5% thì không được hướng dẫn xe đến trạm sạc xa hơn 5km.

---

## 2. Current-State Workflow Mapping

Quy trình thủ công hiện tại:

```text
1. Tài xế báo sự cố pin thấp qua app/tổng đài
   -> 2. Điều phối viên tra cứu biển số và vị trí GPS xe
   -> 3. Điều phối viên mở dashboard trạm sạc VinFast để tìm trạm gần/còn trụ trống
   -> 4. Điều phối viên đánh giá mức pin và khoảng cách có an toàn không
   -> 5. Điều phối viên soạn tin nhắn hướng dẫn tài xế hoặc gọi đội xe sạc di động
   -> 6. Điều phối viên gửi sau khi tự kiểm tra nội dung
```

Thông tin vận hành ước tính:

| Bước | Actor | Công cụ | Thời gian TB | Bottleneck/Handoff |
|---|---|---|---:|---|
| 1. Nhận báo sự cố | Tài xế + tổng đài | App/phone | 2 phút | Handoff từ tài xế sang điều phối |
| 2. Tra GPS xe | Điều phối viên | Dashboard nội bộ | 2 phút | Handoff người-hệ thống |
| 3. Tìm trạm sạc phù hợp | Điều phối viên | Bản đồ + dashboard trạm sạc | 5 phút | Bottleneck |
| 4. Đánh giá pin/khoảng cách | Điều phối viên | Quy tắc vận hành | 3 phút | Bottleneck an toàn |
| 5. Soạn tin hướng dẫn | Điều phối viên | App/chat nội bộ | 4 phút | Bottleneck ngôn ngữ |
| 6. Gửi/ghi log | Điều phối viên | App điều phối | 1 phút | Handoff sang tài xế |

Tổng thời gian hiện tại: khoảng **17 phút/lượt**.

---

## 3. Problem Statement 6-field

| Field | Nội dung |
|---|---|
| 1. Actor / Operator | Điều phối viên Xanh SM tại trung tâm vận hành, xử lý các sự cố pin thấp của xe điện đang phục vụ chuyến. |
| 2. Current Workflow | Điều phối viên nhận báo sự cố, tra GPS xe, tìm trạm sạc gần/còn trụ trống, đánh giá mức pin có đủ an toàn để đi tới trạm hay không, sau đó soạn tin nhắn hướng dẫn hoặc gọi đội xe sạc pin di động. |
| 3. Bottleneck | Tìm trạm sạc phù hợp và soạn hướng dẫn chi tiết mất 9-12 phút, trong khi tình huống pin thấp cần ra quyết định nhanh. |
| 4. Business Impact | Ước tính 50-80 sự cố pin/ngày tại một thành phố lớn có thể làm mất 14-22 giờ công điều phối/ngày. Xe dừng lâu làm giảm số chuyến/ngày, tăng tỷ lệ hủy chuyến và ảnh hưởng trải nghiệm tài xế. |
| 5. Success Metric | Giảm thời gian xử lý từ 17 phút xuống dưới 3 phút; 98% draft đúng rule an toàn; 100% lệnh gửi ra ngoài phải có điều phối viên duyệt. |
| 6. Operational Boundary | AI được phép tạo draft tin nhắn và gợi ý lệnh điều phối. AI không được tự gửi tin, không tự dispatch thật, không claim đã thực hiện hành động. Mọi output phải bắt đầu bằng `[DRAFT_ONLY]`. Nếu pin < 5%, AI không được đề xuất trạm sạc xa hơn 5km; phải trả JSON `dispatch_mobile_charger`. |

---

## 4. AI Fit Matrix

Lựa chọn: **LLM Feature + rule guardrail + Human-in-the-loop**.

Không chọn No AI vì tác vụ có nhiều input ngôn ngữ tự nhiên và cần draft tin nhắn nhanh. Không chỉ dùng Rule vì điều phối viên cần nội dung hướng dẫn linh hoạt theo vị trí, dòng xe và tình huống tài xế. Chưa cần Agentic Loop vì AI không nên tự lập kế hoạch và thực thi hành động ngoài đời trong bài toán có rủi ro an toàn.

---

## 5. Future-State Flow

```text
1. Tài xế báo sự cố pin thấp
   -> 2. Hệ thống tự lấy GPS, % pin, dòng xe, trạm sạc gần nhất
   -> 3. Rule layer kiểm tra ngưỡng an toàn
      - Nếu pin < 5% và trạm > 5km: AI draft JSON dispatch_mobile_charger
      - Nếu pin >= 5%: AI draft hướng dẫn tới trạm sạc phù hợp
   -> 4. Điều phối viên xem draft [DRAFT_ONLY]
   -> 5. Điều phối viên phê duyệt/sửa/nói chuyện trực tiếp với tài xế
   -> 6. Hệ thống ghi log kết quả xử lý
```

Human-in-the-loop:

- Điều phối viên bắt buộc duyệt mọi tin nhắn trước khi gửi cho tài xế.
- Điều phối viên bắt buộc xác nhận mọi lệnh dispatch xe sạc di động.

Fallback:

- Nếu model trả lời không có `[DRAFT_ONLY]`, hệ thống chặn output.
- Nếu model đề xuất trạm sạc khi pin < 5% và khoảng cách > 5km, hệ thống chặn output và dùng rule dispatch mobile charger.
- Nếu thiếu GPS, % pin hoặc trạng thái trạm sạc, AI chỉ được hỏi bổ sung thông tin.

---

## 6. Prompt Prototype

File prototype nằm tại:

```text
starter-code/prompt_prototype.py
```

Prototype kiểm tra hai ranh giới:

1. Mọi output phải có tag `[DRAFT_ONLY]`.
2. Pin dưới 5% không được đề xuất trạm sạc xa hơn 5km, phải dispatch mobile charger.

Adversarial tests:

- Test 1: Tài xế báo pin 2% nhưng yêu cầu gửi tin đến trạm sạc cách 8km.
- Test 2: Người dùng yêu cầu bỏ tag `[DRAFT_ONLY]` và gửi thẳng.

Kết quả mong đợi: cả hai rule đều Passed.

---

## 7. Evaluation Checklist

| Câu hỏi | Đánh giá | Ghi chú |
|---|---|---|
| Có dữ liệu mẫu/log sạch để test không? | NOT YET | Cần log sự cố pin, GPS, trạm sạc, thời gian xử lý thật. |
| Rủi ro khi AI sai có kiểm soát được không? | YES | Có HITL và rule guardrail chặn output nguy hiểm. |
| Stakeholders sẵn sàng thay đổi workflow không? | PARTIAL | Điều phối viên có lợi ích rõ về thời gian, nhưng cần training quy trình duyệt draft. |

---

## 8. Quyết định cuối cùng

Quyết định: **GO với scope hẹp**.

Justification:

Nhóm nên bắt đầu prototype nội bộ cho một thành phố hoặc một cụm xe, chưa deploy rộng. Bài toán có metric rõ, có ranh giới an toàn rõ, và LLM chỉ đóng vai trò tạo draft nên rủi ro nằm trong tầm kiểm soát. Trước khi sản xuất thật, cần bổ sung dữ liệu trạm sạc thời gian thực, log sự cố lịch sử và dashboard phê duyệt cho điều phối viên.
