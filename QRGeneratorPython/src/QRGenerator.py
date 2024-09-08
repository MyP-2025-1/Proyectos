"""
Class of functions to generate QR codes
Author: @ErickAvila
Date: September, 2024
"""

# Dependencies
import qrcode  # Support for QR Codes
from PIL import Image  # Support for image operations


class QRGenerator:
    """
    A class to generate QR Codes with optional embedded images
    """

    def __init__(self, url: str, img_path: str = None):
        """
        Initializes the QRCodeGenerator class with URL and optional image path
        Args:
            url (str): URL to encode in the QR Code
            img_path (str): Path to the image to embed in the QR Code (default: None)
        """
        self.__url = url
        self.__img_path = img_path

    def __make_white_background(self, img: Image) -> Image:
        """
        Make the background of an image white
        Args:
            img (Image): Image object
        Returns:
            Image: Image object with a white background
        """
        white_bg: Image = Image.new("RGB", img.size, "white")
        white_bg.paste(img, (0, 0), img)
        return white_bg

    def __prepare_image(self, img: Image) -> Image:
        """
        Resize an image to fit in the center of a QR code
        Args:
            img (Image): Image object
        Returns:
            Image: Resized Image object
        """
        width: int = 100
        width_percent: float = (width / float(img.size[0]))
        height: int = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((width, height))
        img = self.__make_white_background(img)
        return img

    def __generate(self) -> Image:
        """
        Generate a QR Code with a given URL and an optional image in the center
        Returns:
            Image: QR Code image with optional embedded image
        """
        qr: qrcode.QRCode = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )
        qr.add_data(self.__url)
        qr.make(fit=True)
        QR_img: Image = qr.make_image().convert("RGB")
        if self.__img_path:
            img: Image = Image.open(self.__img_path)
            img = self.__prepare_image(img)
            position: tuple = ((QR_img.size[0] - img.size[0]) //
                               2, (QR_img.size[1] - img.size[1]) // 2)
            QR_img.paste(img, position)
        return QR_img

    def save(self, output_name: str = "QRcode.png"):
        """
        Save the generated QR code to a file
        Args:
            output_name (str): The name of the output file (default: 'qr_code.png')
        """
        qr_img = self.__generate()
        qr_img.save(output_name)
        print(f"Código QR guardado como '{output_name}'")
