from openpyxl import *
from random import *

libro_excel = Workbook()

hoja_excel = libro_excel.active

try:
    hoja_excel['A1'] = "product_id"
    hoja_excel['B1'] = "product_name"
    hoja_excel['C1'] = "qty"
    hoja_excel['D1'] = "price"

    hoja_excel.append(['p01', 'arroz', 2, 3.5])
    hoja_excel.append(['p01', 'arroz', 1, 3.5])
    hoja_excel.append(['p01', 'arroz', 3, 3.5])
    hoja_excel.append(['p02', 'azucar', 4, 4.1])
    hoja_excel.append(['p03', 'aceite', 2, 8.6])
    hoja_excel.append(['p04', 'leche', 1, 3.7])

except:
    pass

libro_excel.save('nuevo_libro.xlsx')

