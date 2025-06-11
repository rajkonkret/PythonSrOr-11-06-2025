# funkcja zagnieżdzona, wewnętrzna
# dekorator - funkcja, która jako argument przyjmuje inną funkcję
# dekorator wykorzystuje idee funkcji wewnętrznej

def fun1():
    print("To jest fun1")

    def fun2():
        print("to jest fun2")

    return fun2  # zwróci adres funkcji


xFun = fun1()  # To jest fun1
print(type(xFun))
print(xFun)
# <class 'function'>
# <function fun1.<locals>.fun2 at 0x000002126AD63B00>
xFun()  # to jest fun2


# zrobic funkcje plik
# zapis odczyt
# w zaleznosci od parametru ma zwrócic jedną lub drugą
def plik(arg):
    print("Sprawdzam czy plik istnieje")

    def zapis():
        print("Zapisałem do pliku")

    def odczyt():
        print("Odczytałem z pliku")

    if arg == "zapis":
        return zapis
    else:
        return odczyt


zapis_pliku = plik("zapis")
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()

odczyt_plik = plik("odczyt")
odczyt_plik()
odczyt_plik()
odczyt_plik()
odczyt_plik()
odczyt_plik()
# Sprawdzam czy plik istnieje
# Zapisałem do pliku
# Zapisałem do pliku
# Zapisałem do pliku
# Zapisałem do pliku
# Sprawdzam czy plik istnieje
# Odczytałem z pliku
# Odczytałem z pliku
# Odczytałem z pliku
# Odczytałem z pliku
# Odczytałem z pliku

fh = open('text.txt', "w")
fh.write("Test\n")
fh.close()
