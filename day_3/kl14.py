# hermetyzacja - ukrycie zmiennych wewnątrz kalsy, widoczność tylko w kalsie
# enkapsulacja -  hermetyzacja pol i wystawienie metod do odczytu i zmiany wartości tych pol (getter, setter)
class Dom:
    def __init__(self, kolor, metraz):
        # pola prywatne
        self.__metraz = metraz
        self.__kolor = kolor

    def wypisz_metraz(self):
        print(f"Mam powierznię {self.__metraz} m2")

    def zmien_matraz(self):
        odp = int(input("Podaj nowy metraz (m2)"))
        self.__metraz = odp
        self.wypisz_metraz()


dom = Dom("zielony", 234)
dom.wypisz_metraz()  # Mam powierznię 234 m2
dom.zmien_matraz()
# Mam powierznię 234 m2
# Podaj nowy metraz (m2)456
# Mam powierznię 456 m2
# pole prywatne
# print(dom.__metraz) # AttributeError: 'Dom' object has no attribute '__metraz'
dom.__metraz = 789  # dodałeś globalną zmienna do obiektu Dom o tej samej nazwie
dom.wypisz_metraz()  # Mam powierznię 566 m2
print(dom.__metraz)  # 789
