import pickle
from dataclasses import dataclass
from kl9 import Person

# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int
#
#     def greets(self):
#         print("My name is:", self.first_name)
#
if __name__ == '__main__':
    with open('lista.txt', "r") as file:
        data = file.read()

    print(data)
    print(type(data))  # <class 'str'>

    with open('dane.pckl', "rb") as file:
        p = pickle.load(file)

    print(10 * "-")
    print(p)
    print(type(p))  # <class 'list'>
