# 🚀 Phase 3 & 5: DEEP-DIVE REPORT (Báo Cáo Nhóm)

**Tên Nhóm:** [Điền Tên Nhóm]
**Thành viên 1:** [Họ tên] - [MSSV]
**Thành viên 2:** [Họ tên] - [MSSV]
**Thành viên 3:** [Họ tên] - [MSSV]
**Thành viên 4:** [Họ tên] - [MSSV]
**Thành viên 5:** [Họ tên] - [MSSV]
**Thành viên 6:** [Họ tên] - [MSSV]

## Quyết định lựa chọn
Nhóm thống nhất chọn bài toán: **Hỗ trợ điều phối an toàn khi xe taxi điện (Xanh SM) sắp cạn pin.**

---

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên điều phối (Dispatcher) tại trung tâm điều hành Xanh SM. |
| **2. Current Workflow** | Tài xế báo pin yếu -> Điều phối viên kiểm tra bản đồ -> Đo khoảng cách trạm sạc gần nhất -> Nhắn tin điều hướng. |
| **3. Bottleneck** | Bước kiểm tra bản đồ và đo khoảng cách thủ công rất dễ sai sót khi áp lực cao, có thể vô tình điều xe sắp hết pin đi quá xa. |
| **4. Business Impact** | Xe sập nguồn giữa đường gây cản trở giao thông, tốn chi phí gọi cứu hộ cẩu xe, và làm ảnh hưởng nghiêm trọng đến trải nghiệm khách hàng. |
| **5. Success Metric** | Rút ngắn thời gian xử lý điều phối từ 3-5 phút xuống dưới 30 giây. Tỷ lệ điều sai trạm sạc (với xe < 5% pin) = 0%. |
| **6. Operational Boundary** | AI **KHÔNG** được gửi tin nhắn trực tiếp cho tài xế (phải có tag `[DRAFT_ONLY]` để duyệt). AI **TUYỆT ĐỐI KHÔNG** được gợi ý trạm sạc > 5km nếu pin < 5% (phải chuyển sang điều xe sạc lưu động). |

---

## 3.3. Future-State Flow & AI Fit
* **Mức độ AI Fit:** [x] LLM Feature (Xử lý ngôn ngữ tự nhiên để soạn tin nhắn và trích xuất quyết định điều phối).

**Future-State Flow (Quy trình tương lai):**
1. Tài xế báo cáo tình trạng pin về hệ thống.
2. 🔵 **AI Step:** Hệ thống AI tự động đọc toạ độ và mức pin. Sinh ra một bản nháp tin nhắn (`[DRAFT_ONLY]`) hoặc mã lệnh điều xe sạc lưu động.
3. 🟢 **Human Step (HITL):** Nhân viên điều phối đọc bản nháp của AI, kiểm tra nhanh và bấm nút "Gửi/Phê duyệt".
4. ↩️ **Fallback:** Nếu AI đưa ra gợi ý không hợp lý hoặc API lỗi, nhân viên điều phối sẽ gõ tin nhắn thủ công như quy trình cũ.

---

# 🏁 Phase 5 — EVALUATE 

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? *(Có dữ liệu toạ độ GPS và trạng thái pin từ hệ thống quản lý xe).*
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát? *(Có, vì mọi quyết định đều phải qua bước Human-in-the-loop).*
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? *(Có, vì nó giúp nhân viên điều phối nhàn hơn rất nhiều).*

### Quyết định cuối cùng của nhóm:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp để hỗ trợ ngay lập tức.
[ ] **NOT YET** 
[ ] **NO-GO**

**Justification (Lý giải quyết định):**
Bài toán này hoàn toàn khả thi (GO) vì nó không đòi hỏi AI tự đưa ra quyết định rủi ro cao (tất cả đều qua người duyệt). Nó sử dụng khả năng xử lý ngôn ngữ và JSON parsing của LLM (Gemini) để giảm tải tác vụ soạn tin nhắn. Việc thiết lập ranh giới cứng (temperature = 0 và system prompt gắt gao) đã chứng minh độ hiệu quả 100% trong bản test `prompt_prototype.py`.
