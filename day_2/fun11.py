generator_x = [x for x in range(5)]
print(generator_x)  # [0, 1, 2, 3, 4]
print(type(generator_x))  # <class 'list'>

generator_2 = (x for x in range(5))
print(generator_2)  # <generator object <genexpr> at 0x0000015FE4776080>
print(type(generator_2))  # <class 'generator'>
print(next(generator_2))  # 0
print(next(generator_2))  # 1
print(next(generator_2))  # 2
print(next(generator_2))  # 3


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))  # 1
print(next(g3))  # 2
print(next(g3))  # 3
print(next(g3))  # 4


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == "stop":
            break


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
g5.send("OK")
try:
    g5.send("stop")
except Exception as e:
    print("Koniec", e)


# stop
# Koniec


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib2 = fibo_with_index(10)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))  # (3, 2)
for i, n in fibo_with_index(10):
    print(f"Pozycja: {i}, element: {n}")
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3
# Pozycja: 5, element: 5
# Pozycja: 6, element: 8
# Pozycja: 7, element: 13
# Pozycja: 8, element: 21
# Pozycja: 9, element: 34
