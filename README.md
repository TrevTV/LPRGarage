# LPR Garage
A python script that detects the owner's license plate then opens a (virtual) garage.<br>
<b>Note: this uses the raspberry pi camera to take pictures</b><br>
<b>Note: DON'T use this in an actual environment, license plates for this can be easily faked.</b><br>
<b>Note: this was made to be used for [GarageAPI](https://github.com/TrevTV/GarageAPI)</b>

## How It Works
The script uses an API to check for license plates in images taken by a camera. Then sends a request to GarageAPI to "open and close" a garage.

## What You'll Need
An API key from [Plate Recognizer](https://platerecognizer.com/)<br>
An instance of GarageAPI. (optional, code for GAPI is currently commented out)<br>
A real license plate OR a printed out image of a fake one. I got mine from [ACME License Maker](https://www.acme.com/licensemaker/)

## How To Use It
Once cloned, open a command prompt and navigate to the folder containing GarageAPI.<br>
Install the dependencies `requests`, `urllib`, `json`, and `picamera` <br>
Modify `Detection.py` so that the variable `licenseNumber` and `apiKey` are correct for you<br>
Run `Detection.py` and the script will do all the work.


![Signature](https://i.ibb.co/c60k2sw/045995e009d085e509c3f8b30012150a.png)
