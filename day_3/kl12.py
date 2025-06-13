class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("X must be integer")
    if not isinstance(y, int):
        raise MyTypeError("Y must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


while True:
    try:
        a = input("Podaj pierwszą liczbę")
        b = input('Podaj drugą liczbę')
        if a == "q" or b == "q":
            break
        result = my_function(int(a), int(b))
    except MyTypeError:
        print("MyTypeError")
    except MyValueError as e:
        print("MyValueError", e)
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Wynik wynosi:", result)
    finally:
        print("Koniec")

# Podaj pierwszą liczbę0.9
# Podaj drugą liczbę1
# Bład invalid literal for int() with base 10: '0.9'
# Koniec
# Podaj pierwszą liczbę1
# Podaj drugą liczbę2
# Wynik wynosi: 0.5
# Koniec
# Podaj pierwszą liczbę1
# Podaj drugą liczbę0
# MyValueError y cannot be zero
# Koniec
# Podaj pierwszą liczbę
