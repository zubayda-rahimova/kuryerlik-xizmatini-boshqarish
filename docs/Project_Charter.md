# Project Charter — Kuryerlik xizmatini boshqarish tizimi

**Talaba:** RAXIMOVA ZUBAYDA ULUG‘BEK QIZI  
**Guruh:** 232-KIDT_Masofaviy  
**Mavzu:** Kuryerlik xizmatini boshqarish tizimi

## 1. Loyiha nomi va muammosi
Loyiha kuryerlik xizmatida buyurtmalarni qabul qilish, jo‘natmalarni ro‘yxatga olish,
kuryerlarni biriktirish va yetkazib berish holatini kuzatishni yagona tizimda tashkil
etishga qaratilgan. Ma’lumotlar qo‘lda yoki turli joylarda yuritilsa, buyurtma holatini
tekshirish va ma’lumotlarni yangilash qiyinlashishi mumkin. Tizim administrator,
dispetcher, kuryer va buyurtma holatini kuzatuvchi mijozlar uchun mo‘ljallangan.

## 2. Maqsad
Buyurtmalar, kuryerlar, jo‘natmalar, manzillar va yetkazib berish holatlarini boshqarish
imkonini beruvchi qulay dasturiy tizimni ishlab chiqish.

## 3. Vazifalar
1. Buyurtmalarni yaratish, ko‘rish va yangilash imkoniyatini ishlab chiqish.
2. Kuryerlar haqidagi ma’lumotlarni ro‘yxatga olish va boshqarish.
3. Jo‘natma va yetkazib berish manzili ma’lumotlarini saqlash.
4. Buyurtmalarni kuryerlarga biriktirish jarayonini tashkil etish.
5. Yetkazib berish holatlarini yangilash va kuzatish.
6. Buyurtmalarni identifikatori, manzili yoki holati bo‘yicha qidirish.
7. Ma’lumotlarning to‘g‘riligini tekshirish va foydalanuvchi rollarini ajratish.

## 4. Manfaatdor tomonlar
- **Administrator:** foydalanuvchilar va tizim ma’lumotlarini boshqaradi.
- **Dispetcher/operator:** buyurtmalarni ro‘yxatga oladi va kuryerlarga taqsimlaydi.
- **Kuryer:** biriktirilgan buyurtmalarni ko‘radi va holatini yangilaydi.
- **Mijoz:** buyurtma holatini kuzatadi.
- **Xizmat rahbari/buyurtmachi:** xizmat natijalarini nazorat qiladi.
- **Loyiha ishlab chiquvchisi:** tizimni loyihalaydi, ishlab chiqadi va sinaydi.

## 5. Loyiha chegaralari (Scope)
### Loyihaga kiradi
- Buyurtmalarni ro‘yxatga olish, ko‘rish va tahrirlash.
- Kuryerlar ma’lumotlarini boshqarish.
- Jo‘natma va manzillarni saqlash.
- Buyurtmani kuryerga biriktirish.
- Yetkazib berish holatini yangilash va ko‘rish.
- Buyurtmalarni qidirish va oddiy hisobot ko‘rinishi.
- Asosiy foydalanuvchi rollari va ruxsatlarini belgilash.

### Loyihaga kirmaydi
- Bank yoki to‘lov tizimlari orqali haqiqiy to‘lovlarni qayta ishlash.
- Keng qamrovli GPS real vaqt kuzatuvi va avtomatik yo‘nalish optimallashtirish.
- Alohida mobil ilova ishlab chiqish.
- Buxgalteriya va ish haqini to‘liq boshqarish.
- Katta yuklama uchun korporativ infratuzilmani joriy etish.

## 6. Muvaffaqiyat mezonlari
- Buyurtma, kuryer, jo‘natma va manzil ma’lumotlari tizimda saqlanadi.
- Dispetcher buyurtmani kuryerga biriktira oladi.
- Kuryer yetkazib berish holatini yangilay oladi.
- Foydalanuvchi buyurtmani qidirib, holatini ko‘ra oladi.
- Asosiy funksiyalar sinovdan o‘tkaziladi.

## 7. GitHub repository tuzilishi
```text
kuryerlik-xizmatini-boshqarish/
├── README.md
├── .gitignore
├── docs/
│   └── Project_Charter.md
├── src/
└── tests/
```

## 8. Dastlabki taxmin va cheklovlar
Loyiha o‘quv maqsadida yaratiladi. Texnologiyalar keyingi bosqichda tanlanadi.
GPS, to‘lov integratsiyasi va alohida mobil ilova birinchi versiyaga kiritilmaydi.
