import requests
import csv
from bs4 import BeautifulSoup


def get_page_content(url):
    response = requests.get(url)
    return response.content


original_link = "https://www.udg.edu.me/fakulteti"

data = []
data2 = []


content = get_page_content(original_link)
soup = BeautifulSoup(content, 'html.parser')
fac_list = soup.find_all("div", class_="faculty-item")
fac_links_list = []
fac_names = []
for faculty in fac_list:
    temp = faculty.find("a")
    temp2 = temp["href"].split("/")[-1].lower()
    if temp2 == "pt":
        temp2 = "politehnika"
    if temp2 == "fuk":
        temp2 = "fu"
    if temp2 == "cfl":
        break
    li = "https://"+temp2+".udg.edu.me/predavaci/"
    fac_names.append(temp2)
    fac_links_list.append(li)


for i in range(len(fac_links_list)):

    fak_content = get_page_content(fac_links_list[i])
    fak_name = fac_names[i]

    soup2 = BeautifulSoup(fak_content, "html.parser")
    t_list = []
    teachers_list = soup2.find_all("a", class_="teacher-name")

    for teacher in teachers_list:
        t_list.append(teacher.text.strip())

    count = 0
    titule = ["Prof. dr", "Doc. dr", "Doc. mr", "dr", "mr"]
    titula_count = [[], [], [], [], [], []]

    for teacher_item in t_list:
        flag = False
        for titula in range(5):
            if (teacher_item.startswith(titule[titula])):
                titula_count[titula].append(teacher_item)
                flag = True
                ime = teacher_item.removeprefix(titule[titula])

                data2.append(
                    {"fakultet": fak_name, "titula": titule[titula], "ime i prezime": ime})
                break
        if not flag:
            titula_count[-1].append(teacher_item)
            data2.append(
                {"fakultet": fak_name, "titula": "", "ime i prezime": teacher_item})

    dataaa = {"fakultet": fak_name,
              "Prof. dr": len(titula_count[0]),
              "Doc. dr": len(titula_count[1]),
              "Doc. mr": len(titula_count[2]),
              "dr": len(titula_count[3]),
              "mr": len(titula_count[4]),
              "bez titule": len(titula_count[5]),
              }

    data.append(dataaa)


fieldnames = ["fakultet", "Prof. dr", "Doc. dr",
              "Doc. mr", "dr", "mr", "bez titule"]

csv_filename = "fajl1.csv"
with open(csv_filename, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

csv_filename = "fajl2.csv"
fieldnames2 = ["fakultet", "titula", "ime i prezime"]
with open(csv_filename, mode='w', encoding="utf-8") as file2:
    writer = csv.DictWriter(file2, fieldnames=fieldnames2)
    writer.writeheader()
    writer.writerows(data2)
