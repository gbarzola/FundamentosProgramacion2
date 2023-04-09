class Telefono:
    __cantidad_objetos = 0
    __total_a_pagar = 0

    def __init__(self, numero, usuario, minutos_consumidos, precio):
        self.__numero = numero
        self.__usuario = usuario
        self.__precio = precio
        self.__minutos_consumidos = minutos_consumidos
        Telefono.__cantidad_objetos += 1
        costo_consumo = self.__precio * self.__minutos_consumidos
        Telefono.__total_a_pagar += costo_consumo + costo_consumo * 0.18
    
    def get_todos(self):
        return self.__numero, self.__usuario, self.__precio, self.__minutos_consumidos
    
    def set_todos(self, numero, usuario, minutos_consumidos, precio):
        self.__numero = numero
        self.__usuario = usuario
        self.__precio = precio
        self.__minutos_consumidos = minutos_consumidos
    
    def imprimir(self):
        print(self.__numero,self.__usuario,self.__precio,self.__minutos_consumidos)
    
    @classmethod
    def total_a_pagar_objetos(cls):
        print(cls.__total_a_pagar)
    
    @classmethod
    def cantidad_objetos(cls):
        print(cls.__cantidad_objetos)
    
    @staticmethod
    def calcular_costo_consumo(minutos_consumidos, precio):
        return print(minutos_consumidos * precio)

    @staticmethod
    def igv(minutos_consumidos, precio):
        return print(minutos_consumidos * precio * 0.18)
    
    @staticmethod
    def total_a_pagar(minutos_consumidos, precio):
        return print(minutos_consumidos * precio * 1.18)
    
    

telefono_1 = Telefono(98652247,"Manuel",50,600)
telefono_2 = Telefono(98651147,"Walter",30,400)
telefono_3 = Telefono(97752247,"Jorge",90,300)
telefono_1.imprimir()
telefono_2.imprimir()
telefono_3.imprimir()
Telefono.total_a_pagar_objetos()
Telefono.cantidad_objetos()