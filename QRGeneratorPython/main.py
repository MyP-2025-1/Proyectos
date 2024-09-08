"""
App to generate QR Codes
Author: @FernandoFong
Contributors: @ErickAvila
"""

# Dependencies
import qrcode  # Support for QR Codes
from PIL import Image  # Support for images

img_path: str = "center.png"
img: Image = Image.open(img_path)

width: int = 100
width_percent: float = (width / float(img.size[0]))
height: int = int((float(img.size[1]) * float(width_percent)))
img = img.resize((width, height))
QR_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

url: str = "https://web.fciencias.unam.mx"

QR_code.add_data(url)

QR_code.make(fit=True)

QR_img = QR_code.make_image(fill_color="black", back_color="white").convert("RGBA")

position: tuple = ((QR_img.size[0] - img.size[0]) // 2, (QR_img.size[1] - img.size[1]) // 2)
QR_img.paste(img, position)
QR_img.save("QR_code.png")

# if __name__ == '__main__':
#     name = input("Escriba el nombre para generar su QR Code:")
#     img = qrcode.make("https://web.fciencias.unam.mx")
#     img.save(f"{name}.png")
