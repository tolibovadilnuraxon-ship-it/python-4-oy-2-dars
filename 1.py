class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print(f"{self.nomi} ovoz chiqarmoqda.")


class It(Hayvon):
    def qoriqlash(self):
        print(f"{self.nomi} uyni qo‘riqlamoqda.")


class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print(f"{self.nomi} sichqon tutmoqda.")


i1 = It("Pantera", 3)
m1 = Mushuk("Momiq", 2)


print("--- It haqida ---")
i1.ovoz()
i1.qoriqlash()

print("\n--- Mushuk haqida ---")
m1.ovoz()
m1.sichqon_tutish()
