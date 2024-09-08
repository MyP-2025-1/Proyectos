# QR Code Generator

**Author:** @ErickAvila  
**Date:** September, 2024

## Descripción

Este proyecto proporciona una clase para generar códigos QR con una URL y opcionalmente, con una imagen incrustada en el centro del código QR. Incluye un script de terminal para facilitar la generación de códigos QR desde la línea de comandos.

## Dependencias

Se recomienda crear un ambiente virtual. Son indispensables las siguientes bibliotecas de Python:

- `qrcode`: Para la generación de códigos QR.
- `PIL` (Pillow): Para operaciones con imágenes.

Puedes instalar las dependencias usando `pip`:

```bash
pip3 install -r requirements.txt
```

## Generar un Código QR desde la Terminal

Puedes ejecutar el script principal main.py desde la línea de comandos para generar un código QR.

Uso básico:

```bash
python main.py <url> [image_path] [output_name]
```
- \<url\>: La URL que se codificará en el código QR.
- [image_path]: (Opcional) La ruta a una imagen que se incrustará en el centro del código QR.
- [output_name]: (Opcional) El nombre del archivo de salida. Por defecto, se guarda como QRcode.png.

Ejemplo:

```bash
python main.py "https://example.com" "path/to/image.png" "my_qr_code.png"
```

## Contribuciones

Contribuidor: @ErickAvila

Si deseas contribuir a este proyecto, por favor, haz un fork del repositorio y envía un pull request con tus cambios.