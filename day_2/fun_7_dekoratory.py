# dekorator - przyjmuje inną funkcję jako argument
# dodaje, modyfikuje funkcje
# wykorzystuje zasady funkcji wewnętrznej
def dekor(func):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return func()

    return wew


@dekor  # użycie dekoratora na funkcji
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja()
# Dekorator. Dodatkowy napis
# Funkcja, którą chcemy udekorować
