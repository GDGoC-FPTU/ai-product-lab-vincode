# 01 - Problem Scan & Quick Cards

> Bai ca nhan - Phase 1 va Phase 2  
> Chu de uu tien: Vin Smart Future ho tro van hanh Xanh SM va cac cong ty thanh vien Vingroup.

---

## Phase 1 - SCAN: Danh sach 5 bai toan van hanh

| # | Subsidiary | Lens | Mo ta ngan bai toan |
|---|---|---|---|
| 1 | Xanh SM | Time-consuming | Dieu phoi vien mat nhieu thoi gian xu ly tai xe xe dien bao pin thap giua duong: tra GPS, tim tram sac, soan tin huong dan, quyet dinh co can xe sac di dong hay khong. |
| 2 | Xanh SM | Stakeholder Pain | Tai xe phan nan he thong goi y diem don/tra khach chua khop voi vi tri thuc te, dac biet tai khu do thi, san bay, trung tam thuong mai. |
| 3 | VinFast | Repetitive | Doi chieu hoa don sac dien va log sac tu cac tram/doi tac moi tuan, nhieu dong du lieu lap lai, de sai khi copy thu cong. |
| 4 | Vinhomes | AI-upgrade | Phan loai phan anh cu dan tren app Vinhomes Resident con cham va phan hoi rap khuon, dan den ticket bi chuyen sai bo phan. |
| 5 | Vinmec | Time-consuming | Bac si mat 20-30 phut de viet tom tat ho so xuat vien tu benh an, xet nghiem va ghi chu lam sang. |
| 6 | Vinpearl | Stakeholder Pain | Quan ly khach san phai doc thu cong review tren Booking/Agoda/Google Maps de phat hien phan nan khan cap ve phong, dich vu, nhan vien. |

Top 3 bai toan duoc chon de quick-assess:

1. Xanh SM - Xu ly su co pin thap/hut pin cua xe dien.
2. Vinhomes - Phan loai va route phan anh cu dan.
3. Vinmec - Soan thao tom tat ho so xuat vien.

---

## Phase 2 - QUICK-ASSESS

## Quick Problem Card #1 - Xanh SM xu ly su co pin thap cua xe dien

| Truong | Noi dung |
|---|---|
| Bai toan | Dieu phoi vien can xu ly nhanh truong hop tai xe Xanh SM bao pin thap, tim tram sac gan hoac dieu xe sac pin di dong neu pin nguy cap. |
| Cong ty thanh vien | Xanh SM / GSM |
| Actor dang dau | Tai xe xe dien, dieu phoi vien trung tam van hanh, khach hang dang cho chuyen xe. |
| Workflow thu cong hien tai | 1. Tai xe goi tong dai bao pin thap. -> 2. Dieu phoi vien tra GPS xe. -> 3. Mo dashboard tram sac VinFast de tim tram gan/con tru sac trong. -> 4. Soan tin nhan huong dan tai xe. -> 5. Neu pin qua thap, goi doi xe sac di dong/cuu ho. |
| Buoc ton thoi gian/loi nhat | Buoc 3-4, mat khoang 10-12 phut/luot; de sai khi chon tram xa hoac khong phu hop cong sac. |
| AI co the ho tro | LLM Feature nhan input pin, GPS, khoang cach tram; draft tin nhan [DRAFT_ONLY] va neu pin < 5% thi tra JSON dispatch_mobile_charger. |
| Success metric | Giam thoi gian xu ly su co tu 15 phut xuong duoi 3 phut; 98% de xuat dung rule an toan pin < 5%. |
| Quick Architecture | LLM Feature + rule guardrail + Human-in-the-loop. |

Danh gia nhanh:

- Gia tri cao vi anh huong truc tiep den an toan giao thong, trai nghiem tai xe va SLA don khach.
- Ranh gioi van hanh ro: AI chi draft, khong gui thang; pin < 5% khong de xuat tram xa hon 5km.
- Nen chon lam prototype vi co the test bang adversarial prompt ro rang.

---

## Quick Problem Card #2 - Vinhomes phan loai va route phan anh cu dan

| Truong | Noi dung |
|---|---|
| Bai toan | Phan anh cua cu dan ve nuoc, dien, thang may, ve sinh, an ninh bi phan loai cham hoac chuyen sai bo phan. |
| Cong ty thanh vien | Vinhomes |
| Actor dang dau | Nhan vien CSKH, ban quan ly toa nha, cu dan gui phan anh. |
| Workflow thu cong hien tai | 1. Cu dan gui ticket tren app. -> 2. CSKH doc noi dung. -> 3. Gan nhan loai van de. -> 4. Chuyen ticket cho bo phan phu trach. -> 5. Theo doi SLA va phan hoi cu dan. |
| Buoc ton thoi gian/loi nhat | Buoc 2-4, mat 6-10 phut/ticket; loi thuong gap la chuyen sai bo phan hoac danh gia sai muc do khan cap. |
| AI co the ho tro | LLM phan loai noi dung, trich dia diem/toa nha/can ho, de xuat muc uu tien va draft phan hoi ban dau. |
| Success metric | 85% ticket duoc phan loai duoi 10 giay; giam ty le route sai tu 12% xuong duoi 4%. |
| Quick Architecture | Rule + LLM Feature; cac ticket khan cap van can nhan vien duyet. |

Danh gia nhanh:

- Phu hop AI vi input la ngon ngu tu nhien va co nhieu bien the.
- Can can trong voi phan anh lien quan tranh chap phi, an ninh, phap ly; cac case nay phai escalation cho con nguoi.

---

## Quick Problem Card #3 - Vinmec soan thao tom tat ho so xuat vien

| Truong | Noi dung |
|---|---|
| Bai toan | Bac si mat nhieu thoi gian tong hop benh an, ket qua xet nghiem, chi dinh va loi dan de viet tom tat xuat vien cho benh nhan. |
| Cong ty thanh vien | Vinmec |
| Actor dang dau | Bac si dieu tri, dieu duong hanh chinh, benh nhan/care giver. |
| Workflow thu cong hien tai | 1. Bac si mo benh an dien tu. -> 2. Doc ghi chu dien bien dieu tri. -> 3. Copy ket qua xet nghiem/chuan doan. -> 4. Viet tom tat va loi dan. -> 5. Kiem tra, ky va in/tra cho benh nhan. |
| Buoc ton thoi gian/loi nhat | Buoc 2-4, mat 20-30 phut/benh nhan; de thieu thong tin quan trong neu bac si qua tai. |
| AI co the ho tro | LLM tao ban nhap tom tat co cau truc tu du lieu EMR da duoc phep truy cap, bac si phai duyet va sua truoc khi ban hanh. |
| Success metric | Giam thoi gian tao draft tu 25 phut xuong duoi 7 phut; 100% ban cuoi phai duoc bac si ky duyet. |
| Quick Architecture | LLM Feature co HITL bat buoc; khong cho AI tu dua chan doan moi. |

Danh gia nhanh:

- Gia tri cao nhung rui ro y te lon, can du lieu sach va quy trinh phe duyet chat.
- Phu hop giai doan sau hon, khi da co baseline va mau ho so chuan.

---

## Ket luan ca nhan

Bai toan nen chon cho prototype la **Xanh SM xu ly su co pin thap cua xe dien**. Ly do: quy trinh co dau vao ro rang, metric do duoc, ranh gioi an toan cu the, va co the stress-test bang prompt injection. Giai phap phu hop nhat la **LLM Feature + rule guardrail + Human-in-the-loop**, khong can agent tu tri trong giai doan dau.