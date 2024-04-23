from openpyxl import Workbook
from datetime import datetime
import calendar
import openpyxl
import time

# Diccionario para mapear nombres de meses en inglés a español
meses_espanol = {
    "January": "enero",
    "February": "febrero",
    "March": "marzo",
    "April": "abril",
    "May": "mayo",
    "June": "junio",
    "July": "julio",
    "August": "agosto",
    "September": "septiembre",
    "October": "octubre",
    "November": "noviembre",
    "December": "diciembre"
}



def escribir_en_excel(nombre):
    # Abre el archivo Excel o crea uno nuevo si no existe
    try:
        workbook = openpyxl.load_workbook("nombres_decodificados.xlsx")
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Encuentra la última columna utilizada en la hoja de cálculo
    last_column = sheet.max_column
    
    # Calcula la próxima columna disponible para escribir el nombre
    next_column = last_column + 1
    
    # Escribe el nombre decodificado en la próxima columna y la fecha y hora actual en la siguiente columna
    sheet.cell(row=1, column=next_column, value=nombre)
    #sheet.cell(row=1, column=next_column+1, value=time.strftime("%Y-%m-%d %H:%M:%S"))
    
    # Guarda los cambios en el archivo Excel
    workbook.save("nombres_decodificados.xlsx")

# Ejemplo de uso
nombre_decodificado = "Ejemplo"
escribir_en_excel(nombre_decodificado)
