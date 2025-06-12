class Contact:
    """
    Klasa Contact
    """
    all_contacts = []

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
# Contact.all_contacts.search("Radek")  # AttributeError: 'list' object has no attribute 'search'
