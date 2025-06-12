# generator - generuje wartość w momencie kiedy jej potrzebuje

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wartosć obliczenia, zatrzymuje się i zapamiętuje na której skończyło


kwa = kwadrat2(5)  # inicjalizacja generatora
print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print("Zrób cokolwiek")
print("Radek")
x = 90
print(x)
print(next(kwa))  # 9
print(next(kwa))
# print(next(kwa))  # StopIteration- generator zakończył działanie

kwa2 = kwadrat2(10)
for k in kwa2:
    print(k)
# 0
# 1
# 4
# 9
# 16

kwa3 = kwadrat2(10)
kwa4 = kwadrat2(10)

print(next(kwa3))  # 0
print(next(kwa4))  # 0
print(next(kwa3))  # 1
print(next(kwa4))  # 1

print(list(kwa4))  # [4, 9, 16, 25, 36, 49, 64, 81]
