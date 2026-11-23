class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Savat:
    def __init__(self, nom):
        self.nom = nom
        self.mahsulotlar = []

    def mahsulot_qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)

    def __str__(self):
        return f"Savat nomi: {self.nom}, Mahsulotlar soni: {len(self)}"

# Tekshirish
savat = Savat("Elektronika")
savat.mahsulot_qosh(Mahsulot("Telefon", 3000000))
savat.mahsulot_qosh(Mahsulot("Quloqchin", 200000))
savat.mahsulot_qosh(Mahsulot("Chexol", 50000))

print(savat)

if savat:
    print("Savat bo'sh emas!")
    print(f"Umumiy narx: {savat.umumiy_narx()} so'm")
else:
    print("Savat bo'sh.")
