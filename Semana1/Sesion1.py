#Nombre de clases:

class estudiante:
  pass
  
#Uso de la clase:

#Objetos
#algoritmo_tipo_1 = algoritmos()
jorge = estudiante()
eduardo = estudiante()
pedro = estudiante()

#Atributos = datos describen a un objeto
jorge.nota_final = 15
jorge.edad = 20
eduardo.nota_final = 18
eduardo.edad = 20
pedro.nota_final = 19
pedro.edad = 20

#plantilla de datos
class utiles_escolares:
  pass
  
lapiz = utiles_escolares()

lapiz.longitud=5
lapiz.material="madera"
lapiz.anio_fabricacion=2015

if lapiz.longitud > 10:
  print("Exito")
else:
  print("Fracaso")
