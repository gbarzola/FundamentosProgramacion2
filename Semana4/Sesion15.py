from abc import *
class Figura(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Triangulo(Figura):
    def area(self):
        print("Area del triangulo")

class Cuadrilatero(Figura):
    def area(self):
        print("Area del cuadrilatero")

class TrianguloEquilatero(Triangulo):
    def area(self):
        print("Area del triangulo equilatero")

class TrianguloRectangulo(Triangulo):
    def area(self):
        print("Area del triangulo rectangulo")

class Trapecio(Cuadrilatero):
    def area(self):
        print("Area del trapecio")

class Cuadrado(Cuadrilatero):
    def area(self):
        print("Area del cuadrado")

#Creación de objetos:

t1 = Triangulo()
c1 = Cuadrilatero()
te1 = TrianguloEquilatero()
tr1 = TrianguloRectangulo()
t = Trapecio()
c = Cuadrado()

#Uso de metodos:
t1.area()
c1.area()
te1.area()
tr1.area()
t.area()
c.area()
