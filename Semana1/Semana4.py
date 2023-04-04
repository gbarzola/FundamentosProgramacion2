class Numero:

  def __init__(self, valor):
    self.valor = valor
    #Llamado a otros metodos:
    self.__str__()
    self.__add__(10)
    self.__sub__(10)
    self.__mul__(10)
    self.promedio()
    self.__str__()

  def __add__(self, elemento):
    return print("Suma : ", self.valor + elemento)

  def __sub__(self, elemento):
    return print(self.valor - elemento)

  def __mul__(self, elemento):
    self.valor = 20
    self.__add__(20)
    return print("Multiplicación : ", self.valor * elemento)

  def __str__(self):
    return print(f'Valor : {self.valor}')

  def promedio(self):
    return print((10 + self.valor) / 2)


#Llamar:

num_1 = Numero(5)
num_2 = Numero(10)
num_3 = Numero(15)
