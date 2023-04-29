class Trabajador:
    def __init__(self, cod_trabajador, nombre):
        self.cod_trabajador = cod_trabajador
        self.nombre = nombre
    
    def HorasTrabajadas(self):
        pass

class Staff(Trabajador):
    def __init__(self, cod_trabajador, nombre, salario, costo_hora):
        super().__init__(cod_trabajador, nombre)
        self.__salario = salario
        self.__costo_hora = costo_hora
    
    def getTodos(self):
        return self.cod_trabajador, self.nombre, self.__salario, self.__costo_hora
    
    def setTodos(self, cod_trabajador, nombre, salario, costo_hora):
        self.cod_trabajador = cod_trabajador
        self.nombre = nombre
        self.__salario = salario
        self.__costo_hora = costo_hora

    def HorasTrabajadas(self):
        try:
            return self.__salario / self.__costo_hora
        except:
            pass
    
    def Imprimir(self):
        try:
            print(Staff.getTodos(self))
            print(Staff.HorasTrabajadas(self))
            print("Es Staff")
        except:
            pass

class Externo(Trabajador):
    def __init__(self, cod_trabajador, nombre, salario, costo_hora):
        super().__init__(cod_trabajador, nombre)
        self.__salario = salario
        self.__costo_hora = costo_hora

    def getTodos(self):
        return self.cod_trabajador, self.nombre, self.__salario, self.__costo_hora
    
    def setTodos(self, cod_trabajador, nombre, salario, costo_hora):
        self.cod_trabajador = cod_trabajador
        self.nombre = nombre
        self.__salario = salario
        self.__costo_hora = costo_hora
    
    def HorasTrabajadas(self):
        try:
            return self.__salario / self.__costo_hora
        except:
            pass
    
    def Imprimir(self):
        try:
            print(Externo.getTodos(self))
            print(Externo.HorasTrabajadas(self))
            print("Es Externo")
        except:
            pass

S1 = Staff(123456, "Juan Pérez", 4000, 20)
E1 = Externo(654321, "Pedro González", 3000, 18)
S1.Imprimir()
E1.Imprimir()

print("El nuevo sueldo de Juan es: ")
S1.setTodos(123456, "Juan Pérez", 4000, 0)
S1.Imprimir()
