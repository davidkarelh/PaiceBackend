import requests
import os
import re
import xml.etree.ElementTree as ET
import pandas as pd

'''
Data ini akan diupdate oleh covid19.go.id setiap harinya
'''

def CleanHTML(RawHTML):
    return re.sub(re.compile('<.*?>'), '', RawHTML)

def TampilkanFeed():

    ListFeed = [
        "Berita",
        "Masyarakat Umum",
        "Protokol",
        "Panduan",
        "Melakukan Perjalanan",
        "Tenaga Kesehatan",
        "Pengusaha & Bisnis",
        "Hoax Buster",
        "Protokol",
        "Regulasi",
        "Tanya Jawab"
    ]

    return ListFeed

def UpdateData(Feed):
    
    KodeFeed = {
        "Berita" : "berita",
        "Masyarakat Umum" : "masyarakat-umum",
        "Protokol" : "protokol",
        "Panduan" : "panduan",
        "Melakukan Perjalanan" : "melakukan-perjalanan",
        "Tenaga Kesehatan" : "tenaga-kesehatan",
        "Pengusaha & Bisnis" : "pengusaha-dan-bisnis",
        "Hoax Buster" : "hoax-buster",
        "Protokol" : "protokol",
        "Regulasi" : "regulasi",
        "Tanya Jawab" : "tanya-jawab"
    }

    URL = "http://covid19.go.id/feed/" + KodeFeed[Feed]
    DataBerita = requests.get(URL)

    tree = ET.ElementTree(ET.fromstring(DataBerita.content))

    root = tree.getroot()

    NewsItem = []

    for item in root.findall('./channel/item'):

        News = {}

        for child in item:

            if child.text == None or child.tag == 'guid' or child.tag == 'description':
                continue
            else:
                News[child.tag] = " ".join(CleanHTML(child.text).replace('\n', '').replace('=', '').strip().split())
        
        NewsItem.append(News)

    df = pd.DataFrame(NewsItem)

    df = df.replace("", "-")

    df = df.rename(columns={"title" : "Judul", "link" : "URL", "pubDate" : "Waktu_Update"})

    # Untuk Backend
    # df.to_csv(os.path.join(os.getcwd(), "paice", "src", "DataCollecting", "data_berita.csv"), index=False)

    Data = df.reset_index().to_dict(orient='records') # Untuk Frontend

    for Object in Data:
        Object['key'] = Object.pop('index')

    return Data

if __name__ == "__main__":
    print(UpdateData("Berita"))