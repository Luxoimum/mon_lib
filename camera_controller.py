from goprocam import GoProCamera
from goprocam import constants
from PIL import Image
from io import BytesIO
import requests
import time
# Script para sacar periodicamente una foto con una camara(gopro hero 3+) y guardarla en un servidor.
for x in range(3):
    print("Conectando con la cámara")
    gpCam = GoProCamera.GoPro(constants.auth)
    print("repetición => " + str(x))
    img_url = gpCam.getMedia()
    print(img_url)
    img_url = img_url[:-5] + str(int(img_url[-5])+1) + img_url[-4:]
    img_name = img_url.split("/")[-1]
    print("Tomando foto")
    gpCam.shutter(constants.start)
    time.sleep(2)
    print("Obteniendo uri de la foto")
    print(img_url)
    print("Obteniendo foto")
    print(img_name)
    response = requests.get(img_url)
    print("Escribiendo el fichero")
    img = Image.open(BytesIO(response.content))
    img.save(img_name)
    print("Foto guardada con éxito: " + img_name)
    time.sleep(10)

print("Conectando con la cámara para apagarla")
gpCam = GoProCamera.GoPro(constants.auth)
gpCam.power_off()