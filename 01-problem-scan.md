# 01 - Problem Scan

## Phase 1 — SCAN

### List bài toán

| # | Subsidiary | Lens             | Mô tả bài toán                                                                                                                                                                                  |
| - | ---------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Xanh SM    | Stakeholder Pain | Khi xe điện sắp hết pin, tài xế phải tự liên hệ tổng đài để xin hướng dẫn. Dispatcher phải tra cứu mức pin, vị trí và khoảng cách tới trạm sạc, dẫn đến xử lý chậm và có nguy cơ hướng dẫn sai. |
| 2 | Xanh SM    | Repetitive       | Dispatcher phải trả lời nhiều yêu cầu giống nhau như hướng dẫn đến trạm sạc, kiểm tra trạng thái pin và điều phối xe cứu hộ nhiều lần mỗi ngày.                                                 |
| 3 | VinFast    | Time-consuming   | Nhân viên kỹ thuật phải kiểm tra thủ công dữ liệu xe để xác định lịch bảo dưỡng phù hợp cho từng khách hàng.                                                                                    |
| 4 | Vinmec     | AI-upgrade       | Tổng đài chăm sóc khách hàng trả lời các câu hỏi phổ biến về lịch khám, bác sĩ và chuyên khoa còn thủ công, gây thời gian chờ lâu.                                                              |
| 5 | Vinhomes   | Time-consuming   | Ban quản lý phải đọc và phân loại nhiều phản ánh của cư dân trước khi chuyển đúng bộ phận xử lý.                                                                                                |

---

# Phase 2 — QUICK-ASSESS

## QUICK PROBLEM CARD #1

**Problem**

Hỗ trợ điều phối tài xế Xanh SM khi pin xe điện sắp cạn.

**Company**

☑ Xanh SM

**Actor**

Dispatcher (Điều phối viên tổng đài)

**Current Workflow**

1. Tài xế gọi tổng đài.
2. Dispatcher hỏi mức pin và vị trí hiện tại.
3. Dispatcher tra cứu trạm sạc gần nhất.
4. Dispatcher quyết định hướng dẫn đến trạm sạc hoặc điều xe cứu hộ.
5. Dispatcher soạn tin nhắn gửi tài xế.

**Bottleneck**

Dispatcher phải tự đánh giá mức độ an toàn dựa trên pin và khoảng cách.

**Estimated Time**

5–8 phút/lượt.

**AI Support**

AI tự động đánh giá mức pin, áp dụng Operational Boundary và sinh hướng dẫn hoặc JSON điều xe sạc lưu động.

**Success Metric**

* Giảm thời gian xử lý từ **6 phút xuống dưới 1 phút**.
* 100% trường hợp pin dưới 5% không hướng dẫn đến trạm sạc quá 5 km.

**Quick Architecture**

☐ No AI

☑ Rule + LLM

☑ Agent (Dispatcher Co-pilot)

---

## QUICK PROBLEM CARD #2

**Problem**

Tự động phân loại phản ánh của cư dân Vinhomes.

**Company**

☑ Vinhomes

**Actor**

Nhân viên chăm sóc cư dân.

**Current Workflow**

1. Cư dân gửi phản ánh.
2. Nhân viên đọc nội dung.
3. Xác định loại sự cố.
4. Chuyển đúng bộ phận.

**Bottleneck**

Đọc và phân loại thủ công.

**Estimated Time**

3 phút/yêu cầu.

**AI Support**

LLM phân loại nội dung và đề xuất bộ phận xử lý.

**Success Metric**

90% phản ánh được phân loại đúng ngay lần đầu.

**Quick Architecture**

☑ LLM

---

## QUICK PROBLEM CARD #3

**Problem**

Tự động trả lời câu hỏi phổ biến của khách hàng Vinmec.

**Company**

☑ Vinmec

**Actor**

Nhân viên tổng đài.

**Current Workflow**

1. Khách gọi.
2. Tổng đài tiếp nhận.
3. Tra cứu thông tin.
4. Trả lời.

**Bottleneck**

Tra cứu thủ công.

**Estimated Time**

4 phút/cuộc gọi.

**AI Support**

LLM trả lời các câu hỏi phổ biến, nhân viên chỉ kiểm duyệt.

**Success Metric**

80% câu hỏi phổ biến được xử lý trong dưới 15 giây.

**Quick Architecture**

☑ LLM
