class Alumno:
  #Variables
  nombre = "Jorge"
  edad = 30
  cantidad = 0

  def __init__(self, nombre, edad):
    Alumno.cantidad = Alumno.cantidad + 1
    self.nombre = nombre
    self.edad = edad

  @classmethod
  def imprime(cls):
    print(f'La clase se llamo : {cls.cantidad} veces')

  def imprime_alumno(self):
    print(f'Alumno: {self.nombre} tiene {self.edad} ')

  def __add__(self, otro_objeto):
    return Alumno("Alumnos", self.edad + otro_objeto.edad)


alu_1 = Alumno("Manuel", 30)
alu_2 = Alumno("Edgar", 25)
alu_3 = Alumno("Carlos", 19)
Alumno.imprime()
alu_1.imprime_alumno()
alu_2.imprime_alumno()
alu_3.imprime_alumno()

suma = alu_1 + alu_2 + alu_3
print(f'La suma de edades del los alumnos es : {suma.edad}')
