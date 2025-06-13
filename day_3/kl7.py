from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # metoda abstrakcyjna
    def drukuj(self):
        pass

    @staticmethod
    def from_string():
        print("Metoda statyczna")

    @classmethod
    def from_counter(cls, counter: "Counter"):  # dodatkowy konstruktor, (symuluje przeciążanie)
        # Counter(counter.values)
        return cls(counter.values)  # zwraca obiekt klasy


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            # rzucam wyjątek
            raise ValueError(f"Wartość nie może być większa niż: {self.MAX}")
        super().__init__(values)  # obowiązkowe

    def drukuj(self):
        print("Drukuje", self.values)


class NewCounter(Counter):
    """
    Klasa dziedziczy po klasie Counter
    """


class CounterPoli(Counter):
    """
    dziedziczy po Counter
    """

    def drukuj(self):
        print("Drukuje:", self.values)


# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()
# c1.increment()
# print(c1.values)  # 1
# c1.drukuj()

bc = BoundedCounter(30)
bc.drukuj()  # Drukuje 30

# nie da sięs tworzyć obiektu takiej klasy
# TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
# nc = NewCounter()

pc = CounterPoli(34)
pc.drukuj()  # Drukuje: 34

# polimorfizm - obiekty róznych klas w pewnym zakresie mogą być traktowane jako obiekt jedej klasy(nadrzędnej)
# klasa abstrakcyjna zapewnia polimorfizm na metodzie drukuj()
lista = [bc, pc]  # obiekty róznych klas
for i in lista:
    i.drukuj()
# Drukuje 30
# Drukuje: 34

# metoda statyczna
# nie ma potrzeby tworzenia obiektu tej klasy
Counter.from_string()

# wykorzystanie classmethod jako konstruktor obiektu
bc2 = BoundedCounter.from_counter(bc)
bc2.drukuj()  # Drukuje 30

bc3 = BoundedCounter(bc.values)
bc3.drukuj()  # Drukuje 30
