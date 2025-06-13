class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()  # dzieli po spacji
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)
# Jan Kowalski
name = "Jan Kowalski"
osoba2 = Osoba.z_nazwy_pelnej(name)
print(osoba2.imie)
print(osoba2.nazwisko)

imie, nazwisko = name.split()
osoba3 = Osoba(imie, nazwisko)
print(f"{osoba3.imie}, {osoba3.nazwisko}")  # Jan, Kowalski
