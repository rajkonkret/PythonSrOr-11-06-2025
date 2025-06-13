# błędy, wyjątki
# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonSrOr-11-06-2025\day_3\kl11.py", line 2, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# Process finished with exit code 1 - program zakończył z błedem
from mypy.util import write_junit_xml

try:
    # print(5 / 0)
    wynik = 9 / 8
except ZeroDivisionError:
    print("Nie dziel przez zero")
except Exception as e:
    print("Bład", e)
else:  # wykona się gdy nie ma błedu
    print("wynik:", wynik)  # Dalsza częśc programu
finally:
    print("Wykonuje się zawsze")
# gdyby był return finally również się wykona
print("Dalsza częśc programu")


class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą większą od zera"))
    if x <= 0:
        raise MyException("Liczba musi być większaa od zera")  # raise - rzucenie wyjątku

except MyException:
    print("Wartość musi być większa od zera")
except Exception as e:
    print("Bład", e)
else:
    print("Podana wartośc:", x)
finally:
    print("koniec")

# Podaj liczbę całkowitą większą od zeraa
# Bład invalid literal for int() with base 10: 'a'
# koniec
# Wartość musi być większa od zera
# koniec
