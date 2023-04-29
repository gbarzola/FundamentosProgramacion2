from openpyxl import Workbook

libro_excel = Workbook()

hoja_excel = libro_excel.active

try:
    hoja_excel['A1'] = "Tv"
    hoja_excel['A2'] = "Radio"
    hoja_excel['A3'] = "Refrigeradora"
    hoja_excel['A4'] = "Lavadora"
except:
    pass

libro_excel.save("Ejemplo2.xlsx")