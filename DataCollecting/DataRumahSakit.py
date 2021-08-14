import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

'''
Data ini akan diupdate oleh SIRANAP setiap harinya
'''

def TampilkanProvinsi():
    
    ListProvinsi = [
        "Aceh",
        "Sumatera Utara",
        "Sumatera Barat",
        "Riau",
        "Jambi",
        "Sumatera Selatan",
        "Bengkulu",
        "Lampung",
        "Kepulauan Bangka Belitung",
        "Kepulauan Riau",
        "DKI Jakarta",
        "Jawa Barat",
        "Jawa Tengah",
        "DI Yogyakarta",
        "Jawa Timur",
        "Banten",
        "Bali",
        "Nusa Tenggara Barat",
        "Nusa Tenggara Timur",
        "Kalimantan Barat",
        "Kalimantan Tengah",
        "Kalimantan Selatan",
        "Kalimantan Timur",
        "Kalimantan Utara",
        "Sulawesi Utara",
        "Sulawesi Tengah",
        "Sulawesi Selatan",
        "Sulawesi Tenggara",
        "Gorontalo",
        "Sulawesi Barat",
        "Maluku",
        "Maluku Utara",
        "Papua Barat",
        "Papua"
    ]

    return ListProvinsi

def TampilkanKabKota(NamaProvinsi):

    KodeProvinsi = {
        "Aceh" : "11prop",
        "Sumatera Utara" : "12prop",
        "Sumatera Barat" : "13prop",
        "Riau" : "14prop",
        "Jambi" : "15prop",
        "Sumatera Selatan" : "16prop",
        "Bengkulu" : "17prop",
        "Lampung" : "18prop",
        "Kepulauan Bangka Belitung" : "19prop",
        "Kepulauan Riau" : "20prop",
        "DKI Jakarta" : "31prop",
        "Jawa Barat" : "32prop",
        "Jawa Tengah" : "33prop",
        "DI Yogyakarta" : "34prop",
        "Jawa Timur" : "35prop",
        "Banten" : "36prop",
        "Bali" : "51prop",
        "Nusa Tenggara Barat" : "52prop",
        "Nusa Tenggara Timur" : "53prop",
        "Kalimantan Barat" : "61prop",
        "Kalimantan Tengah" : "62prop",
        "Kalimantan Selatan" : "63prop",
        "Kalimantan Timur" : "64prop",
        "Kalimantan Utara" : "65prop",
        "Sulawesi Utara" : "71prop",
        "Sulawesi Tengah" : "72prop",
        "Sulawesi Selatan" : "73prop",
        "Sulawesi Tenggara" : "74prop",
        "Gorontalo" : "75prop",
        "Sulawesi Barat" : "76prop",
        "Maluku" : "81prop",
        "Maluku Utara" : "82prop",
        "Papua Barat" : "91prop",
        "Papua" : "92prop"
    }

    URLKabKota = "https://yankes.kemkes.go.id/app/siranap/Kabkota?kode_propinsi=" + KodeProvinsi[NamaProvinsi]
    DataKabKota = requests.get(URLKabKota)
    JSONKabKota = DataKabKota.json()

    ListKabKota = []

    for i in range(len(JSONKabKota['data'])):
        ListKabKota.append(JSONKabKota['data'][i]['nama_kabkota'])

    return ListKabKota

def UpdateData(NamaProvinsi, NamaKabKota):

    Jenis = "1"

    KodeProvinsi = {
        "Aceh" : "11prop",
        "Sumatera Utara" : "12prop",
        "Sumatera Barat" : "13prop",
        "Riau" : "14prop",
        "Jambi" : "15prop",
        "Sumatera Selatan" : "16prop",
        "Bengkulu" : "17prop",
        "Lampung" : "18prop",
        "Kepulauan Bangka Belitung" : "19prop",
        "Kepulauan Riau" : "20prop",
        "DKI Jakarta" : "31prop",
        "Jawa Barat" : "32prop",
        "Jawa Tengah" : "33prop",
        "DI Yogyakarta" : "34prop",
        "Jawa Timur" : "35prop",
        "Banten" : "36prop",
        "Bali" : "51prop",
        "Nusa Tenggara Barat" : "52prop",
        "Nusa Tenggara Timur" : "53prop",
        "Kalimantan Barat" : "61prop",
        "Kalimantan Tengah" : "62prop",
        "Kalimantan Selatan" : "63prop",
        "Kalimantan Timur" : "64prop",
        "Kalimantan Utara" : "65prop",
        "Sulawesi Utara" : "71prop",
        "Sulawesi Tengah" : "72prop",
        "Sulawesi Selatan" : "73prop",
        "Sulawesi Tenggara" : "74prop",
        "Gorontalo" : "75prop",
        "Sulawesi Barat" : "76prop",
        "Maluku" : "81prop",
        "Maluku Utara" : "82prop",
        "Papua Barat" : "91prop",
        "Papua" : "92prop"
    }

    URLKabKota = "https://yankes.kemkes.go.id/app/siranap/Kabkota?kode_propinsi=" + KodeProvinsi[NamaProvinsi]
    DataKabKota = requests.get(URLKabKota)
    JSONKabKota = DataKabKota.json()

    KodeKabKota = {}

    for i in range(len(JSONKabKota['data'])):
        KodeKabKota[JSONKabKota['data'][i]['nama_kabkota']] = JSONKabKota['data'][i]['kode_kabkota']

    URL = "https://yankes.kemkes.go.id/app/siranap/" + "rumah_sakit" + "?" + "jenis=" + str(Jenis) + "&" + "propinsi=" + KodeProvinsi[NamaProvinsi] + "&" + "kabkota=" + KodeKabKota[NamaKabKota]

    Request = requests.get(URL)
    Soup = BeautifulSoup(Request.text, 'html.parser')

    ListRumahSakit = []

    NamaRumahSakit = Soup.find('h5', {'class' : 'mb-0'})
    AtributRumahSakit = Soup.find('p', {'class' : 'mb-0'})
    NoTelpRumahSakit = Soup.find('span', {'style' : 'font-size:13px;color:grey;'})

    while True:
        try:
            RumahSakit = {}

            RumahSakit['Nama'] = " ".join(str(NamaRumahSakit).replace('<h5 class="mb-0" style="color:#4D514D">', '').replace('</h5>', '').replace('\r\n', '').strip().split())
            NamaRumahSakit = NamaRumahSakit.find_next('h5', {'class' : 'mb-0'})

            RumahSakit['Alamat'] = " ".join(str(AtributRumahSakit).replace('<p class="mb-0" style="font-size:14px;color:#4D514D;">', '').replace('</p>', '').replace('\r\n', '').strip().split())
            AtributRumahSakit = AtributRumahSakit.find_next('p', {'class' : 'mb-0'})

            RumahSakit['Ketersediaan'] = " ".join(str(AtributRumahSakit).replace('<p class="mb-0" style="font-size:18px;color:#4D514D;">', '').replace('<p class="mb-0" style="font-size:18px;color:#F97B8B;">', '').replace('<b>', '').replace('</b>', '').replace('</p>', '').replace('\r\n', '').replace('!', '').strip().split())
            AtributRumahSakit = AtributRumahSakit.find_next('p', {'class' : 'mb-0'})

            RumahSakit['Antrian_Pasien'] = " ".join(str(AtributRumahSakit).replace('<p class="mb-0" style="font-size:14px;color:#4D514D;">', '').replace('<p class="mb-0" style="font-size:14px;color:#F97B8B;">', '').replace('</p>', '').replace('\r\n', '').replace('.', '').strip().split())
            AtributRumahSakit = AtributRumahSakit.find_next('p', {'class' : 'mb-0'})

            RumahSakit['No_Telepon'] = " ".join(str(NoTelpRumahSakit).replace('<span style="font-size:13px;color:grey;">', '').replace('</span>', '').strip().split())
            NoTelpRumahSakit = NoTelpRumahSakit.find_next('span', {'style' : 'font-size:13px;color:grey;'})

            RumahSakit['Waktu_Update'] = " ".join(str(AtributRumahSakit).replace('<p class="mb-0" style="font-size:13px;color:grey;">', '').replace('</p>', '').replace('\r\n', '').strip().split())
            AtributRumahSakit = AtributRumahSakit.find_next('p', {'class' : 'mb-0'})
            
            if " ".join(str(AtributRumahSakit).replace('<p class="mb-0" style="font-size:14px;color:#F97B8B;">', '').replace('</p>', '').replace('\r\n', '').replace('.', '').strip().split()) == "cek ketersediaan bed igd di waktu lain":
                AtributRumahSakit = AtributRumahSakit.find_next('p', {'class' : 'mb-0'})

            ListRumahSakit.append(RumahSakit)

        except:
            break

    df = pd.DataFrame(ListRumahSakit)

    df = df.replace("", "-")

    # Untuk Backend
    # df.to_csv(os.path.join(os.getcwd(), "paice", "src", "DataCollecting", "data_rumah_sakit.csv"), index=False)
    
    Data = df.reset_index().to_dict(orient='records') # Untuk Frontend

    for Object in Data:
        Object['key'] = Object.pop('index')

    return Data

if __name__ == "__main__":
    print(TampilkanProvinsi())

    Provinsi = ""

    ListProvinsi = TampilkanProvinsi()

    while Provinsi not in ListProvinsi:
        Provinsi = input("Masukkan Provinsi: ")

    print(TampilkanKabKota(Provinsi))

    KabKota = ""

    ListKabKota = TampilkanKabKota(Provinsi)

    while KabKota not in ListKabKota:
        KabKota = input("Masukkan Kabupaten/Kota: ")

    print(UpdateData(Provinsi, KabKota))