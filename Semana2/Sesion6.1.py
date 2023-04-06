class Construccion:
    __cantObjeto = 0
    __montoTotalDolar = 0
    #precio_construccion = self.__costo_dolar * self.__numero_departamento
    
    #constructor inicialize
    def __init__(self, codigo, numDepart, numContrato, costoDolar):
        self.__codigo = codigo
        self.__numero_departamento = numDepart
        self.__numero_contrato = numContrato
        self.__costo_dolar = costoDolar
        Construccion.__cantObjeto += 1
        Construccion.__montoTotalDolar += costoDolar * numDepart
        
    def setTodos(self, codigo, numDepart, numContrato, costoDolar):
        self.__codigo = codigo
        self.__numero_departamento = numDepart
        self.__numero_contrato = numContrato
        self.__costo_dolar = costoDolar 
    
    def getTodos (self):
        return self.__codigo, self.__numero_departamento, self.__numero_contrato, self.__costo_dolar
        
    def imprimir(self):
        print(self.__codigo, self.__numero_departamento, self.__numero_contrato, self.__costo_dolar)
        
    @classmethod
    def cantObjetos(cls):
        return print(cls.__cantObjeto)
    
    @classmethod
    def montoTotalDolar(cls):
        return print(cls.__montoTotalDolar)
    
    @staticmethod
    def monto(numDepart, costoDolar):
        return print(numDepart * costoDolar)
        
depart_1 = Construccion(23045, 17, 12545, 500)
depart_2 = Construccion(45032, 10, 45363, 300)
depart_1.imprimir()
depart_2.imprimir()
depart_1.monto(17, 500)
depart_2.monto(10, 300)
Construccion.cantObjetos()
Construccion.montoTotalDolar()