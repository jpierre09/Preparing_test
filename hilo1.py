import threading
import requests

def descargar_url(url):
    response = requests.get(url)
    print(f"Descargado {url}: {len(response.content)} bytes")

urls = [
    "https://geoportal.siata.gov.co/geoapi/Geograph/geographJson/1/pm25/103/",
    "https://geoportal.siata.gov.co/geoapi/Geograph/geographJson/1/pm25/87/"
]

hilos = []
for url in urls:
    hilo = threading.Thread(target=descargar_url, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

print("Todas las descargas completadas")