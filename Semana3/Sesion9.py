#Clase padre
class Persona:

  def __init__(self, nombre, apellido, dni, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.edad = edad

  def imprimir_mensaje_bienvenida(self):
    print("Bienvenido")

  def identifica_adulto(self):
    if self.edad >= 18:
      print("Eres adulto")
    else:
      print("No eres adulto")

  '''
  def cumpleaños(self):
    if hoy() == date():
      self.edad += 1
  '''


#Clase hijo
class Estudiante(Persona):

  def __init__(self, nombre, apellido, dni, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.edad = edad

  def curso(self):
    print("Principios de algoritmos")


estudiante_1 = Estudiante("luis", "salas", 70445186, 20)
estudiante_1.imprimir_mensaje_bienvenida()
estudiante_1.curso()
estudiante_1.identifica_adulto()
