class Alumno:
  #Constructor
  def __init__(self, nombre):
    self.nombre = nombre

  def imprime(self):
    print(self.__edad)

  def getEdad(self):
    return self.__edad

  def setEdad(self, edad):
    self.__edad = edad


alu_1 = Alumno("Luis")
alu_1.setEdad(30)

print(alu_1.nombre)
alu_1.imprime()
print(alu_1.getEdad())