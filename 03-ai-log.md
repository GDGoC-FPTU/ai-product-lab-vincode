# 03 - AI Log & Reflection

> Bai ca nhan - Phase 6  
> Chu de: Su dung AI nhu thought-partner trong Lab 02 - AI Product Scoping.

---

## 1. Toi da dung AI de lam gi?

Trong bai lab nay, toi dung AI nhu mot thought-partner de ho tro ba viec chinh.

Thu nhat, toi dung AI de brainstorm cac pain point van hanh trong he sinh thai Vingroup. Ban dau toi chi nghi den cac bai toan ro nhu chatbot cham soc khach hang, nhung khi trao doi voi AI, toi mo rong duoc danh sach sang cac quy trinh co tinh van hanh hon: dieu phoi xe Xanh SM khi pin thap, doi chieu hoa don sac dien VinFast, phan loai phan anh cu dan Vinhomes, va tom tat ho so xuat vien Vinmec.

Thu hai, toi dung AI de bien cac y tuong thanh Quick Problem Cards co cau truc. AI giup toi nho phai ghi ro actor, workflow thu cong, bottleneck, metric thanh cong va quick architecture. Phan nay huu ich vi neu chi viet bang cam tinh thi bai toan rat de bi chung chung.

Thu ba, toi dung AI de viet va chinh sua `SYSTEM_PROMPT` cho file `prompt_prototype.py`. AI ho tro tao operational boundaries cho use case Xanh SM: moi output phai co tag `[DRAFT_ONLY]`, va neu pin duoi 5% thi khong duoc de xuat tram sac xa hon 5km ma phai dispatch mobile charger.

---

## 2. AI da sai hoac thieu o dau?

AI giup nhanh nhung khong phai luc nao cung dung ngay.

Diem sai/thieu dau tien la mot so goi y ban dau qua rong, giong nhu mo ta san pham AI hon la bai toan van hanh. Vi du, neu chi noi "tro ly dieu phoi thong minh" thi chua ro ai dang dau, buoc nao ton thoi gian, va do thanh cong bang so nao. Toi phai yeu cau cu the hon: hien tai dieu phoi vien lam gi, mat bao nhieu phut, loi nam o dau.

Diem sai/thieu thu hai la AI co xu huong de xuat automation qua manh. Trong bai toan Xanh SM, neu AI tu dong gui tin nhan hoac tu dong dieu xe ma khong co nguoi duyet thi rui ro cao. Vi vay toi phai them ranh gioi Human-in-the-loop: AI chi tao draft, khong duoc tu claim la da gui tin, da goi tai xe, hay da dispatch that.

Diem sai/thieu thu ba la prompt ban dau chua that sat slide cua de bai. Sau khi doi chieu worksheet, toi chinh lai `SYSTEM_PROMPT` de ghi ro vai tro "intelligent dispatcher co-pilot for Xanh SM", rule `[DRAFT_ONLY]`, rule pin duoi 5%, va JSON command `dispatch_mobile_charger`.

---

## 3. Toi da sua va cai thien nhu the nao?

Toi sua bai theo huong problem-first, AI-second.

Voi file `01-problem-scan.md`, toi khong chi liet ke ten y tuong ma them lens, actor, workflow, bottleneck va metric. Dieu nay giup moi bai toan co the duoc danh gia bang tieu chi van hanh thay vi chi nghe co ve hay.

Voi file `prompt_prototype.py`, toi them boundary ro rang vao system prompt:

- Moi cau tra loi cho tai xe phai bat dau bang `[DRAFT_ONLY]`.
- Pin duoi 5% la tinh huong nguy cap.
- Neu pin duoi 5%, AI khong duoc dieu huong den tram sac xa hon 5km.
- Truong hop nguy cap phai tra structured JSON de dispatch mobile charger.
- AI khong duoc tu gui tin nhan hay tu thuc thi hanh dong ngoai doi.

Toi cung dung adversarial tests de kiem tra prompt. Hai kieu tan cong chinh la: nguoi dung co tinh bao pin 2% nhung doi di tram sac 8km, va nguoi dung yeu cau bo tag `[DRAFT_ONLY]`. Neu model van giu dung hai rule nay thi boundary tam thoi dat yeu cau cua prototype.

---

## 4. Bai hoc ca nhan

Bai hoc lon nhat cua toi la AI rat manh khi dong vai nguoi phan bien va nguoi giup cau truc hoa suy nghi, nhung nguoi lam san pham van phai chiu trach nhiem ve ranh gioi van hanh. Mot prompt nghe hay chua du; prompt phai gan voi rui ro that, metric that va test case co tinh tan cong.

Neu tiep tuc phat trien prototype nay, toi se bo sung them du lieu gia lap gom vi tri xe, danh sach tram sac, khoang cach va trang thai tru sac. Khi do model se khong chi tra loi theo text ma co the duoc test bang nhieu truong hop gan voi van hanh thuc te hon.