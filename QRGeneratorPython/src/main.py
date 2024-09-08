"""
App to generate QR Codes
Author: @FernandoFong
Contributors: @ErickAvila
"""

import sys  # Support for system operations
from QRGenerator import QRGenerator  # QR Code generator class


def main():
    """
    Main function to run the QR Code generator from terminal
    """
    if len(sys.argv) < 2:
        print("Uso: python main.py <url> [image_path] [output_name]")
        sys.exit(1)

    url: str = sys.argv[1]
    img_path: str = sys.argv[2] if len(sys.argv) > 2 else None
    output_name: str = sys.argv[3] if len(sys.argv) > 3 else "QRcode.png"

    try:
        qr: QRGenerator = QRGenerator(url, img_path)
        qr.save(output_name)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
