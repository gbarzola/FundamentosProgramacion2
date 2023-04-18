from abc import ABC, abstractmethod
class persona:
    def __init__(self,nombre, apellido,edad, estado_civil):
        self.nombre =nombre
        self.apellido =apellido
        self.edad = edad
        self.estadoc=estado_civil
class legislador(ABC): 
    @abstractmethod
    def representar(self):
        pass
    @abstractmethod
    def coordinar(self):
        pass
class congresista(persona, legislador):
    def __init__(self, nombre, apellido, edad, estado_civil, provincia, partido, ndespacho):
        super().__init__(nombre, apellido, edad, estado_civil)
        self.provincia = provincia
        self.partido = partido
        self.ndespacho = ndespacho
    def representar(self):
        return "representa al departamente de lima"
    def coordinar(self):
        return "coordina con su bancada y otros congresistas"
    def imprimir(self):
        print("el nombre",self.nombre)
        print("el apellido",self.apellido)
        print("la edad",self.edad)
        print("el estado civil",self.estadoc)
        print("la provincia",self.provincia)
        print("el partido",self.partido)
        print("el numero de despacho",self.ndespacho)
        print("el representante es",self.representar())
        print("el coordinar",self.coordinar())

c1 = congresista("raul","cardenas",25,"casdo", "iqutos","apra",4)
c1.imprimir()
