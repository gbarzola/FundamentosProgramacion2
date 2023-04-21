from abc import ABC, abstractmethod


class Figura(ABC):

  @abstractmethod
  def area(self):
    pass


class Triangulo(Figura):

  def area(self):
    print("Area triangulo")


class Cuadrado(Figura):

  def area(self):
    print("Area cuadrado")


t1 = Triangulo()
c1 = Cuadrado()
t1.area()
c1.area()
