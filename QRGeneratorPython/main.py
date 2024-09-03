import qrcode

if __name__ == '__main__':
    name = input("Escriba el nombre para generar su QR Code:")
    img = qrcode.make("https://web.fciencias.unam.mx")
    img.save(f"{name}.png")