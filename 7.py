class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        return f"{self.brend} {self.model} — {self.narx:,} so'm".replace(',', ' ')

    def __eq__(self, other):
        return self.narx == other.narx

tel1 = Telefon("Samsung", "A54", 4500000)
tel2 = Telefon("Redmi", "Note 12", 2500000)
print(tel1)
print(tel2)
