# lambda - skrócony zapis funkcji
# lambda return
# funkcja anonimowa - możliwosc uzycia funkcji w miejscu deklaracji


def mnozenie(x, y):
    return x * y


print(mnozenie(6, 9))  # 54

mnozenie_lambda = lambda x, y: x * y
print(mnozenie_lambda(8, 4))  # 32


