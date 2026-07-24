# Bài cá nhân — Problem Scan & Quick Assessment

> **Họ và tên:** Đồng Đại Huy
> **MSSV:** 2A202601901
> **Lưu ý về dữ liệu:** Các thời gian và mục tiêu dưới đây là giả định phục vụ scoping, chưa phải số liệu vận hành chính thức của Vingroup. Baseline cần được xác nhận bằng log hệ thống và pilot thực tế.

# Phase 1 — SCAN: Quét cơ hội

Tôi sử dụng bốn lenses (Lặp lại, Tốn thời gian, AI-upgrade và Stakeholder Pain) để tìm các nút thắt có phạm vi vận hành rõ ràng.

| # | Công ty thành viên | Lens chính | Mô tả ngắn bài toán |
|---:|---|---|---|
| 1 | Xanh SM (GSM) | Tốn thời gian | Khi xe gặp sự cố pin ngoài đường, điều phối viên phải hỏi lại vị trí/mức pin, tra cứu trạm sạc và soạn hướng dẫn thủ công; thời gian giả định 12–15 phút/lượt. |
| 2 | Vinhomes | AI-upgrade | Phản ánh của cư dân được đọc, gắn nhãn và chuyển bộ phận thủ công; nội dung dài hoặc thiếu thông tin dễ bị phân loại sai và phải chuyển lại. |
| 3 | VinFast | Lặp lại | Nhân viên đối soát hóa đơn sạc với log phiên sạc và biểu phí bằng cách kiểm tra nhiều nguồn; các trường hợp lệch dữ liệu phải dò lại thủ công. |
| 4 | Vinmec | Tốn thời gian | Bác sĩ phải tổng hợp nhiều ghi chú để soạn bản nháp tóm tắt xuất viện, làm giảm thời gian dành cho chuyên môn và người bệnh. |
| 5 | Vinpearl | Stakeholder Pain | Nhân viên CSKH mất thời gian đọc yêu cầu thay đổi/hủy đặt phòng từ nhiều kênh và tra chính sách tương ứng; khách phải chờ khi yêu cầu có nhiều điều kiện. |
| 6 | Xanh SM (GSM) | Lặp lại | Lý do hủy chuyến nằm trong mã hủy, ghi chú tài xế và nội dung tổng đài; nhóm vận hành phải tổng hợp thủ công để tìm nguyên nhân lặp lại. |

## Sàng lọc nhanh

Ba bài toán được chọn cho Phase 2 là #1, #2 và #3 vì có tác nhân cụ thể, workflow lặp lại, đầu vào/đầu ra có thể mô tả rõ và metric có thể đo bằng log. Trong đó, bài toán #1 có ảnh hưởng trực tiếp đến an toàn nên AI chỉ được đề xuất; điều phối viên vẫn là người phê duyệt hành động.

---

# Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## Quick Problem Card #1 — Hỗ trợ điều phối sự cố pin xe Xanh SM

- **Bài toán (1 câu):** Rút ngắn thời gian điều phối khi tài xế báo pin yếu hoặc không thể tiếp tục hành trình mà không tự động hóa quyết định có rủi ro an toàn.
- **Công ty thành viên:** Xanh SM (GSM).
- **Actor đang gặp khó khăn:** Tài xế chờ hỗ trợ; điều phối viên phải tra cứu nhiều nguồn trong tình huống gấp.
- **Workflow thủ công hiện tại:**
  1. Tài xế gọi/chat báo vị trí, mức pin và tình trạng xe.
  2. Điều phối viên hỏi lại các dữ kiện còn thiếu.
  3. Điều phối viên mở bản đồ và tra cứu trạm/đội hỗ trợ phù hợp.
  4. Điều phối viên đánh giá phương án, soạn chỉ dẫn cho tài xế.
  5. Tài xế xác nhận; điều phối viên cập nhật ticket.
- **Bottleneck:** Bước 2–4, ước tính **12 phút/lượt**; dễ bỏ sót mức pin, khoảng cách hoặc trạng thái trạm khi phải chuyển qua nhiều màn hình.
- **AI tham gia:** Chuẩn hóa nội dung báo sự cố, phát hiện trường còn thiếu, tổng hợp dữ liệu từ công cụ được cấp quyền và tạo **bản nháp** phương án. Nếu pin dưới 5%, hệ thống không được đề xuất trạm cách quá 5 km và phải chuyển sang đề xuất điều xe sạc/cứu hộ. Mọi hành động cần điều phối viên duyệt.
- **Metric thành công:** Sau pilot 4 tuần, giảm median thời gian từ lúc nhận đủ dữ kiện đến lúc có phương án được duyệt từ **12 phút xuống ≤ 3 phút**; **100%** ca pin dưới 5% không được gợi ý trạm quá 5 km; **100%** tin nhắn AI có nhãn `[DRAFT_ONLY]`.
- **Quick Architecture:** **LLM feature + rules**, không dùng agent tự hành. Rule thực thi ngưỡng an toàn; LLM trích xuất dữ kiện và soạn bản nháp; con người phê duyệt.

## Quick Problem Card #2 — Phân loại và chuyển tuyến phản ánh cư dân Vinhomes

- **Bài toán (1 câu):** Hỗ trợ CSKH phân loại phản ánh tự do của cư dân và đề xuất đúng đội xử lý ngay ở lần chuyển đầu tiên.
- **Công ty thành viên:** Vinhomes.
- **Actor đang gặp khó khăn:** Nhân viên CSKH, đội kỹ thuật/an ninh/vệ sinh nhận ticket và cư dân đang chờ giải quyết.
- **Workflow thủ công hiện tại:**
  1. Cư dân gửi nội dung và ảnh qua ứng dụng.
  2. CSKH đọc, tìm tòa/căn hộ và yêu cầu bổ sung thông tin.
  3. CSKH chọn danh mục, mức ưu tiên và bộ phận phụ trách.
  4. Bộ phận tiếp nhận kiểm tra; ticket sai tuyến được trả lại.
  5. CSKH cập nhật trạng thái cho cư dân.
- **Bottleneck:** Bước 2–3, ước tính **8 phút/ticket**; mô tả mơ hồ và nhiều ý trong cùng một phản ánh làm tăng lỗi chuyển tuyến.
- **AI tham gia:** Tóm tắt nội dung, trích xuất vị trí/sự cố, đề xuất nhãn và câu hỏi bổ sung. Rule ưu tiên các từ khóa nguy hiểm như cháy, khói, rò điện hoặc mắc kẹt; AI không tự kết luận tình trạng khẩn cấp và không tự đóng ticket.
- **Metric thành công:** Giảm median thời gian phân loại từ **8 phút xuống ≤ 2 phút**; tăng tỷ lệ chuyển đúng bộ phận ngay lần đầu từ baseline đo trong tuần 0 lên **≥ 90%**; **100%** ticket khẩn cấp được con người kiểm tra trước khi chuyển.
- **Quick Architecture:** **LLM feature + rule routing**. LLM xử lý ngôn ngữ tự do; rule chặn và nâng mức ưu tiên; CSKH duyệt nhãn cuối.

## Quick Problem Card #3 — Đối soát hóa đơn và phiên sạc VinFast

- **Bài toán (1 câu):** Tự động đối chiếu dữ liệu có cấu trúc và chỉ đưa các trường hợp bất thường cho nhân viên xử lý.
- **Công ty thành viên:** VinFast.
- **Actor đang gặp khó khăn:** Nhân viên tài chính/đối soát và đơn vị vận hành trạm sạc.
- **Workflow thủ công hiện tại:**
  1. Tải hóa đơn, log phiên sạc và bảng giá của kỳ.
  2. Chuẩn hóa mã trạm, thời gian, số điện và thuế.
  3. Ghép từng dòng hóa đơn với phiên sạc tương ứng.
  4. Tính lại số tiền, đánh dấu sai lệch và tìm chứng từ.
  5. Lập danh sách ngoại lệ để xác minh với đối tác.
- **Bottleneck:** Bước 2–4, ước tính **6 phút/dòng ngoại lệ**; mã không đồng nhất và dữ liệu thiếu gây dò tìm lặp lại.
- **AI tham gia:** Không dùng LLM cho phép tính. Rule/SQL thực hiện chuẩn hóa, matching, tính tiền và kiểm tra dung sai; AI chỉ có thể giải thích ngoại lệ bằng ngôn ngữ tự nhiên sau khi kết quả đã được tính xác định.
- **Metric thành công:** Tự động đối soát **≥ 95%** dòng khớp chính xác; giảm thời gian xử lý một dòng ngoại lệ từ **6 phút xuống ≤ 2 phút**; sai số tính toán của pipeline trên bộ test chuẩn bằng **0**.
- **Quick Architecture:** **Rule-based, không cần AI ở lõi**. Đây là bài toán dữ liệu có cấu trúc và quy tắc kế toán xác định; LLM là tùy chọn cho phần giải thích, không tham gia phê duyệt thanh toán.

---

## Kết luận cá nhân

Tôi ưu tiên Card #1 để phát triển sâu hơn vì giá trị thời gian rõ, khớp với prototype prompt trong repo và có ranh giới an toàn kiểm thử được. Tuy nhiên, đây không phải bài toán phù hợp cho agent tự hành: dữ liệu vị trí/trạm phải đến từ hệ thống đáng tin cậy, ngưỡng an toàn phải được khóa bằng rule, và điều phối viên phải phê duyệt trước khi gửi chỉ dẫn hoặc gọi đội hỗ trợ.
