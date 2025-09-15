# 18
# Napisati program kojim se na osnovu temperature vode određuje njeno agregatno
# stanje. Ako je temperatura:
# • viša od 0 C i niža od 100C - agregatno stanje je tečno
# • ne viša od 0 C - agregatno stanje je čvrsto,
# • ne niža od 100 C - agregatno stanje je gasovito.
# Za temperaturu od tačno 0 smatra se da je agregatno stanje čvrsto, a za tačno 100 da je
# gasovito.
# Ulaz: Temperatura - cio broj
# Izlaz: Na standardni izlaz ispisati jednu od sledećih riječi: cvrsto, tecno, gasovito

import math


def agregatno_stanje(temp):
    if 0 < temp < 100:
        print("Tecno")
    elif temp <= 0:
        print("Cvsto")
    else:
        print("Gasovito")


agregatno_stanje(101)
# 23
# Napisati kod koji za date realne brojeve x i y provjerava da li tačka sa koordinatama
# (x,y) pripada osjenčenom dijelu ravni. Centar oba kruga je u tački (0,0), poluprečnici su
# im redom 4 i 6, dok je prava data jednačinom x-y-4=0. Podsjetite se da je krug skup
# tačaka u ravni koje su na rastojanju r od date tačke tj. centra kruga. Štampati poruku
# „Pripada“ ili „Ne pripada“. Pomoć da li se tačka nalazi iznad ili ispod prave se nalazi na


def euklid(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def funk2(x, y):
    a = euklid(x, y, 0, 0)  # rastojanje od centra kruga
    if 4 < a < 6 and x < 0 and y > 0:
        print("Pripada")
    elif x > 0 and y > 0 and 0 < a < 4:
        print("Pripada")
    elif x > 0 and y > 0 and 4 < a < 6 and y < x-4:
        print("Pripada")
    elif x > 0 and y < 0 and 0 < a < 4 and y < x-4:
        print("Pripada")
    else:
        print("Ne pripada")


# 39

def funk39(num):
    li = [int(x) for x in str(num)]
    sum = 0
    for item in li:
        sum = sum + item ** len(li)
    if sum == num:
        print("Da")
    else:
        print("Ne")


funk39(153)
# 96
# Napisati program koji ima dva parametra string i number gdje prvi parametar predstavlja
# ulazni string, dok number predstavlja broj na osnovu koga se radi razbijanje stringa na
# podstringove. Funkcija treba da vrati niz/listu podstringova zadate dužine. Ako poslednji
# podstring ne sadrži dovoljno karaktera dopuniti ga sa *. Napomena: space se takođe
# računa kao karakter.
# Primjer 1:
# split_string(“danas polažemo test”, 5) -> [“danas”, “ pola”, “žemo ”, “test*”]
# Primjer 2:
# split_string(“kurs web program.”, 6) -> [“kurs w”, “eb pro”, “gram.*”]
# Primjer 3:
# split_string(“da”, 7) -> [“da*****”]


def split_string(string, number):
    result = []
    i = 0
    n = len(string)

    while i < n:
        substring = string[i:i + number]

        if len(substring) < number:
            substring += '*' * (number - len(substring))

        result.append(substring)
        i += number

    return result
