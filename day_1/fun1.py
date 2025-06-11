# funkcja - wydzielony fragment kodu, mozemy wykonać w dowolnym momencie
# funkcja musi zostać najpierw zadeklarowa
# ctrl /  - komentarz
# wywołanie funkcji uruchamia kod

a = 10
b = 34


# funkcje niezwracające wyniku
# ctrl alt l - formatowanie kodu
# deklaracja funkcji
# snake_case
def dodaj():  # funkcja bez argumentów
    print(a + b)  # korzysta z globalnych


def dodaj2(a, b):  # dwa obowiązkowe argumenty
    print(a + b)  # argumenty lokalne


# omijamy problem braku przeciązania  funkcji liczbą argumentów
def odejmij(a, b, c=0):
    print(a - b - c)


# uruchomienie funkcji
dodaj()  # 44
print(dodaj)  # <function dodaj at 0x000001DD23E83B00>
print(type(dodaj))  # <class 'function'>

# przekazywanie argumentów po pozycji
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(4, 89)  # 93

odejmij(1, 2)  # -1
odejmij(1, 2, 4)  # -5

odejmij(b=9, a=87)  # 78
dodaj2(b=9, a=87)  # 96

# mieszane
# argumenty pozycyjne przed nazwanymi
# odejmij(c=8, 1, 2) # SyntaxError: positional argument follows keyword argument
odejmij(1, 2, c=90)  # -91
odejmij(1, b=2, c=90)  # -91

print(dodaj())
# 44
# None - odpowiednik null, nie wiem, brak informacji
print(bool(None))  # False


# print(dodaj() + dodaj2(6, 8)) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# funkcje zwracające wynik
def mnozenie(a, b):
    return a * b  # zwraca wynik


print(mnozenie(5, 9))  # 45
wyn = mnozenie(7, 9)
print("Wynik:", wyn)  # Wynik: 63
print(f"Wynik: {wyn}")  # Wynik: 63, f-string
print(f"{a} + {b} = {a + b}")  # 10 + 34 = 44
print("Wynik: {}".format(wyn))  # Wynik: 63
print("Wynik: %s" % wyn)  # Wynik: 63
# lazy - wykonuje się gdy jest potrebny
# print("Wynik: " + wyn) # TypeError: can only concatenate str (not "int") to str
print(type("Wynik: "))
print(type(wyn))
# <class 'str'>
# <class 'int'>
# silne typowanie - nie zamienia typów podczas operacji
print("Wynik: " + str(wyn))  # str() - rzutowanie na str
print("1" + "3")  # 13, konkatenacja str
print("1" * 8)  # 11111111

print(35 * 168)
print(35 * "168")
# 5880
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

print(mnozenie(4, 6) + mnozenie(6, 2))  # 36


# to są  tylko podpowiedzi!!!
def mnozenie2(a: int, b: int) -> tuple[int, int, int]:
    return a, b, a * b  # zwraca wiele wartości


print(mnozenie2(2, "a"))  # (2, 'a', 'aa')
# mypy
# pip install mypy
# mypy .\fun1.py
# pip list
c = mnozenie2(6, 8)
print(c)  # (6, 8, 48)
print(type(c))  # <class 'tuple'>
# (6, 8, 48)
x, y, z = c  # rozpakowanie krotki
print(f"{x} +  {y} = {z}")
tup = 1, 2, 3
print(type(tup))
# a, b = tup  # ValueError: too many values to unpack (expected 2)
a, *b = tup  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]

tuppla_names = "Radek", "Tomek", "Zenek", "Danusia"
name1, name2, *name3 = tuppla_names
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Danusia']

name1, *name2, name3 = tuppla_names
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek'] Danusia

*name1, name2, name3 = tuppla_names
print(name1, name2, name3)  # ['Radek', 'Tomek'] Zenek Danusia
