import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:sifra123@localhost/coinisvjezba")
query = "SELECT * FROM studenti"
df = pd.read_sql_query(query, engine)
engine.dispose()

print("PRVIH 10 REDOVA: ")
print(df.head(10))
print("------------------------------------------------------------------------------------------------------------")

print("INFO:")
df.info()
print("------------------------------------------------------------------------------------------------------------")

print("DESCRIBE:")
print(df.describe())
print("------------------------------------------------------------------------------------------------------------")

print(f"Dataset ima {df.shape[0]} redova i {df.shape[1]} kolona.")
print("------------------------------------------------------------------------------------------------------------")

df = df.replace("", pd.NA)
print("Kolone sa NaN vrijednostima:", df.columns[df.isna().any()].tolist())
print("------------------------------------------------------------------------------------------------------------")

df["Godine"] = pd.to_numeric(df["Godine"], errors="coerce")
# print("Srednja vr. godina je", df["Godine"].mean())
# df["Godine"] = df["Godine"].fillna(df["Godine"].mean().round()).astype("Int64")
print(df["Godine"])
print("------------------------------------------------------------------------------------------------------------")

df["Prosek"] = pd.to_numeric(df["Prosek"], errors="coerce")
print("Medijan prosjeka je", df["Prosek"].median())
print("------------------------------------------------------------------------------------------------------------")
df["Prosek"] = df["Prosek"].fillna(df["Prosek"].median())
print(df.head())
print("------------------------------------------------------------------------------------------------------------")

df["Grad"] = df["Grad"].replace('NIÅ\xa0', 'Nis')
df["Grad"] = df["Grad"].replace('NiÅ¡', 'Nis')
df["Grad"] = df["Grad"].replace(' ', pd.NA)
df["Grad"] = df["Grad"].replace('', pd.NA)
df["Grad"] = df["Grad"].str.title()
df["Grad"] = df["Grad"].fillna("nepoznat")
print(df.head())
print("------------------------------------------------------------------------------------------------------------")

print(df["Grad"].unique())
print("------------------------------------------------------------------------------------------------------------")

print(df["Ime"].unique())
df["Ime"] = df["Ime"].fillna("nepoznat")
df["Ime"] = df["Ime"].replace(" ", "nepoznat")
print(df["Ime"].unique())
print("------------------------------------------------------------------------------------------------------------")

print(df["Godine"].unique())
df.loc[df["Godine"] < 0, "Godine"] = df["Godine"].abs()
df.loc[df["Godine"] > 100, "Godine"] = df["Godine"] / 10
df.loc[df["Godine"] < 15, "Godine"] = df["Godine"] + 15
mean_godine = df["Godine"].mean()
print("Srednja vr. godina je", mean_godine)
df["Godine"] = df["Godine"].fillna(df["Godine"].mean().round()).astype("Int64")
print(df["Godine"].unique())
print("------------------------------------------------------------------------------------------------------------")

print(df["Prosek"].unique())
df.loc[(df["Prosek"] < 5) | (df["Prosek"] > 10),
       "Prosek"] = df["Prosek"].mean()
print(df["Prosek"].unique())
print("------------------------------------------------------------------------------------------------------------")


print(df["ESPB"].unique())
df["ESPB"] = pd.to_numeric(df["ESPB"], errors="coerce")
mean_espb = df["ESPB"][(df["ESPB"] >= 0) & (df["ESPB"] <= 240)].mean().round()
print("Srednja vr. ESPB:", int(mean_espb))
df.loc[(df["ESPB"] < 0) | (df["ESPB"] > 240) |
       (df["ESPB"].isna()), "ESPB"] = mean_espb
df["ESPB"] = df["ESPB"].astype("Int64")
print(df["ESPB"].unique())
print("------------------------------------------------------------------------------------------------------------")

print(df["Email"].unique())
df = df[df["Email"].str.contains(
    r"^[\w\.-]+@[\w\.-]+\.\w+$", regex=True, na=False)]
print(df["Email"])
print("------------------------------------------------------------------------------------------------------------")

print(df["Telefon"].unique())
df["Telefon"] = df["Telefon"].astype(str).str.replace(r"\D", "", regex=True)
print(df["Telefon"].unique())


def standardizuj_telefon(tel):
    if pd.isna(tel) or len(tel) < 8:
        return pd.NA
    if tel.startswith("0"):
        return "+381" + tel[1:]
    elif tel.startswith("381"):
        return "+" + tel
    elif tel.startswith("+381"):
        return tel
    return pd.NA


df["Telefon"] = df["Telefon"].apply(standardizuj_telefon)
print(df["Telefon"].unique())
print("------------------------------------------------------------------------------------------------------------")

df = df.drop_duplicates()
# for col in df.columns:
#     df = df.drop_duplicates(subset=[col], keep="first")
# print(df.head())


print(df["Datum_diplomiranja"].unique())
print(df["Datum_upisa"].unique())


def parse_date(x):
    if pd.isna(x):
        return pd.NaT
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y"):
        try:
            return pd.to_datetime(x, format=fmt)
        except:
            continue
    return pd.NaT


df["Datum_upisa"] = df["Datum_upisa"].apply(parse_date)
df["Datum_diplomiranja"] = df["Datum_diplomiranja"].apply(parse_date)
df["Trajanje_studija"] = (df["Datum_diplomiranja"] -
                          df["Datum_upisa"]).dt.days / 365

# df["Datum_upisa"] = df["Datum_upisa"].dt.strftime("%Y-%m-%d")
# df["Datum_diplomiranja"] = df["Datum_diplomiranja"].dt.strftime("%Y-%m-%d")
print("------------------------------------------------------------------------------------------------------------")

print(df["Datum_diplomiranja"].unique())
print(df["Datum_upisa"].unique())
print("------------------------------------------------------------------------------------------------------------")

najduzi = df.loc[df["Trajanje_studija"].idxmax()]
najkraci = df.loc[df["Trajanje_studija"].idxmin()]

print("Student sa najdužim trajanjem studija:", najduzi)
print("Student sa najkraćim trajanjem studija:", najkraci)
print("------------------------------------------------------------------------------------------------------------")


plt.figure(figsize=(8, 5))
plt.hist(df["Godine"], bins=range(df["Godine"].min(),
         df["Godine"].max()+2), color='skyblue', edgecolor='black')
plt.title("Raspodjela godina studenata")
plt.xlabel("Godine")
plt.ylabel("Broj studenata")
plt.show()

plt.figure(figsize=(6, 5))
plt.boxplot(df["Prosek"], patch_artist=True,
            boxprops=dict(facecolor='lightgreen'))
plt.title("Raspodjela prosjecnog prosjeka")
plt.ylabel("Prosjek")
plt.show()

prosjek_po_gradu = df.groupby("Grad")["Prosek"].mean()
plt.figure(figsize=(8, 5))
prosjek_po_gradu.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Prosjecan prosjek po gradu")
plt.xlabel("Grad")
plt.ylabel("Prosjek")
plt.show()

plt.figure(figsize=(8, 5))
for grad in df["Grad"].unique():
    plt.hist(df[df["Grad"] == grad]["ESPB"], bins=range(
        0, max(df["ESPB"])+50, 50), alpha=0.5, label=grad)
plt.title("Raspodjela ESPB po gradovima")
plt.xlabel("ESPB")
plt.ylabel("Broj studenata")
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Godine"], df["Prosek"], color='purple')
plt.title("Godine - Prosjek")
plt.xlabel("Godine")
plt.ylabel("Prosek")
plt.grid(True)
plt.show()

df["Godina_upisa"] = df["Datum_upisa"].dt.year
prosjek_po_godini = df.groupby("Godina_upisa")["Prosek"].mean()
plt.figure(figsize=(8, 5))
plt.plot(prosjek_po_godini.index,
         prosjek_po_godini.values, marker='o', color='red')
plt.title("Prosjecan prosjek po godini upisa")
plt.xlabel("Godina upisa")
plt.ylabel("Prosjek")
plt.grid(True)
plt.show()


df["Godina_upisa"] = df["Datum_upisa"].dt.year
pivot = pd.pivot_table(df, values="Prosek", index="Grad",
                       columns="Godina_upisa", aggfunc="mean")
print("Prosjecan prosjek po gradu i godini upisa:")
print(pivot)

top5 = df.nlargest(5, "Prosek")[["Ime", "Grad", "Prosek"]]
print("Top 5 studenata sa najvisim prosjekom:")
print(top5)

prosj_vr_espb_po_gradu = df.groupby("Grad")["ESPB"].mean()
print("Prosječan broj ESPB bodova po gradu:")
print(prosj_vr_espb_po_gradu)

df.to_csv("ocisceni_studenti_dataset_700.csv", index=False)
