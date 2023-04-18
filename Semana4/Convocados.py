from abc import ABC, abstractmethod
class Convocados(ABC):
    @abstractmethod
    def viajar(self):
        pass
    @abstractmethod
    def concentrarse(self):
        pass
    @abstractmethod
    def entrenar(self):
        pass
    @abstractmethod
    def jugar(self):
        pass

class Jugador(Convocados):
    def __init__(self, dni, nombre, dorsal, posicion):
        self.dni = dni
        self.nombre = nombre
        self.dorsal = dorsal
        self.posicion = posicion
        
    def viajar(self):
        return print("el lugar de viaje : Lima")
        
    def concentrarse(self):
        return print("Lugar de concentracion : La videna")
        
    def entrenar(self):
        return print("Dias de entrenamiento", 5)
        
    def jugar(self):
        return print("El dia y la fecha de juego: Sabado, 29 de Abril, 2023")
    
    def correr(self):
        return print("velocidad de jugador : 20m/s")
    
    def anotarGoles(self):
        return print("La probabilidad de meter gol", 0.8)
        
    def Imprimir(self):
        print(self.dni, self.nombre, self.dorsal, self.posicion)
        self.viajar()
        self.concentrarse()
        self.entrenar()
        self.jugar()
        self.correr()
        self.anotarGoles()
        
jugador1 = Jugador(75460945, "Marcelo", 7, "Delantero")
jugador1.Imprimir()
        
    
    