

class Calculadora:
    def __init_(self):
        pass

    def get__numero_01(self):
        return self.__numero_01

    def get__numero_02(self):
        return self.get__numero_02

    def setnumero_01(self, num1):
        if str(num1).isnumeric():
            self.__numero_01 = int(num1)
        else:
            ("El valor debe ser un numero")

    def setnumero_02(self, num2):
        if str(num2).isnumeric():
            self.__numero_02 = int(num2)
        else:
            ("El valor debe ser un numero")

    @staticmethod
    def sumar(num1, num2):
        assert (True == isinstance(num1, int) and True ==
                isinstance(num2, int)), "solo ingrese numeros"
        return num1 + num2

    @staticmethod
    def restar(num1, num2):
        assert (True == isinstance(num1, int) and True ==
                isinstance(num2, int)), "solo ingrese numeros"
        return num1 - num2

    @staticmethod
    def multiplicar(num1, num2):
        assert (True == isinstance(num1, int) and True ==
                isinstance(num2, int)), "solo ingrese numeros"
        return num1 * num2

    @staticmethod
    def dividir(num1, num2):
        assert (True == isinstance(num1, int) and True ==
                isinstance(num2, int)), "solo ingrese numeros"
        return num1 / num2

    def imprimir_resultados(self):
        print("sumar", self.sumar(self.__numero_01, self.__numero_02))
        print("resta", self.restar(self.__numero_01, self.__numero_02))
        print("multiplicar", self.multiplicar(
            self.__numero_01, self.__numero_02))
        print("disvision", self.dividir(self.__numero_01, self.__numero_02))


calculadora = Calculadora()
calculadora.setnumero_01("30")
calculadora.setnumero_02("50")
calculadora.imprimir_resultados()
