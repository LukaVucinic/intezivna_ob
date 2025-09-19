from functools import reduce
import time
from functools import wraps
from datetime import datetime


# 2
def najbolji_studenti(imena, ocjene):
    rezultat = []
    for i in range(len(imena)):
        if ocjene[i] > 8.5:
            rezultat.append((imena[i], ocjene[i]))
    return rezultat


imena = ["Petar", "Marija", "Ivan", "Janko"]
ocjene = [9.2, 8.3, 8.7, 7.5]

print(najbolji_studenti(imena, ocjene))


# 5
def prosjek_po_predmetu(podaci, predmet):
    filtrirani = list(filter(lambda x: x[2] == predmet, podaci))
    if not filtrirani:
        return None
    # print(filtrirani)
    ocjene = list(map(lambda x: x[1], filtrirani))
    zbir = reduce(lambda a, b: a + b, ocjene)
    return zbir / len(ocjene)


podaci = [
    ("Petar", 9.0, "pred1"),
    ("Marija", 8.5, "pred1"),
    ("Ivan", 10, "pred2"),
    ("Janko", 7.5, "pred1"),
]

print("Prosjek pred1:", prosjek_po_predmetu(podaci, "pred1"))
print("Prosjek pred2:", prosjek_po_predmetu(podaci, "pred2"))


# 14
def append_to_file(list_of_students):
    with open("students.txt", "a", encoding="utf-8") as f:
        for student in list_of_students:
            line = f"{student['ime']},{student['prezime']},{student['godina']},{student['prosjek']}\n"
            f.write(line)


def get_students_with_greater_grade(year, grade):
    grade_map = {
        "A": (9.5, 10),
        "B": (8.5, 9.5),
        "C": (7.5, 8.5),
        "D": (6.5, 7.5),
        "E": (6.0, 6.5),
    }

    min_val, _ = grade_map[grade]

    rezultat = []
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            ime, prezime, godina, prosjek = line.strip().split(",")
            godina = int(godina)
            prosjek = float(prosjek)
            if godina == year and prosjek >= min_val:
                rezultat.append({
                    "ime": ime,
                    "prezime": prezime,
                    "godina": godina,
                    "prosjek": prosjek
                })
    return rezultat


studenti1 = [
    {"ime": "”Marko”", "prezime": "”Markovic”", "godina": 2, "prosjek": 8.6},
    {"ime": "Boris", "prezime": "Boricic", "godina": 3, "prosjek": 7.9},
    {"ime": "Novak", "prezime": "Novovic", "godina": 3, "prosjek": 6.9}
]

append_to_file(studenti1)

studenti2 = [
    {"ime": "Janko", "prezime": "Djuroivc", "godina": 3, "prosjek": 6.0},
    {"ime": "Ivan", "prezime": "Kontic", "godina": 3, "prosjek": 9.7}
]

append_to_file(studenti2)

print(get_students_with_greater_grade(3, "C"))
print(get_students_with_greater_grade(3, "A"))


# 16

ZANROVI = ["Action", "Crime", "Sports", "FPS", "RPG", "Adventure"]


def validacija(naziv, ocjena, godina, izdavac, zanrovi):
    try:
        if not (2 <= len(naziv) <= 50):
            print("Los naziv")

        if not (1 <= round(float(ocjena), 2) <= 10):
            print("Losa ocjena")

        if not (1950 < int(godina) < datetime.now().year):
            print("Losa godina")

        if izdavac != "" and not (2 <= len(izdavac) <= 40):
            print("Los izdavac")

        zanrovi_list = zanrovi.split()
        if not (1 <= len(zanrovi_list) <= 3):
            print("Losi zanrovi")
        for z in zanrovi_list:
            if z not in ZANROVI:
                print(
                    f"Zanr '{z}' nije dozvoljen. Dozvoljeni: {','.join(ZANROVI)}")

        return {"naziv": naziv, "ocjena": ocjena, "godina": godina, "izdavac": izdavac, "zanrovi": zanrovi_list}

    except ValueError as err:
        print("Greska:", err)
        return None


def ucitaj_igrice():
    igrice = []

    with open("igrice.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            igrica = line.split(";")
            if len(igrica) != 5:
                continue

            naziv, ocjena, godina, izdavac, zanrovi = igrica
            igra = validacija(naziv, ocjena, godina, izdavac, zanrovi)
            if igra:
                igrice.append(igra)

    return igrice


def dodaj_igrice():
    igre = []
    while True:
        print("\nUnesite novu igru ili 'STOP':")
        naziv = input("Naziv: ")
        if naziv.upper() == "STOP":
            break
        ocjena = input("Ocjena 1-10: ")
        godina = input("Godina izlaska: ")
        izdavac = input("Izdavac: ")
        print(f"Moguci zanrovi: {', '.join(ZANROVI)}")
        zanrovi = input("Zanrovi: ")

        igrica = validacija(naziv, ocjena, godina, izdavac, zanrovi)
        if igrica:
            igre.append(igrica)
            with open("igrice.txt", "a", encoding="utf-8") as f:
                line = f"{igrica['naziv']};{igrica['ocjena']};{igrica['godina']};{igrica['izdavac']};{' '.join(igrica['zanrovi'])}\n"
                f.write(line)
            print("Igrica dodata.")
    return igre


def filtriraj_igrice(igrice):
    while True:
        print("Filteri:")
        print("1. Po nazivu")
        print("2. Po ocjeni vece od unesene")
        print("3. Po godini")
        print("4. Po izdavacu")
        print("5. Po zanru")
        print("6. STOP")

        izbor = input("Unesi broj 1-6: ")
        rezultat = []

        if izbor == "1":
            naziv = input("Naziv: ").lower()
            rezultat = [
                i for i in igrice if i["naziv"].lower().startswith(naziv)]

        elif izbor == "2":
            ocj = float(input("Minimalna ocjena 1-10: "))
            rezultat = [i for i in igrice if float(i["ocjena"]) >= ocj]

        elif izbor == "3":
            godina = int(input("Godina: "))
            opcija = input("prije/nakon: ").lower()
            if opcija == "prije":
                rezultat = [i for i in igrice if int(i["godina"]) < godina]
            else:
                rezultat = [i for i in igrice if int(i["godina"]) > godina]

        elif izbor == "4":
            izdavac = input("Ime izdavaca: ").lower()
            rezultat = [
                i for i in igrice if i["izdavac"].lower().startswith(izdavac)]

        elif izbor == "5":
            print(f"Dostupni zanrovi: {', '.join(ZANROVI)}")
            zanrovi = input("Zanrove 1-3 odvojeni sa space: ").lower().split()
            for i in igrice:
                temp = list(i["zanrovi"])
                provjera = []
                for zanr in temp:
                    zanr = zanr.lower()
                    provjera.append(zanr)
                if all(z in provjera for z in zanrovi):
                    rezultat.append(i)
        elif izbor == "6":
            break
        else:
            print("Nepoznat izbor")

        if rezultat:
            for i in rezultat:
                print(
                    f"{i['naziv']} ({i['ocjena']}) - {i['godina']} - {i['izdavac']} - {' '.join(i['zanrovi'])}")
        else:
            print("Nema rezultata")


igrice = ucitaj_igrice()

if igrice:
    for item in igrice:
        print(
            f"{item['naziv']} ({item['ocjena']}) - {item['godina']} - {item['izdavac']} - {' '.join(item['zanrovi'])}")
        # naziv - ocjena - godina - izdavac - zanr
else:
    print("Nema igrica")


while True:
    odgovor = input("Dodaj igrice?: ").lower()
    if odgovor == "da":
        nove_igre = dodaj_igrice()
        igrice.extend(nove_igre)
    elif odgovor == "ne":
        break
    else:
        print("Nepoznat odgovor")

filtriraj_igrice(igrice)


# 17
def mjerenje_vremena(funk):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = funk(*args, **kwargs)
        t2 = time.time()
        print(
            f"Funkcija '{funk.__name__}' je izvršena za {t2 - t1:.6f} sekundi")
        return res
    return wrapper


@mjerenje_vremena
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j


long_time(5)


@mjerenje_vremena
def fakt(n):
    if n == 0:
        return 1
    else:
        return n * fakt(n-1)


print("Faktorijal 10:", fakt(10))


@mjerenje_vremena
def suma_n_prvih(n):
    return sum(range(1, n+1))


print("Suma:", suma_n_prvih(1000000))
