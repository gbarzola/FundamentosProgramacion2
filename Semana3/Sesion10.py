class Padre_1:

  def __init__(self, apellido_1):
    self.apellido_1 = apellido_1

  def mensaje_1(self):
    print("Msj padre 1")


class Padre_2:

  def __init__(self, apellido_2):
    self.apellido_2 = apellido_2

  def mensaje_2(self):
    print("Msj padre 2")


class Hijo(Padre_1, Padre_2):

  def __init__(self, apellido_1, apellido_2):
    super().__init__(apellido_1)
    self.apellido_2 = apellido_2

  def mensaje_familia(self):
    super().mensaje_1()
    super().mensaje_2()
    print("Saludo del hijo/a")


h1 = Hijo("Salas", "Soto")
print(h1.apellido_1)
print(h1.apellido_2)
h1.mensaje_familia()
