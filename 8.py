class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        self.filmlar = filmlar if filmlar is not None else []

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film):
        return film in self.filmlar

kutubxona = FilmKutubxonasi("Sevimli filmlar", ["Avatar", "Titanik", "Gladiator"])
print("Filmlar soni:", len(kutubxona))
print("2-indeksdagi film:", kutubxona[2])
print("Titanik bormi?", "Titanik" in kutubxona)
