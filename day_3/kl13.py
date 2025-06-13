from functools import total_ordering

print(1 + 2)


class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)
# print(num1 < num2)
# TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)


@total_ordering  # automatycznie generuje pozostałe porównania
class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        print("porownanie")
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(5)
num4 = MyNumber2(10)
print(num3 < num4)  # True
print(num3 > num4)  # False
num5 = MyNumber2(10)
print(num4 == num5)  # False
# po dodaniu total_ordering
print(num4 == num5)  # True

print(id(num4))  # 2414565019472
print(id(num5))  # 2414565019792

print(num3 < num2)  # True
print(num2 < num3)  # False
# porownanie
# True
# porownanie
# False
