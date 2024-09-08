"""
App to generate QR Codes
Author: @FernandoFong
Contributors: @ErickAvila
"""


# Dependencies
import qrcode  # Support for QR Codes
from PIL import Image  # Support for images


def open_image(img_path: str) -> Image:
    """
    Open an image from a given path
    Args:
        img_path (str): Path to the image
    Returns:
        Image: Image object
    """
    try:
        img: Image = Image.open(img_path)
        return img
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        raise e


def make_white_background(img: Image) -> Image:
    """
    Make the background of an image white
    Args:
        img (Image): Image object
    Returns:
        Image: Image object
    """
    white_bg: Image = Image.new("RGB", img.size, "white")
    white_bg.paste(img, (0, 0), img)
    return white_bg


def prepare_image(img: Image) -> Image:
    """
    Resize an image to a given width
    Args:
        img (Image): Image object
    Returns:
        Image: Image object
    """
    width: int = 100
    width_percent: float = (width / float(img.size[0]))
    height: int = int((float(img.size[1]) * float(width_percent)))
    img = img.resize((width, height))
    img = make_white_background(img)
    return img


img: Image = open_image("center.png")
img = prepare_image(img)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://www.geeksforgeeks.org/'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'Green'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - img.size[0]) // 2,
       (QRimg.size[1] - img.size[1]) // 2)
QRimg.paste(img, pos)

# save the QR code generated
QRimg.save('gfg_QR.png')

print('QR code generated!')
