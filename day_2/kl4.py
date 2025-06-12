# __missing__ - wykonuje się gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d_python = {}
print(type(d_python))  # <class 'dict'>
print(d_python)  # {}
# print(d_python['name'])  # KeyError: 'name'

d1 = DefaultDict()
print(d1)
print(type(d1))  # <class '__main__.DefaultDict'>
print(DefaultDict.__mro__)  # (<class '__main__.DefaultDict'>, <class 'dict'>, <class 'object'>)

print(d1['name'])  # default


# słownik jak nie ma klucza doda go z wartością domyślną 0

class Autodict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


a1 = Autodict()
print(a1)  # {}
print(a1['name'])  # name
print(a1)  # {'name': 0}


class CaseInsenitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())
        return None


c1 = CaseInsenitiveDict()
c1['name'] = "Radek"
print(c1['Name'])
