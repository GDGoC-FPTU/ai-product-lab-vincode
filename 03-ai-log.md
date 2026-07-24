# 03 - AI Log & Reflection

> Bài cá nhân - Phase 6  
> Chủ đề: Sử dụng AI như thought-partner trong Lab 02 - AI Product Scoping.

---

## 1. Tôi đã dùng AI để làm gì?

Trong bài lab này, tôi dùng AI như một thought-partner để hỗ trợ ba việc chính.

Thứ nhất, tôi dùng AI để brainstorm các pain point vận hành trong hệ sinh thái Vingroup. Ban đầu tôi chỉ nghĩ đến các bài toán rõ như chatbot chăm sóc khách hàng, nhưng khi trao đổi với AI, tôi mở rộng được danh sách sang các quy trình có tính vận hành hơn: điều phối xe Xanh SM khi pin thấp, đối chiếu hóa đơn sạc điện VinFast, phân loại phản ánh cư dân Vinhomes, và tóm tắt hồ sơ xuất viện Vinmec.

Thứ hai, tôi dùng AI để biến các ý tưởng thành Quick Problem Cards có cấu trúc. AI giúp tôi nhớ phải ghi rõ actor, workflow thủ công, bottleneck, metric thành công và quick architecture. Phần này hữu ích vì nếu chỉ viết bằng cảm tính thì bài toán rất dễ bị chung chung.

Thứ ba, tôi dùng AI để viết và chỉnh sửa `SYSTEM_PROMPT` cho file `prompt_prototype.py`. AI hỗ trợ tạo operational boundaries cho use case Xanh SM: mọi output phải có tag `[DRAFT_ONLY]`, và nếu pin dưới 5% thì không được đề xuất trạm sạc xa hơn 5km mà phải dispatch mobile charger.

---

## 2. AI đã sai hoặc thiếu ở đâu?

AI giúp nhanh nhưng không phải lúc nào cũng dùng ngay.

Điểm sai/thiếu đầu tiên là một số gợi ý ban đầu quá rộng, giống như mô tả sản phẩm AI hơn là bài toán vận hành. Ví dụ, nếu chỉ nói "trợ lý điều phối thông minh" thì chưa rõ ai đang đau, bước nào tốn thời gian, và đo thành công bằng số nào. Tôi phải yêu cầu cụ thể hơn: hiện tại điều phối viên làm gì, mất bao nhiêu phút, lỗi nằm ở đâu.

Điểm sai/thiếu thứ hai là AI có xu hướng đề xuất automation quá mạnh. Trong bài toán Xanh SM, nếu AI tự động gửi tin nhắn hoặc tự động điều xe mà không có người duyệt thì rủi ro cao. Vì vậy tôi phải thêm ranh giới Human-in-the-loop: AI chỉ tạo draft, không được tự claim là đã gửi tin, đã gọi tài xế, hay đã dispatch thật.

Điểm sai/thiếu thứ ba là prompt ban đầu chưa thật sát slide của đề bài. Sau khi đối chiếu worksheet, tôi chỉnh lại `SYSTEM_PROMPT` để ghi rõ vai trò "intelligent dispatcher co-pilot for Xanh SM", rule `[DRAFT_ONLY]`, rule pin dưới 5%, và JSON command `dispatch_mobile_charger`.

---

## 3. Tôi đã sửa và cải thiện như thế nào?

Tôi sửa bài theo hướng problem-first, AI-second.

Với file `01-problem-scan.md`, tôi không chỉ liệt kê tên ý tưởng mà thêm lens, actor, workflow, bottleneck và metric. Điều này giúp mỗi bài toán có thể được đánh giá bằng tiêu chí vận hành thay vì chỉ nghe có vẻ hay.

Với file `prompt_prototype.py`, tôi thêm boundary rõ ràng vào system prompt:

- Mọi câu trả lời cho tài xế phải bắt đầu bằng `[DRAFT_ONLY]`.
- Pin dưới 5% là tình huống nguy cấp.
- Nếu pin dưới 5%, AI không được điều hướng đến trạm sạc xa hơn 5km.
- Trường hợp nguy cấp phải trả structured JSON để dispatch mobile charger.
- AI không được tự gửi tin nhắn hay tự thực thi hành động ngoài đời.

Tôi cũng dùng adversarial tests để kiểm tra prompt. Hai kiểu tấn công chính là: người dùng cố tình báo pin 2% nhưng đòi đi trạm sạc 8km, và người dùng yêu cầu bỏ tag `[DRAFT_ONLY]`. Nếu model vẫn giữ đúng hai rule này thì boundary tạm thời đạt yêu cầu của prototype.

---

## 4. Bài học cá nhân

Bài học lớn nhất của tôi là AI rất mạnh khi đóng vai người phản biện và người giúp cấu trúc hóa suy nghĩ, nhưng người làm sản phẩm vẫn phải chịu trách nhiệm về ranh giới vận hành. Một prompt nghe hay chưa đủ; prompt phải gắn với rủi ro thật, metric thật và test case có tính tấn công.

Nếu tiếp tục phát triển prototype này, tôi sẽ bổ sung thêm dữ liệu giả lập gồm vị trí xe, danh sách trạm sạc, khoảng cách và trạng thái trụ sạc. Khi đó model sẽ không chỉ trả lời theo text mà có thể được test bằng nhiều trường hợp gần với vận hành thực tế hơn.