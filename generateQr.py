
# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

def main():  
    # String which represents the QR code
    district = input("Enter district : ")
    subdivision = input("Enter subdivision : ")
    stationName = input("Enter station name : ")

    s = "./feedback.html/" + f"search?{district}+{subdivision}+{stationName}"
    url = pyqrcode.create(s)
    url.svg("myqr.svg", scale = 8)
    url.png('myqr.png', scale = 6)

if __name__ == "__main__":
    main()