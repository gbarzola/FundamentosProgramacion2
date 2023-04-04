#Objeto: Estudiante e1
#Atributos: codigo,nombre,nota_1,nota_2,nota_3
class Estudiante:
  #Inicializado, construido mi formato en blanco
  def __init__(self, cod, nom, n_1, n_2, n_3):
    self.codigo = cod
    self.nombre = nom
    self.nota_1 = n_1
    self.nota_2 = n_2
    self.nota_3 = n_3

  #Funcion de promedio
  def promedio(self):
    return (self.nota_1 + self.nota_2 + self.nota_3) / 3


# Variables:
a = 561321
b = "Fer"
c = 15
d = 14
e = 18

Fernando = Estudiante(a, b, c, d, e)
valor = Fernando.promedio()
print(valor)

#********************************
#Aplicando Clean Code :
'''
class Estudiante:

  def __init__(self, codigo, nombre, nota_1, nota_2, nota_3):
    self.codigo = codigo
    self.nombre = nombre
    self.nota_1 = nota_1
    self.nota_2 = nota_2
    self.nota_3 = nota_3

  def calcular_promedio(self):
    return (self.nota_1 + self.nota_2 + self.nota_3) / 3


codigo_fernando = 561321
nombre_fernando = "Fer"
nota_1_fernando = 15
nota_2_fernando = 14
nota_3_fernando = 18

fernando = Estudiante(codigo_fernando, nombre_fernando, nota_1_fernando,
                      nota_2_fernando, nota_3_fernando)
promedio_fernando = fernando.calcular_promedio()
'''