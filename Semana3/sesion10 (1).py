class Poligono:

  def __init__(self, nombre):
    self.__nombre = nombre

  def Imprimir_poligono(self):
    print(self.__nombre)


class Cuadrilatero(Poligono):

  def __init__(self, nombre, lados, lados_iguales):
    #super().__init__(nombre)
    #super().setNombre(nombre)
    self.__nombre = nombre
    self.__lados = lados
    self.__lados_iguales = lados_iguales

  def Imprimir_cuadrilatero(self):
    print(self.__nombre)
    print(self.__lados)
    print(self.__lados_iguales)


class Cuadrado(Cuadrilatero):

  def __init__(self, nombre, lados, lados_iguales, tipo, largo):
    #super().__init__(nombre, lados, lados_iguales)
    self.__nombre = nombre
    self.__lados = lados
    self.__lados_iguales = lados_iguales
    self.__tipo = tipo
    self.__largo = largo

  def getNombre(self):
    return self.__nombre

  def setNombre(self, nombre):
    self.__nombre = nombre

  def getLados(self):
    return self.__lados

  def setLados(self, lados):
    self.__lados = lados

  def getLadosIguales(self):
    return self.__lados_iguales

  def setLadosIguales(self, lados_iguales):
    self.__lados_iguales = lados_iguales

  def getLargo(self):
    return self.__largo

  def setLargo(self, largo):
    self.__largo = largo

  def getTipo(self):
    return self.__tipo

  def setTipo(self, tipo):
    self.__tipo = tipo

  def Area(self):
    return print(self.__largo**2)

  def Perimetro(self):
    return print(self.__largo * 4)

  def Imprimir(self):
    print(self.__nombre)
    #print(super().__nombre)
    print(self.__lados)
    print(self.__lados_iguales)
    print(self.__tipo)
    print(self.__largo)


poligono1 = Poligono("Poligono")
poligono1.Imprimir_poligono()
cuadrilatero = Cuadrilatero("cuadrado 3D", 4, 4)
cuadrilatero.Imprimir_cuadrilatero()
cuadrado1 = Cuadrado("cuadrado 2D", 4, 4, "cuadrado", 15)
cuadrado1.Imprimir()
cuadrado1.Area()
cuadrado1.Perimetro()
cuadrado1.setLargo(20)
cuadrado1.Imprimir()
cuadrado1.Area()
cuadrado1.Perimetro()
cuadrado1.setLados(10)
cuadrado1.Imprimir()