try:
    def funciona(a,b):
        return print(a ** b) 

    funciona(2,4)
    funciona(4,10)
    funciona(1e10,1e10)
except OverflowError:
    print("parametros invalidos")