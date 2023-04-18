#Clase padre: Figura
#Clase hijo: Cuadrado

from abc import ABC, abstractmethod
#Clase abstracta : 
class Figura(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
        
    @abstractmethod
    def calcular_perimetro(self):
        pass

#Clase hija:
class Cuadrado(Figura):
    
    def __init__(self,lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado*self.lado
        
    def calcular_perimetro(self):
        return 4* self.lado

c1 = Cuadrado(5)
c2 = Cuadrado(10)
#f1 = Figura()

#=====Metodos======
print(c1.calcular_area())
print(c1.calcular_perimetro())
print(c2.calcular_area())
print(c2.calcular_perimetro())
#print(f1.calcular_perimetro())
#print(f1.calcular_area())