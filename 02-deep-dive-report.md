#vincode - Ngô Đình Khánh - khanhngodinh7a@gmail.com
# 02 - Deep Dive Report

# AI Product Deep Dive

## Project

**Xanh SM Intelligent Dispatcher Co-pilot for EV Battery Depletion**

---
# 0. Thong tin nhom
Ten nhom: VinCode
Thanh vien: Dien ten va MSSV cac thanh vien tai day truoc khi nop bai.
Nguyen Thanh Duy - 2A202601599
Nguyen Minh Triet - 2A202601173
Nguyen Hong Yen - 2A202601065
Nguyen Thi Mung - 2A202601571
Dong Dai Huy - 2A202601901
Cong ty thanh vien duoc chon: Xanh SM / GSM
Don vi cong nghe gia dinh: Vin Smart Future
# 1. Selected Problem

Nhóm lựa chọn bài toán **hỗ trợ điều phối viên (Dispatcher) của Xanh SM xử lý các trường hợp xe điện sắp hết pin**.

Hiện nay, khi tài xế gặp tình trạng pin yếu, dispatcher phải thu thập thông tin thủ công, đánh giá khả năng di chuyển đến trạm sạc và quyết định nên hướng dẫn tài xế hay điều xe sạc lưu động. Quá trình này phụ thuộc nhiều vào kinh nghiệm cá nhân, mất thời gian và tiềm ẩn rủi ro nếu đánh giá sai.

---

# 2. Current-State Workflow

```
Driver detects low battery
        │
        ▼
Driver contacts Dispatcher
        │
        ▼
Dispatcher asks:
• Battery level
• Current GPS
• Vehicle status
        │
        ▼
Dispatcher searches nearest charging station
        │
        ▼
Dispatcher estimates:
• Remaining range
• Distance
• Traffic condition
        │
        ▼
Decision:
├── Reachable
│      │
│      ▼
│  Draft routing message
│
└── Not reachable
       │
       ▼
Dispatch mobile charging vehicle
       │
       ▼
Driver receives instruction
```

### Workflow Time

| Step                                 | Average Time  |
| ------------------------------------ | ------------- |
| Driver reports issue                 | 1 minute      |
| Information collection               | 2 minutes     |
| Dispatcher searches charging station | 2 minutes     |
| Decision making                      | 2 minutes     |
| Drafting response                    | 1 minute      |
| **Total**                            | **8 minutes** |

### Bottleneck

* Dispatcher phải tự đánh giá khoảng cách an toàn.
* Không có quy tắc thống nhất.
* Quyết định phụ thuộc kinh nghiệm.

---

# 3. Problem Statement (6 Fields)

| Field                | Description                                                                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Actor / Operator     | Dispatcher của Xanh SM                                                                                                                                                                                  |
| Current Workflow     | Tiếp nhận cuộc gọi, thu thập thông tin, tra cứu trạm sạc, đánh giá khả năng di chuyển, gửi hướng dẫn cho tài xế.                                                                                        |
| Bottleneck           | Đánh giá thủ công gây mất thời gian và có nguy cơ hướng dẫn sai khi pin quá thấp.                                                                                                                       |
| Business Impact      | Thời gian xử lý trung bình khoảng 8 phút/lượt, tăng thời gian chờ của tài xế và có nguy cơ xe hết pin giữa đường.                                                                                       |
| Success Metric       | Giảm thời gian xử lý xuống dưới 1 phút; 100% trường hợp pin dưới 5% không được hướng dẫn tới trạm sạc cách quá 5 km.                                                                                    |
| Operational Boundary | AI chỉ được tạo bản nháp hoặc JSON điều xe sạc. AI không được tự động gửi tin nhắn, không được bỏ qua bước phê duyệt của Dispatcher và không được hướng dẫn xe có pin dưới 5% đến trạm sạc xa hơn 5 km. |

---

# 4. AI Fit Analysis

| Solution     | Suitable | Reason                                                        |
| ------------ | -------- | ------------------------------------------------------------- |
| Rule-based   | ✓        | Kiểm tra ngưỡng pin dưới 5%.                                  |
| LLM Feature  | ✓        | Sinh hướng dẫn tự nhiên cho tài xế.                           |
| Agentic Loop | ✓        | Co-pilot hỗ trợ Dispatcher, không tự ra quyết định cuối cùng. |

**Chosen Architecture**

Rule Engine + LLM Co-pilot.

Rule Engine chịu trách nhiệm kiểm tra các điều kiện an toàn.

LLM chịu trách nhiệm sinh nội dung phản hồi.

Dispatcher là người phê duyệt cuối cùng.

---

# 5. Future-State Workflow

```
Driver reports battery issue
          │
          ▼
Dispatcher enters battery level
          │
          ▼
AI evaluates request
          │
          ▼
Rule Engine
          │
          ├──────── Battery <5%
          │
          ▼
Return JSON:
dispatch_mobile_charger
          │
          ▼
Dispatcher approves
          │
          ▼
Mobile charger dispatched

────────────────────────────

Battery ≥5%
          │
          ▼
LLM drafts routing message
          │
          ▼
[DRAFT_ONLY]
          │
          ▼
Dispatcher reviews
          │
          ▼
Message sent
```

---

# 6. Human-in-the-loop

Các quyết định cuối cùng luôn do Dispatcher thực hiện.

AI chỉ:

* đánh giá điều kiện,
* tạo bản nháp,
* sinh JSON điều xe.

Dispatcher có quyền:

* chỉnh sửa nội dung,
* từ chối đề xuất,
* thay đổi quyết định nếu có thông tin thực tế khác.

---

# 7. Fallback Strategy

Nếu AI:

* không chắc chắn mức pin,
* không xác định được khoảng cách,
* sinh kết quả không hợp lệ,

thì hệ thống sẽ:

1. yêu cầu Dispatcher nhập thêm dữ liệu;
2. hoặc chuyển hoàn toàn sang quy trình thủ công.

Không có trường hợp nào AI tự gửi hướng dẫn trực tiếp cho tài xế.

---

# 8. AI Readiness Checklist

| Checklist             | Status |
| --------------------- | ------ |
| Có dữ liệu mẫu        | ✅      |
| Có Human-in-the-loop  | ✅      |
| Có Fallback           | ✅      |
| Rủi ro được kiểm soát | ✅      |

---

# 9. Final Decision

## GO

### Justification

Nhóm quyết định **GO** vì bài toán có phạm vi rõ ràng, quy trình hiện tại tồn tại bottleneck cụ thể và có thể giảm đáng kể thời gian xử lý bằng AI.

Giải pháp kết hợp Rule Engine và LLM giúp đảm bảo các ràng buộc an toàn luôn được thực thi trước khi sinh phản hồi. Việc giữ Dispatcher trong vòng phê duyệt (Human-in-the-loop) giúp giảm rủi ro khi AI đưa ra đề xuất chưa phù hợp.

Dự án không yêu cầu AI tự động điều khiển phương tiện hay tự gửi thông tin đến tài xế, vì vậy mức độ rủi ro được đánh giá là thấp và phù hợp để triển khai prototype trong giai đoạn đầu.
