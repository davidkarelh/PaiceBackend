import pandas as pd
import os

'''
Data ini akan terus diupdate oleh Wikipedia setiap harinya
'''

def TranslateProvinsi():
    
    MapProvinsi = {
        "Aceh" : "Aceh",
        "North Sumatra" : "Sumatera Utara",
        "West Sumatra" : "Sumatera Barat",
        "Riau" : "Riau",
        "Jambi" : "Jambi",
        "South Sumatra" : "Sumatera Selatan",
        "Bengkulu" : "Bengkulu",
        "Lampung" : "Lampung",
        "Bangka Belitung Islands" :"Kepulauan Bangka Belitung",
        "Riau Islands" : "Kepulauan Riau",
        "Jakarta" : "DKI Jakarta",
        "West Java" : "Jawa Barat",
        "Central Java" : "Jawa Tengah",
        "Special Region of Yogyakarta" : "DI Yogyakarta",
        "East Java" : "Jawa Timur",
        "Banten" : "Banten",
        "Bali" : "Bali",
        "West Nusa Tenggara" : "Nusa Tenggara Barat",
        "East Nusa Tenggara" : "Nusa Tenggara Timur",
        "West Kalimantan" : "Kalimantan Barat",
        "Central Kalimantan" : "Kalimantan Tengah",
        "South Kalimantan" : "Kalimantan Selatan",
        "East Kalimantan" : "Kalimantan Timur",
        "North Kalimantan" : "Kalimantan Utara",
        "North Sulawesi" : "Sulawesi Utara",
        "Central Sulawesi" : "Sulawesi Tengah",
        "South Sulawesi" : "Sulawesi Selatan",
        "Southeast Sulawesi" : "Sulawesi Tenggara",
        "Gorontalo" : "Gorontalo",
        "West Sulawesi" : "Sulawesi Barat",
        "Maluku" : "Maluku",
        "North Maluku" : "Maluku Utara",
        "West Papua" : "Papua Barat",
        "Papua" : "Papua",
        "Total" : "Total"
    }

    return MapProvinsi

def UpdateData():

    Table = pd.read_html("https://en.wikipedia.org/wiki/Statistics_of_the_COVID-19_pandemic_in_Indonesia", match="COVID-19 cases in Indonesia")

    df = Table[0]["COVID-19 cases in Indonesia[a][b]"]

    df = df.replace("", "-")

    df = df.drop(df.index[35])
    df = df.drop(["Recoveryrate", "Fatalityrate", "Official website"], axis=1)
    df = df.rename(columns={"Active[c]" : "kasus_aktif", "Cases per100,000 population[d]" : "kasus_per_100000_penduduk", "index" : "key", "Province" : "provinsi", "Cases" : "kasus_kumulatif", "Recoveries" : "sembuh", "Deaths" : "meninggal"})

    Translate = TranslateProvinsi()

    for i in range(len(df)):
        df.iloc[i]['provinsi'] = Translate[df.iloc[i]['provinsi']]

    # Untuk Backend
    # df.to_csv(os.path.join(os.getcwd(), "paice", "src", "DataCollecting", "data_covid.csv"), index=False)

    Data = df.reset_index().to_dict(orient='records') # Untuk Frontend

    for Object in Data:
        Object['key'] = Object.pop('index')

    return Data

if __name__ == "__main__":
    print(UpdateData())