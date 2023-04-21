from abc import ABC, abstractmethod


class Instrumento(ABC):

    @abstractmethod
    def tipoDeSonido(self):
        pass
    
    @abstractmethod
    def imprimir(self):
        pass


class InstrumentoCuerda(Instrumento):
    
    def __init__(self, excitacion, marca, costo):
        self.excitacion = excitacion
        self.marca = marca
        self.costo = costo
    

    def tipoDeSonido(self, parametro):
        if parametro == 1:
            print("Indica que el sonido se obtiene frotando las cuerdas con un arco")
        elif parametro == 2:
            print("El sonido se obtiene tocando las cuerdas con los dedos")
        elif parametro == 3:
            print("El sonido se obtiene golpeando las cuerdas como el piano")
        else:
            print("NO TE DI ESAS OPCIONES!!!")
    
    
    def imprimir(self):
        print(self.excitacion, self.marca, self.costo)
        
class InstrumentoPercusion(Instrumento):
    def __init__(self, marca, costo):
        self.marca = marca
        self.costo = costo
    
    def tipoDeSonido(self, parametro):
        if parametro == 1:
            print("El sonido se genera mediante la percusión con una varilla o baqueta")
        elif parametro == 2:
            print("El sonido se genera agitando repetidamente el instrumento")
        elif parametro == 3:
            print("El sonido se genera al chocar dos piezas iguales")
        elif parametro == 4:
            print("El sonido se genera al frotar la rugosidad de su superficie")
        elif parametro == 5:
            print("El sonido se genera por la vibración de una lámina")
        else:
            print("NO TE DI ESAS OPCIONES!!!")
    
    def imprimir(self):
        print(self.marca, self.costo)
        
C1 = InstrumentoCuerda("Alto", "Ibanez", 500)
P1 = InstrumentoPercusion("Yamaha", 800)
C1.imprimir()
P1.imprimir()
