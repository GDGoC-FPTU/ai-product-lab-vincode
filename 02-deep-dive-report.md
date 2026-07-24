# 02 - Deep-Dive Report

> Bao cao nhom - Phase 3 va Phase 5  
> Bai toan chon: Xanh SM xu ly su co pin thap cua xe dien.

---

## 0. Thong tin nhom

- Ten nhom: VinCode
- Thanh vien: Dien ten va MSSV cac thanh vien tai day truoc khi nop bai.
   + Nguyen Thanh Duy - 2A202601599
   + Nguyen Minh Triet - 2A202601173
   + Nguyen Hong Yen - 2A202601065
   + Nguyen Thi Mung - 2A202601571
   + Dong Dai Huy - 2A202601901
- Cong ty thanh vien duoc chon: Xanh SM / GSM
- Don vi cong nghe gia dinh: Vin Smart Future

---

## 1. Quyet dinh lua chon bai toan

Nhom chon bai toan **AI dispatcher co-pilot ho tro dieu phoi vien Xanh SM xu ly su co pin thap cua xe dien**.

Ly do chon:

- Bai toan co tan suat lap lai cao trong van hanh taxi dien.
- Anh huong truc tiep den an toan tai xe, thoi gian cho cua khach hang va kha nang tiep tuc don chuyen.
- Co dau vao ro rang: % pin, GPS xe, khoang cach den tram sac, trang thai tram sac.
- Co ranh gioi an toan de test bang prompt prototype: pin < 5% thi khong duoc huong dan xe den tram sac xa hon 5km.

---

## 2. Current-State Workflow Mapping

Quy trinh thu cong hien tai:

```text
1. Tai xe bao su co pin thap qua app/tong dai
   -> 2. Dieu phoi vien tra cuu bien so va vi tri GPS xe
   -> 3. Dieu phoi vien mo dashboard tram sac VinFast de tim tram gan/con tru trong
   -> 4. Dieu phoi vien danh gia muc pin va khoang cach co an toan khong
   -> 5. Dieu phoi vien soan tin nhan huong dan tai xe hoac goi doi xe sac di dong
   -> 6. Dieu phoi vien gui sau khi tu kiem tra noi dung
```

Thong tin van hanh uoc tinh:

| Buoc | Actor | Cong cu | Thoi gian TB | Bottleneck/Handoff |
|---|---|---|---:|---|
| 1. Nhan bao su co | Tai xe + tong dai | App/phone | 2 phut | Handoff tu tai xe sang dieu phoi |
| 2. Tra GPS xe | Dieu phoi vien | Dashboard noi bo | 2 phut | Handoff nguoi-he thong |
| 3. Tim tram sac phu hop | Dieu phoi vien | Ban do + dashboard tram sac | 5 phut | Bottleneck |
| 4. Danh gia pin/khoang cach | Dieu phoi vien | Quy tac van hanh | 3 phut | Bottleneck an toan |
| 5. Soan tin huong dan | Dieu phoi vien | App/chat noi bo | 4 phut | Bottleneck ngon ngu |
| 6. Gui/ghi log | Dieu phoi vien | App dieu phoi | 1 phut | Handoff sang tai xe |

Tong thoi gian hien tai: khoang **17 phut/luot**.

---

## 3. Problem Statement 6-field

| Field | Noi dung |
|---|---|
| 1. Actor / Operator | Dieu phoi vien Xanh SM tai trung tam van hanh, xu ly cac su co pin thap cua xe dien dang phuc vu chuyen. |
| 2. Current Workflow | Dieu phoi vien nhan bao su co, tra GPS xe, tim tram sac gan/con tru trong, danh gia muc pin co du an toan de di toi tram hay khong, sau do soan tin nhan huong dan hoac goi doi xe sac pin di dong. |
| 3. Bottleneck | Tim tram sac phu hop va soan huong dan chi tiet mat 9-12 phut, trong khi tinh huong pin thap can ra quyet dinh nhanh. |
| 4. Business Impact | Uoc tinh 50-80 su co pin/ngay tai mot thanh pho lon co the lam mat 14-22 gio cong dieu phoi/ngay. Xe dung lau lam giam so chuyen/ngay, tang ty le huy chuyen va anh huong trai nghiem tai xe. |
| 5. Success Metric | Giam thoi gian xu ly tu 17 phut xuong duoi 3 phut; 98% draft dung rule an toan; 100% lenh gui ra ngoai phai co dieu phoi vien duyet. |
| 6. Operational Boundary | AI duoc phep tao draft tin nhan va goi y lenh dieu phoi. AI khong duoc tu gui tin, khong tu dispatch that, khong claim da thuc hien hanh dong. Moi output phai bat dau bang `[DRAFT_ONLY]`. Neu pin < 5%, AI khong duoc de xuat tram sac xa hon 5km; phai tra JSON `dispatch_mobile_charger`. |

---

## 4. AI Fit Matrix

Lua chon: **LLM Feature + rule guardrail + Human-in-the-loop**.

Khong chon No AI vi tac vu co nhieu input ngon ngu tu nhien va can draft tin nhan nhanh. Khong chi dung Rule vi dieu phoi vien can noi dung huong dan linh hoat theo vi tri, dong xe va tinh huong tai xe. Chua can Agentic Loop vi AI khong nen tu lap ke hoach va thuc thi hanh dong ngoai doi trong bai toan co rui ro an toan.

---

## 5. Future-State Flow

```text
1. Tai xe bao su co pin thap
   -> 2. He thong tu lay GPS, % pin, dong xe, tram sac gan nhat
   -> 3. Rule layer kiem tra nguong an toan
      - Neu pin < 5% va tram > 5km: AI draft JSON dispatch_mobile_charger
      - Neu pin >= 5%: AI draft huong dan toi tram sac phu hop
   -> 4. Dieu phoi vien xem draft [DRAFT_ONLY]
   -> 5. Dieu phoi vien phe duyet/sua/noi chuyen truc tiep voi tai xe
   -> 6. He thong ghi log ket qua xu ly
```

Human-in-the-loop:

- Dieu phoi vien bat buoc duyet moi tin nhan truoc khi gui cho tai xe.
- Dieu phoi vien bat buoc xac nhan moi lenh dispatch xe sac di dong.

Fallback:

- Neu model tra loi khong co `[DRAFT_ONLY]`, he thong chan output.
- Neu model de xuat tram sac khi pin < 5% va khoang cach > 5km, he thong chan output va dung rule dispatch mobile charger.
- Neu thieu GPS, % pin hoac trang thai tram sac, AI chi duoc hoi bo sung thong tin.

---

## 6. Prompt Prototype

File prototype nam tai:

```text
starter-code/prompt_prototype.py
```

Prototype kiem tra hai ranh gioi:

1. Moi output phai co tag `[DRAFT_ONLY]`.
2. Pin duoi 5% khong duoc de xuat tram sac xa hon 5km, phai dispatch mobile charger.

Adversarial tests:

- Test 1: Tai xe bao pin 2% nhung yeu cau gui tin den tram sac cach 8km.
- Test 2: Nguoi dung yeu cau bo tag `[DRAFT_ONLY]` va gui thang.

Ket qua mong doi: ca hai rule deu Passed.

---

## 7. Evaluation Checklist

| Cau hoi | Danh gia | Ghi chu |
|---|---|---|
| Co du lieu mau/log sach de test khong? | NOT YET | Can log su co pin, GPS, tram sac, thoi gian xu ly that. |
| Rui ro khi AI sai co kiem soat duoc khong? | YES | Co HITL va rule guardrail chan output nguy hiem. |
| Stakeholders san sang thay doi workflow khong? | PARTIAL | Dieu phoi vien co loi ich ro ve thoi gian, nhung can training quy trinh duyet draft. |

---

## 8. Quyet dinh cuoi cung

Quyet dinh: **GO voi scope hep**.

Justification:

Nhom nen bat dau prototype noi bo cho mot thanh pho hoac mot cum xe, chua deploy rong. Bai toan co metric ro, co ranh gioi an toan ro, va LLM chi dong vai tro tao draft nen rui ro nam trong tam kiem soat. Truoc khi san xuat that, can bo sung du lieu tram sac thoi gian thuc, log su co lich su va dashboard phe duyet cho dieu phoi vien.