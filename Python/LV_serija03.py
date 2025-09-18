from functools import reduce
import time
from functools import wraps


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
