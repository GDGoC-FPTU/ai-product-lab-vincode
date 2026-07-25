# 🔍 Phase 1 & 2 Deliverable: Problem Scan & Quick Problem Cards

**Họ và tên:** Nguyễn Văn A  
**MSSV:** 20230001  
**Đơn vị / Dự án:** Vin Smart Future (Vingroup) — AI Product Scoping Lab  

---

# 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Tối Ưu Bằng AI

Áp dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain) để tìm kiếm các bài toán vận hành thực tế tại các công ty thành viên Vingroup.

| # | Công ty thành viên (Subsidiary) | Lens áp dụng | Mô tả ngắn bài toán & Pain Point |
|---|----------------------------------|--------------|-----------------------------------|
| 1 | **Xanh SM (GSM)** | Lặp lại | So khớp và phân bổ lại cuốc xe khi khách hàng yêu cầu thay đổi điểm đến giữa chừng trong giờ cao điểm. |
| 2 | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế xe điện về sự cố pin/cạn pin thực địa (mất 15-20 min/lượt). |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện tự động và đối chiếu dữ liệu dòng tiền trạm sạc đối tác hằng tuần. |
| 4 | **Vinhomes** | AI-upgrade | Phân loại tự động và gợi ý phản hồi các khiếu nại của cư dân trên App Vinhomes Resident (hiện xử lý rập khuôn, mất 12 tiếng). |
| 5 | **Vinmec** | Pain từ người khác | Bác sĩ tốn 20-30 phút/bệnh nhân để tổng hợp văn bản tóm tắt hồ sơ xuất viện thủ công, gây phàn nàn và chậm trễ quá tải. |
| 6 | **Xanh SM (GSM)** | Tốn thời gian | Phân tích tóm tắt lý do hủy chuyến từ file ghi âm cuộc gọi và ghi chú tài xế để tìm ra nguyên nhân lỗi hệ thống. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 bài toán tiềm năng nhất từ bảng SCAN để tiến hành phân tích nhanh.

---

### 🎴 QUICK PROBLEM CARD #1 (Bài toán được chọn Deep-Dive)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                   │
│                                                                         │
│ Bài toán: Tài xế Xanh SM báo sự cố sạc pin / cạn pin giữa đường cần     │
│ điều phối cứu hộ hoặc trạm sạc VinFast trống phù hợp gần nhất.          │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau (Actor)? Tài xế (chờ đợi), Điều phối viên (quá tải)         │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Tài xế gọi tổng đài điều vận báo sự cố hết pin                    │
│   ──> 2. Điều phối viên tra cứu vị trí GPS xe trên bản đồ nội bộ        │
│   ──> 3. Tra cứu thủ công các trạm sạc VinFast còn trụ trống            │
│   ──> 4. Soạn tin nhắn văn bản chỉ dẫn đường đi gửi qua App tài xế      │
│   ──> 5. Liên hệ đài cứu hộ pin di động nếu dung lượng pin < 5%         │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 10 phút/lượt)            │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4                        │
│ (Tự động lấy vị trí -> Tra cứu trạm trống -> Soạn nháp SMS chỉ dẫn)     │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ Giảm tổng thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt.        │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (Tự động soạn nháp thông điệp)      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 🎴 QUICK PROBLEM CARD #2

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                   │
│                                                                         │
│ Bài toán: Phân loại và tự động gợi ý câu trả lời khiếu nại dịch vụ      │
│ cho Ban quản lý cư dân Vinhomes trên ứng dụng Vinhomes Resident.        │
│ Công ty thành viên: [x] Vinhomes                                        │
│                                                                         │
│ Ai đang đau (Actor)? Ban quản lý khu đô thị, Nhân viên CSKH Vinhomes    │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Cư dân gửi phản hồi/khiếu nại lên App Vinhomes Resident            │
│   ──> 2. Nhân viên đọc và phân loại thủ công từng ý kiến                │
│   ──> 3. Tra cứu quy định/sổ tay khu đô thị để tìm cách xử lý           │
│   ──> 4. Soạn phản hồi cá nhân hóa và gửi tới cư dân                    │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 25 phút/phản hồi)        │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3                        │
│ (Phân loại chủ đề ticket + Tìm kiếm thông tin RAG + Soạn nháp trả lời)   │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ Giảm thời gian phản hồi phản ánh từ 12 giờ ──> dưới 1 giờ.              │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (System Prompt + RAG Tra cứu)       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 🎴 QUICK PROBLEM CARD #3

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                   │
│                                                                         │
│ Bài toán: Phân tích tự động nguyên nhân hủy chuyến của khách hàng taxi   │
│ Xanh SM từ dữ liệu cuộc gọi tổng đài và note tài xế.                    │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau (Actor)? Đội ngũ Quản lý Chất lượng Vận hành (QA/QC)        │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Trích xuất danh sách các cuốc xe bị hủy trong ngày                 │
│   ──> 2. Nhân viên nghe ngẫu nhiên các file ghi âm cuộc gọi tổng đài    │
│   ──> 3. Phân loại thủ công nguyên nhân hủy (do tài xế chậm, giá...)     │
│   ──> 4. Tổng hợp báo cáo Excel gửi lãnh đạo hàng tuần                  │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 30 phút/báo cáo 10 cuốc)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3                        │
│ (STT chuyển thoại thành văn bản + LLM Phân loại lý do hủy tự động)      │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ Phân tích 100% cuốc hủy theo thời gian thực thay vì chỉ sample 5%.     │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (Batch Text Processing)             │
└─────────────────────────────────────────────────────────────────────────┘
```
