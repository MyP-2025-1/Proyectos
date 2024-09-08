"""
App to generate QR Codes
Author: @FernandoFong
Contributors: @ErickAvila
"""


# Dependencies
import qrcode  # Support for QR Codes
from PIL import Image  # Support for image operations
import sys  # Support for system operations


def open_image(img_path: str) -> Image:
    """
    Open an image from a given path
    Args:
        img_path (str): Path to the image
    Returns:
        Image: Image object
    Raises:
        FileNotFoundError: If the file is not found
        Exception: If an error occurs
    """
    try:
        img: Image = Image.open(img_path)
        return img
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


def generate_QR_code(url: str, img_path: str = None) -> Image:
    """
    Generate a QR Code with a given URL and an optional image
    Args:
        url (str): URL to encode
        img_path (str): Path to the image
    Returns:
        Image: QR Code image
    """
    QR_code: qrcode = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    QR_code.add_data(url)
    QR_code.make(fit=True)
    QR_img: Image = QR_code.make_image().convert("RGB")
    if img_path:
        img: Image = open_image(img_path)
        img = prepare_image(img)
        position: tuple = ((QR_img.size[0] - img.size[0]) //
                           2, (QR_img.size[1] - img.size[1]) // 2)
        QR_img.paste(img, position)
    return QR_img


def main():
    """
    Main function to run the QR Code generator from terminal
    """
    if len(sys.argv) < 2:
        print("Uso: python main.py <url> [image_path] [output_name]")
        sys.exit(1)

    url: str = sys.argv[1]
    img_path: str = sys.argv[2] if len(sys.argv) > 2 else None
    output_name: str = sys.argv[3] if len(sys.argv) > 3 else "qr_code.png"

    try:
        qr_img: Image = generate_QR_code(url, img_path)
        qr_img.save(output_name)  # Save the QR Code image
        print(f"Código QR generado y guardado como '{output_name}'")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
