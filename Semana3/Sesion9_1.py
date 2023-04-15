class Empleado:

  def __init__(self, cod_empl, nombre, num_celular):
    self.__codigo_empleado = cod_empl
    self.__nombre_empleado = nombre
    self.__numero_celular = num_celular

class Directivo(Empleado):

  def __init__(self, cat, area, cod_empl, nombre, num_celular):
    self.__categoria = cat
    self.__area = area
    self.__codigo_empleado = cod_empl
    self.__nombre_empleado = nombre
    self.__numero_celular = num_celular

  def setTodos(self, cat, area):
    self.__categoria = cat
    self.__area = area

  def getTodos(self):
    return self.__categoria, self.__area

  def sueldo_bruto(self):
    if self.__categoria == 0:
      return 22000
    elif self.__categoria == 1:
      return 18000
    else:
      return 16000

  def descuento_sueldo_bruto(self):
    return self.sueldo_bruto() * 0.13

  def sueldo_neto(self):
    return self.sueldo_bruto() - self.descuento_sueldo_bruto()

  def imprimir(self):
    print(self.__codigo_empleado, self.__nombre_empleado,
          self.__numero_celular, self.__categoria, self.__area)


class Asesor(Empleado):

  def __init__(self, num_ase, tar_hora, beaticos, cod_empl, nombre,
               num_celular):
    self.__numero_asesorias = num_ase
    self.__tarifa_asesorias = tar_hora
    self.__beaticos = beaticos
    self.__codigo_empleado = cod_empl
    self.__nombre_empleado = nombre
    self.__numero_celular = num_celular

  def setTodos(self, num_ase, tar_hora, beaticos):
    self.__numero_asesorias = num_ase
    self.__tarifa_asesorias = tar_hora
    self.__beaticos = beaticos

  def getTodos(self):
    return self.__numero_asesorias, self.__tarifa_asesorias, self.__beaticos

  def sueldo_bruto_asesor(self):
    return self.__numero_asesorias * self.__tarifa_asesorias + self.__beaticos

  def descuento_sueldo_bruto_asesor(self):
    return self.sueldo_bruto_asesor() * 0.05

  def sueldo_neto_asesor(self):
    return self.sueldo_bruto_asesor() - self.descuento_sueldo_bruto_asesor()

  def imprimir(self):
    print(self.__codigo_empleado, self.__nombre_empleado,
          self.__numero_celular, self.__numero_asesorias,
          self.__tarifa_asesorias, self.__beaticos)


Empleado2 = Directivo(1, "administracion", "e002", "Jorge", "987654321")
Empleado3 = Asesor(4, 24.8, 150, "e001", "Juan", "999955555")

Empleado2.imprimir()
Empleado3.imprimir()
