class A:

  def __init__(self):
    self.apellido_1 = "Salas"

  def mensaje_1(self):
    print("Msj padre 1")


class B:

  def __init__(self):
    self.apellido_2 = "Soto"

  def mensaje_2(self):
    print("Msj padre 2")


class Hijo(B, A):

  def __init__(self):
    super().__init__()


h1 = Hijo()
print(h1.apellido_2)
print(h1.apellido_1)

h1.mensaje_1()
h1.mensaje_2()
