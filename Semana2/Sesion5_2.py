class Alumno:
  #Constructor
  def __init__(self, nombre):
    self.nombre = nombre

  def imprime(self):
    print(self.__edad)

  @property
  def edad(self):
    return self.__edad

  @edad.setter
  def edad(self, edad):
    self.__edad = edad


alu_1 = Alumno("Luis")
alu_1.edad = 30
print(alu_1.edad)


#print(alu_1.nombre)
#alu_1.imprime()
#print(alu_1.getEdad())
