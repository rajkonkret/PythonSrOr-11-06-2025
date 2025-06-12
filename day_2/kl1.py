# klasa - element programowania obiektowego
# szablon, przepis
#  obiekt - zbudowany wg przepisu
# paradygmaty programowania obiektowego
# hermetyzacja, polimorfizm, dziedziczenie, abstrakcja
# pola - zmienne
# metody - funkcje
# tworzenie obiektu uruchamia metodę inicjalizujacą (konstruktor)
import math


# PascalCase
class MyFirstClass:
    """
    Klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        self - obiekt, który wywołał metode
        :param x:
        :param y:
        """
        # self.x = x
        # # ob.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        Metoda przemiesczza punkt w miejsce wskazane x,y
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        Obliczanie odległści pomiędzy dwoma punktami
        using the Pythagorean theorem:  sqrt(x*x + y*y)
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x, self.y}"

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x00000277AE9B6F90>
# print(MyFirstClass.__doc__)  # wypisze dokumentację
# print(print.__doc__)
# pydoc -b serwer dokumentacji
# pydoc -w .\kl1.py plik html z dokumentacją
print(ob.x)
print(ob.y)
# po nadpisaniu metody __str__ obiekt wyświetla się tak
# (0, 0)
ob.move(567, 908)
print(ob)  # (567, 908)

ob2 = MyFirstClass(100, 789)
print(ob2)  # (100, 789)
ob2.reset()
print(ob2)  # (0, 0)

print(ob.calculate(ob2))  # 1070.4919429869615
print(ob2.calculate(ob))  # 1070.4919429869615

lista = [ob, ob2]
print(lista)
# [<__main__.MyFirstClass object at 0x0000027D5D046F90>,
# <__main__.MyFirstClass object at 0x0000027D5D314E10>] __repr__
# po nadpisaniu __repr__ lisat zostanie wyświetlona
# [MyFirstClass ((567, 908), MyFirstClass ((0, 0)]

print(ob)  # (567, 908) __str__
print(str(ob))  # (567, 908)
