# 🔍 Phase 1 — SCAN (Cá nhân)

### 📝 List bài toán của tôi:
| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM | Stakeholder Pain | Tài xế phàn nàn hệ thống điều phối không tối ưu khi xe sắp hết pin, dễ gây sập nguồn giữa đường. |
| 2 | Vinmec | Time-consuming | Bác sĩ tốn quá nhiều thời gian gõ hồ sơ bệnh án thủ công sau mỗi ca khám. |
| 3 | Vinhomes | Repetitive | Nhân viên CSKH phải trả lời lặp đi lặp lại các câu hỏi của cư dân về phí dịch vụ, giờ mở hồ bơi. |
| 4 | VinFast | AI-upgrade | Tổng đài viên gặp khó khăn khi chẩn đoán lỗi xe qua mô tả mơ hồ của khách hàng. |
| 5 | Vinpearl | Repetitive | Phân loại hàng nghìn email đặt phòng và phản ánh của khách hàng mỗi ngày một cách thủ công. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân)

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Hỗ trợ điều phối an toàn khi xe taxi điện sắp cạn pin │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên điều phối (Dispatcher) và Tài xế │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Tài xế báo pin yếu ──> 2. Điều phối viên xem bản đồ ──>│
│   3. Tính toán khoảng cách trạm sạc ──> 4. Nhắn tin điều hướng│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 3-5 phút/lượt)│
│ AI nhảy vào hỗ trợ ở bước nào? Phân tích toạ độ & tự soạn tin │
│                                                             │
│ Đo thành công bằng gì? Giảm thời gian điều phối từ 5p -> <30s │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Trợ lý AI nghe và tự động điền hồ sơ bệnh án      │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ khám bệnh                       │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Bác sĩ khám ──> 2. Ghi chú ra giấy ──>                 │
│   3. Cuối ngày ngồi gõ lại vào hệ thống ──> 4. Lưu hồ sơ    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 10 phút/hồ sơ)   │
│ AI nhảy vào hỗ trợ ở bước nào? Chuyển giọng nói thành văn bản │
│ và trích xuất đúng trường thông tin (Triệu chứng, Đơn thuốc)│
│                                                             │
│ Đo thành công bằng gì? Giảm thời gian nhập liệu 80%         │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: AI Chatbot tự động giải đáp thắc mắc của cư dân   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên Chăm sóc khách hàng (CSKH)   │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Cư dân gửi câu hỏi qua App ──> 2. NV CSKH đọc ──>      │
│   3. Tìm kiếm cẩm nang ──> 4. Gõ câu trả lời gửi lại        │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 5 phút/lượt) │
│ AI nhảy vào hỗ trợ ở bước nào? Đọc câu hỏi và tự sinh câu trả │
│ lời dựa trên Cẩm nang cư dân (RAG).                         │
│                                                             │
│ Đo thành công bằng gì? Tỷ lệ tự động trả lời thành công >70%│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
