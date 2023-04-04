class Numero:

  def __init__(self, valor):
    self.valor = valor

  def __add__(self, objeto_1):
    return Numero(self.valor + objeto_1.valor)


# Sumando objetos
num_1 = Numero(5)
num_2 = Numero(10)
num_3 = Numero(20)
num_4 = Numero(10)
num_5 = Numero(20)
num_6 = Numero(10)
num_7 = Numero(20)

suma_total = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7
print(suma_total.valor)