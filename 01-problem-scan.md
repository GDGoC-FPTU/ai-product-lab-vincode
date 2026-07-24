# 🔍 Bài Làm Cá Nhân 1: Problem Scan & Quick Assess

* **Họ và tên:** Nguyễn Hồng Yến 
* **MSSV:** 2A202601065

---

## 1. Phase 1 — SCAN: Bảng Quét Cơ Hội Vingroup

Sử dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác) để quét qua các hoạt động vận hành thực tế tại các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán / Cơ hội ứng dụng AI |
|---|------------|------|-----------------------------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố sạc pin hoặc cạn kiệt pin giữa đường (mất 15-20 phút/lượt). |
| 2 | **VinFast** | AI-upgrade | Trợ lý hướng dẫn trạm sạc thông minh: Tự động đề xuất trạm sạc trống và phù hợp với chuẩn cổng sạc của từng dòng xe điện (VF5, VF8, VF9). |
| 3 | **Vinhomes** | AI-upgrade | Phân loại và định tuyến (route) tự động các phản hồi/khiếu nại của cư dân trên App Vinhomes Resident để giảm thời gian phản hồi CSKH. |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện (mất 20-30 phút/bệnh nhân, gây quá tải cho đội ngũ y bác sĩ). |
| 5 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện hằng tuần và đối chiếu số liệu điện năng với các trạm sạc đối tác liên kết. |

---

## 2. Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn 3 bài toán tiềm năng nhất từ danh sách SCAN trên: **Card #1 (Xanh SM Sự cố sạc pin)**, **Card #2 (VinFast Trạm sạc thông minh)**, **Card #3 (Vinhomes CSKH Resident)**.

### 🃏 Quick Problem Card #1 — Xanh SM: Xử lý sự cố sạc pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo cáo sự cố sạc pin / cạn pin    │
│ giữa đường cần điều phối cứu hộ hoặc trạm sạc gần nhất.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (chờ đợi), Điều phối viên (quá tải)     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo hết pin               │
│   → 2. Điều phối viên tra cứu thủ công vị trí xe trên bản đồ│
│   → 3. Tra cứu thủ công các trạm sạc VinFast còn trụ trống 🔴│
│   → 4. Soạn tin nhắn chỉ dẫn/đường đi gửi qua App tài xế 🔴 │
│   → 5. Liên hệ đội xe cứu hộ nếu pin cạn kiệt (< 5%)        │
│                                                             │
│ Bước nào tốn nhất? Bước 3 & 4 (⏱ 10 phút/lượt)              │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Tự động tra cứu trạm sạc phù hợp & soạn nháp tin nhắn)     │
│                                                             │
│ Metric đo thành công:                                        │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Tự động soạn nháp)     │
└─────────────────────────────────────────────────────────────┘
```

### 🃏 Quick Problem Card #2 — VinFast: Trợ lý tư vấn trạm sạc tối ưu

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Đề xuất trạm sạc VinFast phù hợp với tuyến đường   │
│ và cổng sạc của các dòng xe điện (VF5, VF8, VF9).            │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau? Chủ xe điện VinFast (tốn thời gian tìm trạm)   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Chủ xe mở ứng dụng VinFast tìm trạm sạc                │
│   → 2. Lọc thủ công các trạm sạc dọc lộ trình               │
│   → 3. Kiểm tra cổng sạc tương thích với dòng xe đang đi 🔴   │
│   → 4. Dẫn đường đến trạm sạc                               │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 8 phút/lượt)               │
│ AI có thể nhảy vào ở bước nào? Bước 2 & 3                    │
│ (Phân tích dữ liệu xe & gợi ý trạm sạc trống tương thích)    │
│                                                             │
│ Metric đo thành công:                                        │
│ Rút ngắn thời gian tìm trạm sạc phù hợp từ 8 phút ──> 1 phút │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

### 🃏 Quick Problem Card #3 — Vinhomes: Tự động phân loại phản hồi cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Phân loại và định tuyến ý kiến phản hồi cư dân     │
│ trên ứng dụng Vinhomes Resident đến đúng ban quản lý.       │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Cư dân (chờ đợi), Nhân viên CSKH (quá tải)     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản hồi/khiếu nại lên App                  │
│   → 2. Nhân viên CSKH đọc và phân loại thủ công 🔴          │
│   → 3. Chuyển tiếp đến Ban Quản lý khu đô thị tương ứng 🔴  │
│   → 4. Soạn phản hồi mẫu gửi lại cư dân                     │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 12 giờ xử lý)              │
│ AI có thể nhảy vào ở bước nào? Bước 2 & 3                    │
│ (AI tự đọc nội dung phản hồi, phân loại & route tự động)    │
│                                                             │
│ Metric đo thành công:                                        │
│ Tăng tốc độ phản hồi cư dân từ 12 giờ ──> dưới 15 phút.      │
│                                                             │
│ Quick Architecture: [x] Rule-based + LLM Router             │
└─────────────────────────────────────────────────────────────┘
```
