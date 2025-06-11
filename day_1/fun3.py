# lambda - skrócony zapis funkcji
# lambda return
# funkcja anonimowa - możliwosc uzycia funkcji w miejscu deklaracji
import math
from collections import Counter
from functools import reduce, lru_cache


def mnozenie(x, y):
    return x * y


print(mnozenie(6, 9))  # 54

mnozenie_lambda = lambda x, y: x * y
print(mnozenie_lambda(8, 4))  # 32

lata = [(2000, 29.7), (2001, 33.12), (2020, 32.92)]
print(max(lata))  # (2020, 32.92)
print(min(lata))  # (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # indeksujemy od zera, (2001, 33.12)
lata.sort(key=lambda c: c[1])
print(lata)  # [(2000, 29.7), (2020, 32.92), (2001, 33.12)]
print(max(lata))  # (2020, 32.92)

print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

lista = [1, 2, 3, 4, 5]
lista_wyn = []

for i in lista:
    lista_wyn.append(i * 4)
print(lista_wyn)  # [4, 8, 12, 16, 20]


def zmien_dane(x):
    return x ** 4


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien_dane(i))
print(lista_wyn_2)

# list comprehensions
print([i ** 4 for i in lista])  # [1, 16, 81, 256, 625]

# map() - funkcja wyzszego rzędu, jako argument przyjmuje inną funkcję
print(f"Zastosowanie map(): {list(map(zmien_dane, lista))}")
# Zastosowanie map(): [1, 16, 81, 256, 625]
# zastosowanie lambdy jako funkcja naonimowa
print(f"Zastosowanie map(): {list(map(lambda x: x ** 4, lista))}")
# Zastosowanie map(): [1, 16, 81, 256, 625]

# filter() zwraca elementy spełniające warunek
print(lista)
print(f"Filtrowanie: {list(filter(lambda x: x > 3, lista))}")  # Filtrowanie: [4, 5]
for i in lista:
    if i > 3:
        print(i, end=",")  # 4,5,

r0 = {'miasto': "Toruń"}
r1 = {'miasto': "Toruń", "ZIP": "25-900"}

print(r0['miasto'])  # Toruń
print(r1['miasto'])  # Toruń

print(r1['ZIP'])  # 25-900
# print(r0['ZIP'])  # KeyError: 'ZIP'

print(r0.get("ZIP"))  # None
print(r0.get("ZIP", "default"))  # default

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
print(r0)  # {'miasto': 'Toruń', 'ZIP': '00-000'}
print(r1)  # {'miasto': 'Toruń', 'ZIP': '25-900'}

#  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#     calculates ((((1 + 2) + 3) + 4) + 5).
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)
print("Wynik:", wynik)  # Wynik: 15
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15

wynik = reduce(lambda a, b: a * b, liczby)
print(wynik)  # 120

dane = ["a", "b", "a", "c", "a", "b", "b", "b", "c", "a"]

licznik = Counter(dane)
print(licznik)  # Counter({'a': 4, 'b': 4, 'c': 2})
wyn = reduce(lambda a, b: a if licznik[a] >= licznik[b] else b, licznik)
print(wyn)  # a

listy = [[1, 2], [3, 4], [5], [6, 7]]
flatten = reduce(lambda a, b: a + b, listy)
print(flatten)  # [1, 2, 3, 4, 5, 6, 7]
lista1 = [1, 2]
lista2 = [3, 4]
print(lista1 + lista2)  # [1, 2, 3, 4]

liczby = [2, 4, 4, 4, 5, 5, 7, 9]
suma, suma_danych, n = reduce(
    lambda acc, x: (acc[0] + x, acc[1] + x ** 2, acc[2] + 1),
    liczby,
    (0, 0, 0)
)

avg = suma / n
wariancja = (suma_danych / n) - (avg ** 2)
odchylenie = math.sqrt(wariancja)
print(f"Średnia: {avg:.2f}, Odchylenie std: {odchylenie:.2f}")


# Średnia: 5.00, Odchylenie std: 2.00
@lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # 5
print(fibonacci.cache_info())  # CacheInfo(hits=3, misses=6, maxsize=1000, currsize=6)
print(fibonacci(10))  # 55
print(fibonacci.cache_info())  # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
print(fibonacci(10))  # 55
print(fibonacci.cache_info())  # CacheInfo(hits=10, misses=11, maxsize=1000, currsize=11)
# hits - ile razy wyciągnąl z cache
# misses - ile razy wykonał dodatkowe obliczenia
fibonacci.cache_clear()
print(fibonacci.cache_info())  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)
