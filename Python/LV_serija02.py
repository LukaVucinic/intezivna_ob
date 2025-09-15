# 5

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
    naslov = ""
    autor = ""
    godinaizdanja = 0
    broj_kopija = 0

    def __init__(self, naslov, autor, godina_izdanja, broj_kopija):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.broj_kopija = broj_kopija

    def __str__(self):
        return f"naslov: {self.naslov}, autor: {self.autor}, godina_izdanja: {self.godina_izdanja}, broj_kopija: {self.broj_kopija}"

    def get_naslov(self):
        return self.naslov

    def get_autor(self):
        return self.autor

    def gte_god_izd(self):
        return self.godina_izdanja

    def get_br_kop(self):
        return self.broj_kopija

    def set_(self, naslov):
        self.naslov = naslov

    def set_(self, autor):
        self.autor = autor

    def set_(self, god_izd):
        self.godina_izdanja = god_izd

    def set_(self, br_kop):
        self.broj_kopija = br_kop


class Library:

    list_knjiga = []

    def __init__(self, lista):
        self.list_knjiga = lista

    def add_book(self, naslov, autor, godina_izdanja, broj_kopija):
        self.list_knjiga.append(
            Book(naslov, autor, godina_izdanja, broj_kopija))

    def delete_book(self, b):
        self.list_knjiga.remove(b)

    def find_book(self, b):
        return self.list_knjiga.index(b)

    def show_lib(self):
        for item in self.list_knjiga:
            print(item)


b1 = Book("n1", "a1", 1999, 10)
b2 = Book("n2", "a2", 1998, 1)
b3 = Book("n3", "a3", 1997, 5)

library1 = Library([b1, b2, b3])
for item in library1.list_knjiga:
    print(item)

library1.add_book("n4", "a4", 1990, 100)
library1.delete_book(b3)
for item in library1.list_knjiga:
    print(item)
# 12
