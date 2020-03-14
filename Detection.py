import requests
import urllib.request as ul
import json
from picamera import PiCamera

camera = PiCamera()
licenseNumber = "pl4te"
apiKey = "API-KEY-HERE";

def wait_for_internet():
    print("Waiting for internet connection!")
    while True:
        try:
            response = ul.urlopen('https://google.com', timeout=1)
            return
        except ul.URLError:
            pass

def main():
    print("Connection received!")
    while True:
        camera.capture('/home/pi/Desktop/img.jpg')
    
        with open('/home/pi/Desktop/img.jpg', 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                files=dict(upload=fp),
                headers={'Authorization': 'Token ' + apiKey})
        data = response.json()
        try:
            if licenseNumber in str(data["results"]):
                print("Owner car detected! Opening garage")
                # requests.get('https://garageapi-js.herokuapp.com/api/open')
            else:
                print("Car with plate number '" + data["results"][0]["plate"] + "' has been detected")
                # requests.get('https://garageapi-js.herokuapp.com/api/close')
        except IndexError:
            print("No cars detected in image.")
            # requests.get('https://garageapi-js.herokuapp.com/api/close')
        except KeyError:
            print("Error, pass")
            pass
        
wait_for_internet()
main()
