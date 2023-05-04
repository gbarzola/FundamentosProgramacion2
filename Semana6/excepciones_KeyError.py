#KeyError: 'pera'
try:
    frutas = {"manzana":2,"platano":5,"naranja":6}
    print(frutas["pera"])
    
except KeyError:
    print("la llave no existe")