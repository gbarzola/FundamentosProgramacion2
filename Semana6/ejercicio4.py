try:
    nombres =  ['Juan','Pedro','Maria','Ana','Rosario','Humberto']

    def buscarNombres(nombres,n):
        print(nombres[n])

    buscarNombres(nombres,0)
    buscarNombres(nombres,5)
    buscarNombres(nombres,10)
    
except IndexError:
    print("Nombre no encontrado")