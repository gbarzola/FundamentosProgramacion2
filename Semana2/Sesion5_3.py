class Alumno:
  #Variables
  nombre = "Jorge"
  edad = 30
  cantidad = 0

  def __init__(self):
    Alumno.cantidad = Alumno.cantidad + 1

  @classmethod
  def imprime(cls):
    print(f'La clase se llamo : {cls.cantidad} veces')


alu_1 = Alumno()
alu_2 = Alumno()
alu_3 = Alumno()

Alumno.imprime()
