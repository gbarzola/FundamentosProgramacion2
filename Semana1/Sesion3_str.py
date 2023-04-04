# Alumno: codigo, nombre, edad
class Alumno:
  #Inicializar
  def __init__(self, codigo, nombre, edad):
    self.codigo = codigo
    self.nombre = nombre
    self.edad = edad

  #Mostrar valores string
  def __str__(self):
    codigo_string = str(self.codigo)
    edad_string = str(self.edad)
    print("str", codigo_string, type(codigo_string))
    print("str", edad_string, type(edad_string))

  def imprimir(self):
    print("init", self.codigo, type(self.codigo))
    print("init", self.edad, type(self.edad))

alumno_1 = Alumno(20230015, "Fernando", 32)

alumno_1.__str__()
alumno_1.imprimir()
