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
df["Godine"]=pd.to_numeric(df["Godine"], errors="coerce")
# print("Srednja vr. godina je",df["Godine"].mean())
# df["Godine"] = df["Godine"].fillna(df["Godine"].mean().round()).astype("Int64")
# print(df["Godine"])
print("------------------------------------------------------------------------------------------------------------")

df["Prosek"]=pd.to_numeric(df["Prosek"], errors="coerce")
print("Medijan prosjeka je",df["Prosek"].median())
print("------------------------------------------------------------------------------------------------------------")
df["Prosek"] = df["Prosek"].fillna(df["Prosek"].median())
print(df.head())
print("------------------------------------------------------------------------------------------------------------")

df["Grad"] = df["Grad"].fillna("nepoznat")
print(df.head())
print("------------------------------------------------------------------------------------------------------------")

print(df["Grad"].unique())
df["Grad"] = df["Grad"].replace('NIÅ\xa0', 'Nis')
df["Grad"] = df["Grad"].replace('NiÅ¡', 'Nis')
df["Grad"] = df["Grad"].replace(' ', 'nepoznat')
df["Grad"] = df["Grad"].str.title()
print("------------------------------------------------------------------------------------------------------------")

print(df["Ime"].unique())
df["Ime"] = df["Ime"].fillna("nepoznat")
df["Ime"] = df["Ime"].replace(" ", "nepoznat")
print("------------------------------------------------------------------------------------------------------------")

print(df["Godine"].unique())
df.loc[df["Godine"] < 0, "Godine"] = df["Godine"].abs()
df.loc[df["Godine"] > 100, "Godine"] = df["Godine"] / 10
df.loc[df["Godine"] < 15, "Godine"] = df["Godine"] + 15
mean_godine = df["Godine"].mean()
print("Srednja vr. godina je",mean_godine)
df["Godine"] = df["Godine"].fillna(df["Godine"].mean().round()).astype("Int64")
print(df["Godine"].unique())
print("------------------------------------------------------------------------------------------------------------")


print(df["Prosek"].unique())
df["Prosek"] = df["Prosek"].mask((df["Prosek"] < 5) | (df["Prosek"] > 10), df["Prosek"].mean())
print(df["Prosek"].unique())
print("------------------------------------------------------------------------------------------------------------")

df["Datum_upisa"] = pd.to_datetime(df["Datum_upisa"], errors="coerce")
df["Datum_diplomiranja"] = pd.to_datetime(df["Datum_diplomiranja"], errors="coerce")
print("------------------------------------------------------------------------------------------------------------")

print(df["ESPB"].unique())
df["ESPB"] = pd.to_numeric(df["ESPB"], errors="coerce")
mean_espb = df["ESPB"][df["ESPB"] >= 0].mean().round()
df.loc[(df["ESPB"] < 0) | (df["ESPB"] > 300) | (df["ESPB"].isna()), "ESPB"] = mean_espb
print(df["ESPB"].unique())
print("------------------------------------------------------------------------------------------------------------")

print(df["Email"].unique())
df["Email"] = df["Email"].astype(str)
df["Email"] = df["Email"].where(df["Email"].str.contains(r"^[\w\.-]+@[\w\.-]+\.\w+$", regex=True), pd.NA)
print(df["Email"].unique())
print("------------------------------------------------------------------------------------------------------------")

print(df["Telefon"].unique())
df["Telefon"] = df["Telefon"].astype(str)
df["Telefon"] = df["Telefon"].str.replace(r"\D", "", regex=True)
df["Telefon"] = df["Telefon"].where(df["Telefon"].str.len().between(8, 12), pd.NA)
print(df["Telefon"].unique())
print("------------------------------------------------------------------------------------------------------------")