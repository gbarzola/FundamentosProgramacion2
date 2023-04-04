'''
class Numero:

  def __init__(self, valor):
    self.valor = valor

  def __cmp__(self, objeto_1):
    if self.valor > objeto_1.valor:
      return 1
    elif self.valor < objeto_1.valor:
      return -1
    else:
      return 0


# Restando objetos
lista = []
num_1 = Numero(5)
num_2 = Numero(10)
num_3 = Numero(20)
num_4 = Numero(10)
num_5 = Numero(20)
num_6 = Numero(10)
num_7 = Numero(20)

compara = num_1.__cmp__(num_2)
print(compara)

compara = num_1 > num_2
print(compara)
'''


class Numero:

  def __init__(self, valor):
    self.valor = valor

  #Devuelve el mayor
  def __cmp__(self, objeto_1):
    if self.valor > objeto_1.valor:
      return Numero(self.valor)
    elif self.valor < objeto_1.valor:
      return Numero(objeto_1.valor)
    else:
      return Numero(self.valor)


# Restando objetos
lista = []
num_1 = Numero(5)
num_2 = Numero(10)
num_3 = Numero(20)
num_4 = Numero(10)
num_5 = Numero(20)
num_6 = Numero(10)
num_7 = Numero(20)

compara = num_1.__cmp__(num_2)
compara2 = compara.__cmp__(num_3)
print(compara2.valor)
