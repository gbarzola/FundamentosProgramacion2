#Ejemplo TypeError:
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

5 + "hola"


#TypeError: unsupported operand type(s) for /: 'int' and 'list'
lista = [5,6,9]
5/lista


#TypeError: suma() takes 2 positional arguments but 6 were given
def suma(num1,num2):
    return num1+num2
    
suma(1,2,3,5,4,7)