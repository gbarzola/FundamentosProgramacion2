class Persona:

    def __init__(self):

        self.__dni = input("Ingresa tu dni: ")
        self.__nombre = input("Ingresa tu nombre: ")
        self.__apellido_paterno = input("Ingresa tu primer apellido: ")
        self.__apellido_materno = input("Ingresa tu segundo apellido: ")


    '''
    def setTodos(self):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido_paterno = apel_pat
        self.__apellido_materno = apel_mat
    '''
    def getTodos(self):
        return self.__dni, self.__nombre, self.__apellido_paterno, self.__apellido_materno


    def Imprimir(self):
        try:
            print("Datos de Persona")
            print(f"Documento de identidad: {self.__dni}")
            print(f"Nombre completo: {self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}")
        except:
            pass


class Docente(Persona):

    valor = ""
    universidad = []

    def __init__(self):
        super().__init__()
        self.grado_academico = input("Ingrese grado academico: ")

        while Docente.valor != "n":
            Docente.valor = input("Ingresa la universidad, caso contrario coloca n")
            if Docente.valor != "n":
                Docente.universidad.append(Docente.valor)


        self.universidades = Docente.universidad


    def Imprimir(self):
        try:
            super().Imprimir()
            print(self.grado_academico, self.universidades)
        except:
            pass

d1 = Docente()

d1.Imprimir()










