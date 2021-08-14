from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.getcwd()), "DataCollecting"))
import DataCovid
import DataRumahSakit
import DataOksigen
import DataVaksin
import DataBerita

app = Flask(__name__)
CORS(app)

# ProvinsiRS = ""
# KotaRS = ""
@app.route('/')
def index():
    return {"Response": "Response"}

@app.route('/statistik')
def statistik():
    Data = DataCovid.UpdateData()
    for datas in Data:
        del datas["kasus_kumulatif"]
        del datas["kasus_per_100000_penduduk"]
        del datas["meninggal"]
        del datas["sembuh"]
        datas["rumahSakit"] = True
        datas["infoOksigen"] = True
        datas["lokasiVaksinasi"] = True
    Data.pop()
    return {"Response": Data}

@app.route('/hospital', methods=['GET', 'POST'])
def hospital():
    ProvinsiRS = ""
    KotaRS = ""
    if request.method == 'GET':
        return {"Response": DataRumahSakit.TampilkanProvinsi()}
    elif request.method == 'POST' and "Kota" in request.get_json() and "Provinsi" in request.get_json():
        ProvinsiRS = request.get_json()["Provinsi"]
        KotaRS = request.get_json()["Kota"]
        return {"Response": DataRumahSakit.UpdateData(ProvinsiRS, KotaRS)}
    elif request.method == 'POST' and "Provinsi" in request.get_json():
        ProvinsiRS = request.get_json()["Provinsi"]
        return {"Response": DataRumahSakit.TampilkanKabKota(request.get_json()["Provinsi"])}


@app.route('/oksigen', methods=['GET', 'POST'])
def oksigen():
    ProvinsiOks = ""
    KotaOks = ""
    if (sys.platform == "darwin"):
        path = os.path.join(os.path.dirname(os.getcwd()), 'DataCollecting', 'chromedriver_mac64', 'chromedriver')
    elif (sys.platform == "win32"):
        path = os.path.join(os.path.dirname(os.getcwd()), 'DataCollecting', 'chromedriver_win32', 'chromedriver.exe')
    if request.method == 'GET':
        return {"Response": DataOksigen.TampilkanProvinsi()}
    elif request.method == 'POST' and "Kota" in request.get_json() and "Provinsi" in request.get_json():
        ProvinsiOks = request.get_json()["Provinsi"]
        KotaOks = request.get_json()["Kota"]
        return {"Response": DataOksigen.UpdateData(ProvinsiOks, KotaOks, path)}
    elif request.method == 'POST' and "Provinsi" in request.get_json():
        ProvinsiOks = request.get_json()["Provinsi"]
        return {"Response": DataOksigen.TampilkanKabKota(request.get_json()["Provinsi"], path)} 

@app.route('/vaksin', methods=['GET', 'POST'])
def vaksin():
    ProvinsiVak = ""
    KotaVak = ""
    if (sys.platform == "darwin"):
        path = os.path.join(os.path.dirname(os.getcwd()), 'DataCollecting', 'chromedriver_mac64', 'chromedriver')
    elif (sys.platform == "win32"):
        path = os.path.join(os.path.dirname(os.getcwd()), 'DataCollecting', 'chromedriver_win32', 'chromedriver.exe')
    if request.method == 'GET':
        return {"Response": DataVaksin.TampilkanProvinsi()}
    elif request.method == 'POST' and "Kota" in request.get_json() and "Provinsi" in request.get_json():
        ProvinsiOks = request.get_json()["Provinsi"]
        KotaOks = request.get_json()["Kota"]
        return {"Response": DataVaksin.UpdateData(ProvinsiOks, KotaOks,path)}
    elif request.method == 'POST' and "Provinsi" in request.get_json():
        ProvinsiOks = request.get_json()["Provinsi"]
        return {"Response": DataVaksin.TampilkanKabKota(request.get_json()["Provinsi"], path)}


@app.route('/berita', methods=['GET', 'POST'])
def berita():
    if request.method == 'GET':
        return {"Response": DataBerita.TampilkanFeed()}
    elif request.method == 'POST':
        return {"Response" :DataBerita.UpdateData(request.get_json()["Feed"])}

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')