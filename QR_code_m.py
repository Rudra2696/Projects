import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data("Hello")
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white")
img.save("QR_code.png")
