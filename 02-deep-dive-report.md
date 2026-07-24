# 📖 Báo Cáo Phân Tích Sâu (Deep-Dive Report) — AI Product Scoping

---

### 👥 THÔNG TIN NHÓM & THÀNH VIÊN
* **Tên Nhóm:** VinCode
* **Công ty thành viên lựa chọn:** **GSM (Xanh SM)** — Vận hành taxi điện thông minh
* **Bài toán lựa chọn:** Điều phối khẩn cấp sự cố sạc pin / cạn pin thực địa cho tài xế Xanh SM
* **Danh Sách Thành Viên Tham Gia:**
  1. **Nguyễn Hồng Yến** | MSSV: 2A202601065
  2. **Nguyễn Thị Mừng** | MSSV: 2A202601571
  3. **Nguyễn Thành Duy** | MSSV: Nguyen-thanhduy16
  4. **Vũ Hải Nam** | MSSV: VuHaiNam
  5. **Tony** | MSSV: tonytony3003

---

## 🏛️ 1. Bối cảnh & Lý do lựa chọn bài toán

Thông qua khảo sát thực địa tại Trung tâm Điều vận Xanh SM, nhóm chúng tôi nhận thấy các điều phối viên (Dispatchers) đang gặp áp lực rất lớn khi xử lý các cuộc gọi báo sự cố sạc pin từ tài xế trong giờ cao điểm.

### Lý do chọn bài toán "Xử lý sự cố sạc pin Xanh SM" và loại bỏ bài toán khác:
* **Chọn Bài toán Xanh SM (Sự cố pin thực địa):** Tác động trực tiếp đến vận hành thời gian thực (Real-time operations). Xử lý chậm làm lãng phí thời gian tài xế, gây rò rỉ doanh thu cuốc xe và nguy cơ cạn pin giữa đường gây tắc nghẽn giao thông.
* **Loại bỏ Bài toán Vinhomes CSKH:** Rủi ro pháp lý cao nếu phản hồi sai thông tin phí quản lý/hợp đồng cư dân.
* **Loại bỏ Bài toán Xanh SM Hủy chuyến:** Là tác động phân tích offline (Back-office), không giải quyết nỗi đau khẩn cấp thời gian thực.

---

## 🏗️ 2. Problem Statement (Bảng 6 trường thông tin chuẩn Vin Smart Future)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều vận Xanh SM (GSM). |
| **2. Current Workflow** | Khi tài xế báo sự cố sắp hết pin (< 10%), Điều phối viên phải: (1) Nhận cuộc gọi ➔ (2) Tra cứu thủ công vị trí GPS xe ➔ (3) Tra cứu trạm sạc VinFast còn trụ trống ➔ (4) Soạn tin nhắn hướng dẫn gửi qua App ➔ (5) Gọi cứu hộ pin nếu < 5%. Tổng 5 bước thủ công, mất ~15 phút/lượt. |
| **3. Bottleneck** | **Bước 3 & 4 (mất 10 phút/lượt):** Tra cứu thủ công trạm sạc trống tương thích với dòng xe (VF5/VF8/VF9) và tự gõ văn bản chỉ đường gửi cho tài xế. |
| **4. Business Impact** | Mỗi ngày có ~80 sự cố pin tại Hà Nội. Lãng phí 20 giờ làm việc/ngày của team điều vận. Tăng thời gian chờ đợi của tài xế, gây sụt giảm ~15% hiệu suất đón khách và tài xế căng thẳng. |
| **5. Success Metric** | 1. Giảm thời gian xử lý sự cố từ **15 phút ──> dưới 3 phút** (Efficiency).<br>2. Đảm bảo 100% hướng dẫn đúng trạm sạc trống và loại cổng sạc phù hợp (Quality). |
| **6. Operational Boundary** | AI được phép truy xuất vị trí GPS, API trạm sạc VinFast, tự động soạn nháp tin nhắn hướng dẫn. **CẤM:** AI không được tự động gửi tin đi nếu chưa có điều phối viên duyệt (`[DRAFT_ONLY]`); tuyệt đối không chỉ đường tới trạm sạc xa hơn 5km nếu pin < 5% (bắt buộc trả JSON kích hoạt xe sạc di động). |

---

## 🔄 3. Future-State Flow & AI Fit

* **Lựa chọn AI Fit:** **LLM Feature** (Soạn nháp chỉ dẫn + Phản xạ quy tắc an toàn). Không chọn Agent tự trị hoàn toàn vì rủi ro điều hướng sai có thể làm xe chết máy giữa đường.
* **Quy trình vận hành tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │ ──→ │ Auto-pull    │ ──→ │ AI Soạn nháp │ ──→ │ Điều phối    │
│ gọi sự cố    │     │ Vị trí & Trạm│     │ Tin nhắn     │     │ viên Click   │
│              │     │ sạc trống    │     │ [DRAFT_ONLY] │     │ Duyệt & Gửi  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI bị lỗi,
                                                               Dispatcher tự nhập
                                                               thủ công như cũ.
```

---

## 💻 4. Nguyên mẫu Prompt & Kiểm thử Ranh giới (Prompt Prototype)

Nhóm đã xây dựng và kiểm thử thành công nguyên mẫu tại `starter-code/prompt_prototype.py` với model **Google Gemini 3.6 Flash**:

1. **Ranh giới [RULE 1]:** Bắt buộc mọi tin nhắn draft phải bắt đầu bằng tiền tố `[DRAFT_ONLY]`. Khi người dùng cố tình tấn công ép bỏ thẻ, Gemini 3.6 Flash đã bảo vệ ranh giới thành công.
2. **Ranh giới [RULE 2]:** Khi tài xế báo pin còn 2% (dưới 5%) và đòi chỉ đường tới trạm sạc xa 8km, mô hình lập tức chặn và trả về đúng định dạng JSON: `{"action": "dispatch_mobile_charger", "reason": "..."}`.

---

## 🏁 5. Evaluate & Quyết định dự án

* **Quyết định:** **GO (Tiến hành triển khai)**.
* **Luận điểm:** Bài toán có nỗi đau rõ ràng, metric đo lường bằng con số cụ thể (15 phút ➔ 3 phút), kiến trúc LLM Feature đơn giản, chi phí thấp và ranh giới an toàn được bảo vệ 100% qua programmatic stress-testing.
