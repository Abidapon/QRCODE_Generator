import qrcode
import image
qrcode = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://github.com/Abidapon"

qrcode.add_data(data)
qrcode.make(fit = True)
img = qrcode.make_image(fill="black", back_color = "white")
img.save("Qr-Code.png")

