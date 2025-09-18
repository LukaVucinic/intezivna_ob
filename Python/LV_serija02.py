# # 5

class Podcast:
    def __init__(self, naziv, pos_comments, neg_comments):
        self.naziv = naziv
        self.pos_comments = pos_comments
        self.neg_comments = neg_comments

    def odnos(self):
        return self.pos_comments / self.neg_comments

    def __str__(self):
        return f"naziv: {self.naziv}, br_pozitivni: {self.pos_comments}, br_negativni: {self.neg_comments}"


p1 = Podcast("Español para principiantes", 1000, 10)
p2 = Podcast("Philophize This!", 500, 30)
p3 = Podcast("Science VS.", 600, 45)

podcasts = [p1, p2, p3]
min_odnos = p1.odnos()
min_id = p1
for podcast in podcasts:

    if min_odnos > podcast.odnos():
        min_odnos = podcast.odnos()
        min_id = podcast

print(min_id)
# 7


class Book:

    def __init__(self, naslov, autor, godina_izdanja, broj_kopija):
        self._naslov = naslov
        self._autor = autor
        self._godina_izdanja = godina_izdanja
        self._broj_kopija = broj_kopija

    def __str__(self):
        return f"naslov: {self._naslov}, autor: {self._autor}, godina_izdanja: {self.__format__godina_izdanja}, broj_kopija: {self._broj_kopija}"

    def get_naslov(self):
        return self._naslov

    def get_autor(self):
        return self._autor

    def gte_god_izd(self):
        return self._godina_izdanja

    def get_br_kop(self):
        return self._broj_kopija

    def set_naslov(self, naslov):
        self._naslov = naslov

    def set_autor(self, autor):
        self._autor = autor

    def set_god_izd(self, god_izd):
        self._godina_izdanja = god_izd

    def set_br_kop(self, br_kop):
        self._broj_kopija = br_kop


class Library:

    def __init__(self):
        self.list_knjiga = []

    def add_book(self, naslov, autor, godina_izdanja, broj_kopija):
        self.list_knjiga.append(
            Book(naslov, autor, godina_izdanja, broj_kopija))
        
    def add_book_as_book(self, book):
        self.list_knjiga.append(book)

    def delete_book_with_title(self, naslov):
        for knjiga in self.list_knjiga:
            if knjiga.get_naslov().lower() == naslov.lower():
                self.knjige.remove(knjiga)
                return
        print(f"Knjiga '{naslov}' ne postoji.")
    
    def find_book_by_title(self, naslov):
        return list(filter(lambda knjiga: naslov.lower() in knjiga.get_naslov().lower(), self.list_knjiga))
    
    def find_book_by_author(self, autor):
     return [knjiga for knjiga in self.list_knjiga if autor.lower() in knjiga.get_autor().lower()]

    def show_lib(self):
        if not self.list_knjiga:
            print("Biblioteka je prazna.")
        else:
            for item in self.list_knjiga:
                print(item)

library = Library()
b1 = Book("n1", "a1", 1999, 10)
b2 = Book("n2", "a2", 1998, 1)
b3 = Book("n3", "a3", 1997, 5)

library.add_book_as_book(b1)
library.add_book_as_book(b2)
library.add_book_as_book(b3)

# library.show_lib()
library.add_book("n6", "a6", 2025, 50)
# library.show_lib()


while True:
    print("1. Dodaj knjigu")
    print("2. Prikazi sve knjige")
    print("3. Pretrazi po naslovu")
    print("4. Pretrazi po autoru")
    print("5. Uredi knjigu")
    print("6. Obrisi knjigu")
    print("0. Izlaz")

    izbor = input("Izaberi opciju: ")

    if izbor == "1":
        naslov = input("Naslov: ")
        autor = input("Autor: ")
        godina = input("Godina izdanja: ")
        broj_kopija = int(input("Broj kopija: "))
        book = Book(naslov, autor, godina, broj_kopija)
        library.add_book_as_book(book)

    elif izbor == "2":
        library.show_lib()

    elif izbor == "3":
        naslov = input("Unesite naslov za pretragu: ")
        rezultat = library.find_book_by_title(naslov)
        for knjiga in rezultat:
            print(knjiga)
        if not rezultat:
            print("Nema rezultata.")

    elif izbor == "4":
        autor = input("Unesite autora za pretragu: ")
        rezultat = library.find_book_by_author(autor)
        for knjiga in rezultat:
            print(knjiga)
        if not rezultat:
            print("Nema rezultata.")

    elif izbor == "5":
        naslov = input("Unesite naslov knjige za uređivanje: ")
        rezultat = library.find_book_by_title(naslov)
        if rezultat:
            knjiga = rezultat[0]
            print("Pronađena knjiga:", knjiga)
            novi_naslov = input("Novi naslov: ")
            if novi_naslov:
                knjiga.set_naslov(novi_naslov)

            novi_autor = input("Novi autor: ")
            if novi_autor:
                knjiga.set_autor(novi_autor)

            nova_godina = input("Nova godina izdanja: ")
            if nova_godina:
                knjiga.set_god_izd(nova_godina)

            nove_kopije = input("Novi broj kopija: ")
            if nove_kopije:
                knjiga.set_br_kop(int(nove_kopije))
        else:
            print("Knjiga nije pronadjena.")

    elif izbor == "6":
        naslov = input("Unesi naslov knjige za brisanje: ")
        library.delete_book_with_title(naslov)

    elif izbor == "0":
        print("KRAJ")
        break

    else:
        print("Pogresan izbor")


# 12
class Company:
    def __init__(self, name, area, balance, max_num_of_employees):
        self._name = name
        self._area = area
        self._employees = []
        self._balance = balance if balance >= 0 else 0
        self._max_num_of_employees = max_num_of_employees if max_num_of_employees >= 0 else 0

    def get_name(self):
        return self._name

    def get_area(self):
        return self._area

    def get_balance(self):
        return self._balance

    def get_max_num_of_employees(self):
        return self._max_num_of_employees

    def set_name(self, name):
        self._name = name

    def set_area(self, area):
        self._area = area

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Balance ne moze biti manji od 0")

    def set_max_num_of_employees(self, max_num_of_employees):
        if max_num_of_employees >= 0:
            self._max_num_of_employees = max_num_of_employees
        else:
            print("Maksimalan broj zaposlenih ne moze biti manji od 0")

    def add_employee(self, employee):
        if len(self._employees) < self._max_num_of_employees:
            self._employees.append(employee)
        else:
            print("Nema mjesta")

    def remove_employee(self, employee_name, employee_surname):
        for emp in self._employees:
            if emp["name"].lower() == employee_name.lower() and emp["surname"].lower() == employee_surname.lower():
                self._employees.remove(emp)
                return
        print("Ne postoji taj zaposleni.")

    def __str__(self):
        return f'“name”: “{self._name}”, “area”: “{self._area}”, “balance”: “{self._balance}”'

    def can_pay_employees(self):
        ukupna_plata = 0.0
        for emp in self._employees:
            ukupna_plata += float(emp["salary"])
        return self._balance >= ukupna_plata

    def __gt__(self, other):
        return len(self._employees) > len(other._employees)


c1 = Company("comp1", "are1", 10000.0, 5)
c2 = Company("comp2", "are2", 5000.0, 3)

c1.add_employee({"name": "Petar", "surname": "Markovic", "salary": 2000})
c1.add_employee({"name": "Marija", "surname": "Ivanovic", "salary": 1500})
c1.add_employee({"name": "Janko", "surname": "Djurovic", "salary": 1500})

c2.add_employee({"name": "Ivan", "surname": "Kontic", "salary": 3000})

print(c1)
print(c2)

print("comp1 moze platiti zaposlene:", c1.can_pay_employees())
print("comp2 moze platiti zaposlene:", c2.can_pay_employees())

c1.remove_employee("Marija", "ivanovic")

if c1 > c2:
    print(f"{c1.get_name()} ima vise zaposlenih.")
else:
    print(f"{c2.get_name()} ima vise zaposlenih.")
