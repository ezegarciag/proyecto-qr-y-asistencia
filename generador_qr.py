import qrcode


# Texto que quieres codificar en el código QR
nombre_completo = "Ezequiel Garcia Genga"

# Genera el código QR y guárdalo en un archivo
img = qrcode.make(nombre_completo)
img.save("codigo_qr.png")
