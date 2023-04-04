class Alumno:
  #Constructor
  def __init__(self, nombre, edad):
    self.nombre = nombre
    #Atributo privado
    self.__edad = edad

  def imprime(self):
    print(self.__edad)

  def getEdad(self):
    return self.__edad

  def setEdad(self, edad):
    self.__edad = edad


alu_1 = Alumno("Luis", 30)

print(alu_1.nombre)
#print(alu_1.__edad)
#print(alu_1.edad)
alu_1.imprime()
