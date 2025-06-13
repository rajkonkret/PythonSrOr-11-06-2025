# dziedziczenie po wielu klasach
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


a = A()
a.method()

b = B()
b.method()


# Metoda z klasy A
# Metoda z klasy B


class C(B, A):
    """
    Klasa dziedziczy po kalsie B i A
    """


c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po D i A
    """


d = D()
d.method()  # Metoda z klasy A
print(D.__mro__)


# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    def method(self):
        B.method(self)  # jawnie wskazujemy klasę B


f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # super() - możemy wywołać metodę z klasy nadrzędnej, tutaj A


g = G()
g.method()  # Metoda z klasy A


class X(A, B):
    def method(self):
        super().method()
        print("Dopisane w klasie X")
        B.method(self)


x = X()
x.method()
