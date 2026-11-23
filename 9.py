class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        return f"{self.egasi} (**** {self.raqam_oxiri}) — Balans: {self.balans} so'm"

    def __gt__(self, other):
        return self.balans > other.balans

    def __lt__(self, other):
        return self.balans < other.balans

karta1 = Karta("Alisher", "1234", 1500000)
karta2 = Karta("Malika", "5678", 2300000)

print(karta1)
print(karta2)

if karta2 > karta1:
    print(f"{karta2.egasi}da mablag' ko'proq.")
else:
    print(f"{karta1.egasi}da mablag' ko'proq.")
