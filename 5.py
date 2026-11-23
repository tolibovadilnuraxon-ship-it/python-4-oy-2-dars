class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        return f"Kitob: {self.nom}, Muallif: {self.muallif}, Sahifa: {self.sahifa_soni}"

class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        bazaviy = super().malumot()
        return f"{bazaviy}, Format: {self.format}, Hajmi: {self.fayl_hajmi}"

e_kitob = ElektronKitob("Python asoslari", "Anvar Narzullayev", 350, "PDF", "15 MB")
print(e_kitob.malumot())
