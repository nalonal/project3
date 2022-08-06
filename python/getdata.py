import requests,json
from datetime import datetime

daftar_kota = ["Bali","Lombok","Labuan Bajo","Bogor","Bandung"]

def getdata(namakota):
    hasil = requests.post("https://api.openweathermap.org/data/2.5/weather?q="+namakota+"&appid=d5f11f21e3d4617bc66950d463fdeb4b")
    output = hasil.json() 
    ini_hasil = {}

    #mengambil waktu sekarang
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    st = datetime.fromtimestamp(ts)
    waktu = st.isoformat(timespec='microseconds')

    #sesuaikan bagian ini
    ini_hasil['kota'] = namakota
    ini_hasil['cuaca'] = output["weather"][0]["main"]
    ini_hasil['cuaca_deskripsi'] = output["weather"][0]["description"]
    ini_hasil['temperatur'] = output['main']['temp']
    ini_hasil["waktu"] = waktu
    #end sesuaikan
    return ini_hasil

for kota in daftar_kota:
    print(getdata(kota))

