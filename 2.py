class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        return f"Ism: {self.ism}, Maosh: {self.maosh}"

class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        return f"{super().malumot()}, Fan: {self.fan}"

class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        return f"{super().malumot()}, Qavat: {self.qavat}"

oqituvchi = Oqituvchi("Anvar", 5000000, "Matematika")
farrosh = Farrosh("Dilbar", 3000000, 2)

print(oqituvchi.malumot())
print(farrosh.malumot())
