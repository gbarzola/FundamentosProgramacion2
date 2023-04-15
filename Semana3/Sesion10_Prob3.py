class Vehiculo:

  def __init__(self, serie, marca, anio, precio):
    self.serie = serie
    self.marca = marca
    self.anio = anio
    self.precio = precio


class Auto(Vehiculo):

  def __init__(self, serie, marca, anio, precio, num_pasajeros):
    super().__init__(serie, marca, anio, precio)
    self.num_pasajeros = num_pasajeros
    #self.imprimir()

  def imprimir(self):
    print(self.serie, self.marca, self.anio, self.precio, self.num_pasajeros)


class Camioneta(Vehiculo):

  def __init__(self, serie, marca, anio, precio, carga, ejes):
    super().__init__(serie, marca, anio, precio)
    self.carga = carga
    self.ejes = ejes
    #self.imprimir()

  def imprimir(self):
    print(self.serie, self.marca, self.anio, self.precio, self.carga,
          self.ejes)


v1 = Vehiculo("AXWR-45", "Audi", 2022, 40000)
a1 = Auto("AXWR-45", "Audi", 2022, 40000, 5)
c1 = Camioneta("AXWR-45", "Audi", 2022, 40000, "200Kg", 2)

a1.imprimir()
c1.imprimir()