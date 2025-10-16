import qrcode
from PIL import image

qr = qrcode.QRCode(version = 2,
               error_correction = qrcode.ERROR_CORRECT_H,
               box_size=10, border=4)

qr.add_data("")     # You can give here the links or data which you want to have in your QR code.
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("")    # Give here the name by which the qrcode file will be saved.