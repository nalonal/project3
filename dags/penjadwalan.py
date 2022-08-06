import requests,json
from datetime import datetime
import datetime as dt
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


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

def panggilsuhu():
    daftar_kota = ["Bali","Lombok","Labuan Bajo","Bogor","Bandung"]
    for kota in daftar_kota:
        print(getdata(kota))

default_args = {
    'start_date': dt.datetime(2022, 8, 1, 10, 00, 00),
}

with DAG('penjadwalan',default_args=default_args,schedule_interval='*/2 * * * *') as dag:
    opr_suhu = PythonOperator(task_id='dapat_suhu',python_callable=panggilsuhu)
    
opr_suhu