# 01 - Problem Scan & Quick Cards

> Bài cá nhân - Phase 1 và Phase 2  
> Chủ đề ưu tiên: Vin Smart Future hỗ trợ vận hành Xanh SM và các công ty thành viên Vingroup.

---

## Phase 1 - SCAN: Danh sách 5 bài toán vận hành

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Time-consuming | Điều phối viên mất nhiều thời gian xử lý tài xế xe điện báo pin thấp giữa đường: tra GPS, tìm trạm sạc, soạn tin hướng dẫn, quyết định có cần xe sạc di động hay không. |
| 2 | Xanh SM | Stakeholder Pain | Tài xế phàn nàn hệ thống gợi ý điểm đón/trả khách chưa khớp với vị trí thực tế, đặc biệt tại khu đô thị, sân bay, trung tâm thương mại. |
| 3 | VinFast | Repetitive | Đối chiếu hóa đơn sạc điện và log sạc từ các trạm/đối tác mỗi tuần, nhiều dòng dữ liệu lặp lại, dễ sai khi copy thủ công. |
| 4 | Vinhomes | AI-upgrade | Phân loại phản ánh cư dân trên app Vinhomes Resident còn chậm và phản hồi rập khuôn, dẫn đến ticket bị chuyển sai bộ phận. |
| 5 | Vinmec | Time-consuming | Bác sĩ mất 20-30 phút để viết tóm tắt hồ sơ xuất viện từ bệnh án, xét nghiệm và ghi chú lâm sàng. |
| 6 | Vinpearl | Stakeholder Pain | Quản lý khách sạn phải đọc thủ công review trên Booking/Agoda/Google Maps để phát hiện phàn nàn khẩn cấp về phòng, dịch vụ, nhân viên. |

Top 3 bài toán được chọn để quick-assess:

1. Xanh SM - Xử lý sự cố pin thấp/hụt pin của xe điện.
2. Vinhomes - Phân loại và route phản ánh cư dân.
3. Vinmec - Soạn thảo tóm tắt hồ sơ xuất viện.

---

## Phase 2 - QUICK-ASSESS

## Quick Problem Card #1 - Xanh SM xử lý sự cố pin thấp của xe điện

| Trường | Nội dung |
|---|---|
| Bài toán | Điều phối viên cần xử lý nhanh trường hợp tài xế Xanh SM báo pin thấp, tìm trạm sạc gần hoặc điều xe sạc pin di động nếu pin nguy cấp. |
| Công ty thành viên | Xanh SM / GSM |
| Actor đang đau | Tài xế xe điện, điều phối viên trung tâm vận hành, khách hàng đang chờ chuyến xe. |
| Workflow thủ công hiện tại | 1. Tài xế gọi tổng đài báo pin thấp. -> 2. Điều phối viên tra GPS xe. -> 3. Mở dashboard trạm sạc VinFast để tìm trạm gần/còn trụ sạc trống. -> 4. Soạn tin nhắn hướng dẫn tài xế. -> 5. Nếu pin quá thấp, gọi đội xe sạc di động/cứu hộ. |
| Bước tốn thời gian/lỗi nhất | Bước 3-4, mất khoảng 10-12 phút/lượt; dễ sai khi chọn trạm xa hoặc không phù hợp cổng sạc. |
| AI có thể hỗ trợ | LLM Feature nhận input pin, GPS, khoảng cách trạm; draft tin nhắn `[DRAFT_ONLY]` và nếu pin < 5% thì trả JSON `dispatch_mobile_charger`. |
| Success metric | Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút; 98% đề xuất đúng rule an toàn pin < 5%. |
| Quick Architecture | LLM Feature + rule guardrail + Human-in-the-loop. |

Đánh giá nhanh:

- Giá trị cao vì ảnh hưởng trực tiếp đến an toàn giao thông, trải nghiệm tài xế và SLA đón khách.
- Ranh giới vận hành rõ: AI chỉ draft, không gửi thẳng; pin < 5% không đề xuất trạm xa hơn 5km.
- Nên chọn làm prototype vì có thể test bằng adversarial prompt rõ ràng.

---

## Quick Problem Card #2 - Vinhomes phân loại và route phản ánh cư dân

| Trường | Nội dung |
|---|---|
| Bài toán | Phản ánh của cư dân về nước, điện, thang máy, vệ sinh, an ninh bị phân loại chậm hoặc chuyển sai bộ phận. |
| Công ty thành viên | Vinhomes |
| Actor đang đau | Nhân viên CSKH, ban quản lý tòa nhà, cư dân gửi phản ánh. |
| Workflow thủ công hiện tại | 1. Cư dân gửi ticket trên app. -> 2. CSKH đọc nội dung. -> 3. Gắn nhãn loại vấn đề. -> 4. Chuyển ticket cho bộ phận phụ trách. -> 5. Theo dõi SLA và phản hồi cư dân. |
| Bước tốn thời gian/lỗi nhất | Bước 2-4, mất 6-10 phút/ticket; lỗi thường gặp là chuyển sai bộ phận hoặc đánh giá sai mức độ khẩn cấp. |
| AI có thể hỗ trợ | LLM phân loại nội dung, trích địa điểm/tòa nhà/căn hộ, đề xuất mức ưu tiên và draft phản hồi ban đầu. |
| Success metric | 85% ticket được phân loại dưới 10 giây; giảm tỷ lệ route sai từ 12% xuống dưới 4%. |
| Quick Architecture | Rule + LLM Feature; các ticket khẩn cấp vẫn cần nhân viên duyệt. |

Đánh giá nhanh:

- Phù hợp AI vì input là ngôn ngữ tự nhiên và có nhiều biến thể.
- Cần cẩn trọng với phản ánh liên quan tranh chấp phí, an ninh, pháp lý; các case này phải escalation cho con người.

---

## Quick Problem Card #3 - Vinmec soạn thảo tóm tắt hồ sơ xuất viện

| Trường | Nội dung |
|---|---|
| Bài toán | Bác sĩ mất nhiều thời gian tổng hợp bệnh án, kết quả xét nghiệm, chỉ định và lời dặn để viết tóm tắt xuất viện cho bệnh nhân. |
| Công ty thành viên | Vinmec |
| Actor đang đau | Bác sĩ điều trị, điều dưỡng hành chính, bệnh nhân/caregiver. |
| Workflow thủ công hiện tại | 1. Bác sĩ mở bệnh án điện tử. -> 2. Đọc ghi chú diễn biến điều trị. -> 3. Copy kết quả xét nghiệm/chẩn đoán. -> 4. Viết tóm tắt và lời dặn. -> 5. Kiểm tra, ký và in/trả cho bệnh nhân. |
| Bước tốn thời gian/lỗi nhất | Bước 2-4, mất 20-30 phút/bệnh nhân; dễ thiếu thông tin quan trọng nếu bác sĩ quá tải. |
| AI có thể hỗ trợ | LLM tạo bản nháp tóm tắt có cấu trúc từ dữ liệu EMR đã được phép truy cập, bác sĩ phải duyệt và sửa trước khi ban hành. |
| Success metric | Giảm thời gian tạo draft từ 25 phút xuống dưới 7 phút; 100% bản cuối phải được bác sĩ ký duyệt. |
| Quick Architecture | LLM Feature có HITL bắt buộc; không cho AI tự đưa chẩn đoán mới. |

Đánh giá nhanh:

- Giá trị cao nhưng rủi ro y tế lớn, cần dữ liệu sạch và quy trình phê duyệt chặt.
- Phù hợp giai đoạn sau hơn, khi đã có baseline và mẫu hồ sơ chuẩn.

---

## Kết luận cá nhân

Bài toán nên chọn cho prototype là **Xanh SM xử lý sự cố pin thấp của xe điện**. Lý do: quy trình có đầu vào rõ ràng, metric đo được, ranh giới an toàn cụ thể, và có thể stress-test bằng prompt injection. Giải pháp phù hợp nhất là **LLM Feature + rule guardrail + Human-in-the-loop**, không cần agent tự trị trong giai đoạn đầu.