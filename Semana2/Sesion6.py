class Auto:
    
    def __init__(self,precio):
        self.precio = precio
    
    @staticmethod
    def imprimir ():
        print("Hola")
    
    @staticmethod
    def suma():
        print(5+6)
    
    @staticmethod
    def aumento(x):
        print(x+10)
        
    @staticmethod
    def suma_objetos(objeto1,objeto2):
        precio_nuevo = objeto1.precio + objeto2.precio
        return Auto(precio_nuevo)
    
    @staticmethod
    def ejecuta_todo():
        Auto.imprimir()
        Auto.suma()
        Auto.aumento(10)
        print(Auto.suma_objetos(Auto(100),Auto(200)).precio)
        
'''
auto_1 = Auto(100)
auto_2 = Auto(200)
auto_3 = Auto.suma_objetos(auto_1,auto_2)
print(auto_3.precio)
auto_1.imprimir()
auto_1.suma()
auto_1.aumento(20)
'''
Auto.ejecuta_todo()

