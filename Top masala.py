##1-masala
# class Talabalar:
#     def __init__(self, nomi,yoshi, kursi):
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self.kursi = kursi
# Ali = Talabalar("Ali"," - 20 yosh","2-kurs")
# Vali = Talabalar("Vali","- 21 yosh","4-kurs")
# Hasan = Talabalar("Hasan","- 19 yosh","1-kurs")
# Husan = Talabalar("Husan","- 22 yosh","4-kurs")
# Olim = Talabalar("Olima","- 20 yosh","2-kurs")
#
# print("---Talabalar ro'yxati---")
# print(f"{Ali.nomi}{Ali.yoshi},{Ali.kursi}")
# print(f"{Vali.nomi}{Vali.yoshi},{Vali.kursi}")
# print(f"{Hasan.nomi}{Hasan.yoshi},{Hasan.kursi}")
# print(f"{Husan.nomi}{Husan.yoshi},{Husan.kursi}")
# print(f"{Olim.nomi}{Olim.yoshi},{Olim.kursi}")

##2-masala
# class Kitob:
#     def __init__(self, nomi, muallifi, narxi):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narxi = narxi
#
# print("=== KITOBLAR RO'YHATI===")
# a = Kitob("Python dasturlash","Xusnidddin","- 50000 so'm")
# b = Kitob("Algoritmlar","Hikmatjon","- 75000 so'm")
# c = Kitob("Ma'lumotlar strukturasi","Hasan","- 60000 so'm")
# d = Kitob("Web dasturlash","Husan","- 80000 so'm")
# e = Kitob("Ma'shuniyat","Akbar","- 45000 so'm")
#
# print(f"{a.nomi} {a.muallifi} {a.narxi}")
# print(f"{b.nomi} {b.muallifi} {b.narxi}")
# print(f"{c.nomi} {c.muallifi} {c.narxi}")
# print(f"{d.nomi} {d.muallifi} {d.narxi}")
# print(f"{e.nomi} {e.muallifi} {e.narxi}")
#
#
# print("=== Eng qimmat kitob ==="
# print(f"Kitob nomi: {d.nomi}")
# print(f"Kitob muallifi: {d.muallifi}")
# print(f"Kitob narxi: {d.narxi}")



# 3 - masla
# class Telefon:
#     def __init__(self, model, narx, rang):
#         self.model = model
#         self.narx = narx
#         self.rang = rang
#
#     def info(self):
#         print(f"{self.model} | Rang: {self.rang} | Narx: {self.narx} so'm")
#
# # 5 ta telefon yaratamiz
# t1 = Telefon("iPhone 14", 12000000, "Qora")
# t2 = Telefon("Samsung S23", 11500000, "Oq")
# t3 = Telefon("Xiaomi 13", 9000000, "Ko‘k")
# t4 = Telefon("Huawei P50", 8500000, "Qizil")
# t5 = Telefon("Oppo A96", 4500000, "Yashil")
#
# telefonlar = [t1, t2, t3, t4, t5]
# print("=== TELEFONLAR RO‘YXATI ===")
# jami = 0
# for tel in telefonlar:
#     tel.info()
#     jami += tel.narx
# print(f"\nJami narx: {jami} so'm")




# 4 - masala
# class Meva:
#     def __init__(self, nomi, vazni, narxi):
#         self.nomi = nomi
#         self.vazni = vazni
#         self.narxi = narxi
#
#     def info(self):
#         print(f"{self.nomi} | Vazni: {self.vazni} kg | Narxi: {self.narxi} so'm")
# # 5 ta meva yaratamiz
# m1 = Meva("Olma", 1, 15000)
# m2 = Meva("Banan", 1.5, 25000)
# m3 = Meva("Uzum", 2, 18000)
# m4 = Meva("Anor", 1, 30000)
# m5 = Meva("Nok", 1, 14000)
#
# mevalar = [m1, m2, m3, m4, m5]
#
# print("=== MEVALAR RO‘YXATI ===")
# for m in mevalar:
#     m.info()
#
# eng_arzon = mevalar[0]
# for m in mevalar:
#     if m.narxi < eng_arzon.narxi:
#         eng_arzon = m
#
# print("\n=== ENG ARZON MEVA ===")
# eng_arzon.info()




## 5 - masala
# class Sportchi:
#     def __init__(self, ism, yosh, sport_turi):
#         self.ism = ism
#         self.yosh = yosh
#         self.sport_turi = sport_turi
#
#     def info(self):
#         print(f"{self.ism} | Yosh: {self.yosh} | Sport: {self.sport_turi}")
#
#
# s1 = Sportchi("Ali", 22, "Futbol")
# s2 = Sportchi("Vali", 19, "Basketbol")
# s3 = Sportchi("Hasan", 25, "Tennis")
# s4 = Sportchi("Husan", 20, "Suzish")
# s5 = Sportchi("Olim", 18, "Voleybol")
#
# # Ro‘yxatga yig‘amiz
# sportchilar = [s1, s2, s3, s4, s5]
#
# print("=== SPORTCHILAR RO‘YXATI ===")
# for s in sportchilar:
#     s.info()
# # Eng yosh sportchini topamiz
# eng_yosh = sportchilar[0]
# for s in sportchilar:
#     if s.yosh < eng_yosh.yosh:
#         eng_yosh = s
#
# print("\n=== ENG YOSH SPORTCHI ===")
# eng_yosh.info()