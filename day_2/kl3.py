from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contact = []
        for c in self:
            if name == c.name:
                matching_contact.append(c)

        return matching_contact


contact_list = ContactList()
print(contact_list)  # []
print(contact_list.search("Radek"))  # []


class Contact:
    """
    Klasa Contact
    """
    # all_contacts = []
    all_contacts = ContactList()

    def __init__(self, name, email):
        """

        :param name:
        :param email:
        """
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):  # __repr__ nadpisze __str__  gdy ten nie istnieje
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa dziedziczy po kalsie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, mail, phone="+48000-000-000"):
        super().__init__(name, mail)  # obowiązkowo super() - klasa nadrzędna
        self.phone = phone

    def __repr__(self):  # __repr__ nadpisze __str__  gdy ten nie istnieje
        # !r - opakowuje stringi cudzysłowami '', konwersja formatowania
        return f"{self.name!r} {self.email!r}, {self.phone!r}"


c1 = Contact("Adam", "adam@wp.pl")
print(c1)  # Adam adam@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
print(c2)  # Radek radek@wp.pl
print(c1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl]
print(c2.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl]

s1 = Suplier("Marek", "marek@wp.pl")
print(s1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl]
s1.order("kawa")  # kawa zamówiono od Marek
print(Contact.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl]
print(Contact.all_contacts.search("Radek"))  # [Radek radek@wp.pl]

f1 = Friend("Kasia", "kasia@wp.pl")
print(f1)
print(f1.all_contacts)
# Kasia kasia@wp.pl
# [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl]
# Kasia kasia@wp.pl, +48000-000-000
# [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl, +48000-000-000]
print(
    Friend.__mro__)  # (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
# kolejnośc rozwiązywania nazw
# [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl]
# [Radek radek@wp.pl]
# 'Kasia' 'kasia@wp.pl', '+48000-000-000'
# [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl, 'Kasia' 'kasia@wp.pl', '+48000-000-000']
f2 = Friend("Asia", "asia@wp.pl", "567890345")
print(f2.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl,
# 'Kasia' 'kasia@wp.pl', '+48000-000-000', 'Asia' 'asia@wp.pl', '567890345']

pprint(f2.all_contacts)
# [Adam adam@wp.pl,
#  Radek radek@wp.pl,
#  Marek marek@wp.pl,
#  'Kasia' 'kasia@wp.pl', '+48000-000-000',
#  'Asia' 'asia@wp.pl', '567890345']
