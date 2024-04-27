import tkinter as tk
from tkinter import ttk
import qrcode

def generar_qr():
    nombre_completo = nombre_entry.get()
    img = qrcode.make(nombre_completo)
    img.save(f"{nombre_completo}.png")
    resultado_label.config(text="¡Código QR generado!")

# Crear ventana
root = tk.Tk()
root.title("Generador de Código QR")

# Crear y colocar etiquetas y entrada
nombre_label = ttk.Label(root, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

nombre_entry = ttk.Entry(root, width=30)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

# Botón para generar QR
generar_button = ttk.Button(root, text="Generar QR", command=generar_qr)
generar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar resultado
resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
