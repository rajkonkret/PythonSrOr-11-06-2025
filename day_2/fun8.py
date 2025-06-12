# zrobic dekorator, który zmieni wynik dzialania funkcji na duże litery
# funkcja musi zwracac str
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper  # adres funckcji


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello world!!!"


# kolejnośc dekoratorów może mieć znaczenia
@bold_decorator
@uppercase_decorator
def greeting2(string):
    return f"Podałeś {string}"


print(greeting())
print(greeting2("Radek"))  # PODAŁEŚ RADEK

from colorama import init, Fore, Style

init(autoreset=True)  # powoduje wyłaczenie po kazdym print
print(Style.BRIGHT + "To jest pogrubiony tekst!")  # To jest pogrubiony tekst!
print(Fore.RED + "Czerwony tekst")  # Czerwony tekst
print("Nowy")


# rich

def wrap(*args):  # arguemty pozycyjne
    print(args)


wrap()
wrap(1, 2)  # (1, 2)


def wrap_all(*args, **kwargs):
    print(f"{args=}, {kwargs=}")


wrap_all()  # args=(), kwargs={}
wrap_all(45, name="Radek")
# args=(45,), kwargs={'name': 'Radek'}
