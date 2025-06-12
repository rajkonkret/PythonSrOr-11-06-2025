from itertools import zip_longest

person = ["Radek", "Tomek", "Zenek", "Agnieszka", "Paulina"]
age = [34, 45, 22, 56]

for p, w in zip(person, age):
    print(p, w)
# Radek 34
# Tomek 45
# Zenek 22
# Agnieszka 56

zipped = zip_longest(person, age, fillvalue="Brak Danych")
print(zipped)  # <itertools.zip_longest object at 0x00000169C65AAF70>

print(10 * "-")
for p, a in zipped:
    print(p, a)
# Radek 34
# Tomek 45
# Zenek 22
# Agnieszka 56
# Paulina Brak Danych
print(10 * "-")
for p, a in zipped:
    print(p, a)

print(10 * "-")
zipped = zip_longest(person, age, fillvalue="Brak Danych")
print(zipped)  # <itertools.zip_longest object at 0x00000169C65AAF70>
lista = list(zipped)
for item in lista:
    print(item)
# Radek 34
# Tomek 45
# Zenek 22
# Agnieszka 56
# <itertools.zip_longest object at 0x0000015E027DAF70>
# ----------
# Radek 34
# Tomek 45
# Zenek 22
# Agnieszka 56
# Paulina Brak Danych
# ----------
# ----------
# <itertools.zip_longest object at 0x0000015E02857A10>
# ('Radek', 34)
# ('Tomek', 45)
# ('Zenek', 22)
# ('Agnieszka', 56)
# ('Paulina', 'Brak Danych')
