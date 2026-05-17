import pandas as pd
from rapidfuzz import process, fuzz
from unidecode import unidecode
import re

dosya1 = pd.read_csv("titck_liste_18.04.csv")
dosya2 = pd.read_excel("ATC_14_04.xlsx")

def yazi_temizle(x):
    if pd.isna(x):
        return ""

    x = str(x)
    x = unidecode(x)
    x = x.lower()
    x = re.sub(r"[^a-z0-9 ]", " ", x)
    x = re.sub(r" +", " ", x)
    x = x.strip()

    return x

dosya1["ad1"] = dosya1["Ilac_Adi"].apply(yazi_temizle)
dosya1["madde1"] = dosya1["Etkin_Madde"].apply(yazi_temizle)
dosya1["firma1"] = dosya1["Firma"].apply(yazi_temizle)

dosya2["ad2"] = dosya2["İlaç Adı"].apply(yazi_temizle)
dosya2["madde2"] = dosya2["ATC Adı"].apply(yazi_temizle)

dosya1["karsilastirma"] = dosya1["ad1"] + " " + dosya1["madde1"] + " " + dosya1["firma1"]
dosya2["karsilastirma"] = dosya2["ad2"] + " " + dosya2["madde2"]

atc_liste = list(dosya2["karsilastirma"])

son_liste = []
sayac = 0

while sayac < len(dosya1):

    satir = dosya1.iloc[sayac]

    if sayac % 100 == 0:
        print(sayac, "satir yapildi")

    bulunan_sonuc = process.extractOne(
        satir["karsilastirma"],
        atc_liste,
        scorer=fuzz.token_sort_ratio
    )

    bulunan_index = bulunan_sonuc[2]
    puan = bulunan_sonuc[1]

    bulunan_satir = dosya2.iloc[bulunan_index]

    yeni_satir = {
        "TITCK_ID": satir["ID"],
        "TITCK_Ilac_Adi": satir["Ilac_Adi"],
        "ATC_Barkod": bulunan_satir["Barkod"],
        "ATC_Kodu": bulunan_satir["ATC Kodu"],
        "ATC_Durumu": bulunan_satir["Durumu"],
        "Match_Score": round(puan, 2)
    }

    son_liste.append(yeni_satir)
    sayac = sayac + 1

sonuc = pd.DataFrame(son_liste)
sonuc.to_csv("eslesmis_ilaclar.csv", index=False, encoding="utf-8-sig")

print("islem bitti")