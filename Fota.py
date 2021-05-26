from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview()

for i in range(20):
    camera.capture('Bilder/Bild{}.jpg'.format(i))
    sleep(0.5)

camera.stop_preview()
camera.close()
