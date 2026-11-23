class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda")

class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda tez yurmoqda")

class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped velosiped yo'lakchasida ketmoqda")

class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd temir yo'l bo'ylab harakatlanmoqda")

transportlar = [Mashina(), Velosiped(), Poyezd()]
for t in transportlar:
    t.harakatlanish()
