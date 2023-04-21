from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def Perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Triangulo(Figura):

    def __init__(self, lado01, lado02, lado03):
        self.lado01 = lado01
        self.lado02 = lado02
        self.lado03 = lado03

    def Perimetro(self):
        return self.lado01 + self.lado02 + self.lado03

    def area(self):
        P = (self.lado01 + self.lado02 + self.lado03)/2
        A = (P*(P - self.lado01)*(P - self.lado02)*(P - self.lado03))**0.5
        return A


class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def Perimetro(self):
        pi = 3.14
        return 2*pi*self.radio
        
    def area(self):
        pi = 3.14
        A = 2*pi*(self.radio**2)
        return A


def Imprimir(dato):
    if isinstance(dato,Triangulo):
        print(f"los lados del Triangulo seleccionados son: {dato.lado01}, {dato.lado02}, {dato.lado03}")
        print(f"El area del triangulo es: {dato.area()}")
        print(f"El perimetro del triangulo es: {dato.Perimetro()}")
    elif isinstance(dato,Circulo):
        print(f"los radio seleccionado del circulo es: {dato.radio}")
        print(f"El area del circulo es: {dato.area()}")
        print(f"El permitro del ciruclo es: {dato.Perimetro()}")


lado1 = int(input("Ingrese el lado1: "))
lado2 = int(input("Ingrese el lado2: "))
lado3 = int(input("Ingrese el lado3: "))
radio = int(input("Ingrese el radio: "))

Triangulo1 = Triangulo(lado1,lado2, lado3)
Circulo1 = Circulo(radio)

Imprimir(Triangulo1)
Imprimir(Circulo1)




