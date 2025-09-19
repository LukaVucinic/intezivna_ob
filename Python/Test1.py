import re


# 4 a
def najveca_duzina():
    while True:
        duzina1 = int(input("Duzina 1:"))
        duzina2 = int(input("Duzina 2:"))
        duzina3 = int(input("Duzina 3:"))

        if (duzina1 == duzina2 and duzina2 == duzina3):
            break

        return max(duzina1, duzina2, duzina3)


# print(najveca_duzina())


# 4 b
def broj_recenica(tekst):
    sentences = re.split(r'(?<=[.!?])\s*', tekst)
    return len(sentences)-1


t1 = "Recenica broj 1.Recenica broj 2? Recenica broj 3!"
print(broj_recenica(t1))


# 4 c

def presjek(lista1, lista2):
    return [item1 for item1 in lista1 for item2 in lista2 if item1 == item2]


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
print(presjek(lista1, lista2))

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 4, 5, 6, 7]
print(presjek(lista1, lista2))

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 4, 5, 6, 7]
print(set(presjek(lista1, lista2)))
