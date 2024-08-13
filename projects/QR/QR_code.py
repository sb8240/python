import qrcode
from PIL import Image
import cv2


qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,border=4)

qr.add_data("HELLO PYHTON")
qr.make(fit=True)
img = qr.make_image(fill_color="green",back_color="black")
img.save("h.png")

d = cv2.QRCodeDetector()
v, p, st = d.detectAndDecode(cv2.imread("h.png"))
print(v)
