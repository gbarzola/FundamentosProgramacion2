{"filter":false,"title":"Sesion3_str.py","tooltip":"/Semana1/Sesion3_str.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["# Alumno: codigo, nombre, edad","class Alumno:","  #Inicializar","  def __init__(self, codigo, nombre, edad):","    self.codigo = codigo","    self.nombre = nombre","    self.edad = edad","","  #Mostrar valores string","  def __str__(self):","    codigo_string = str(self.codigo)","    edad_string = str(self.edad)","    print(\"str\", codigo_string, type(codigo_string))","    print(\"str\", edad_string, type(edad_string))","","  def imprimir(self):","    print(\"init\", self.codigo, type(self.codigo))","    print(\"init\", self.edad, type(self.edad))","","alumno_1 = Alumno(20230015, \"Fernando\", 32)","","alumno_1.__str__()","alumno_1.imprimir()",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":0},"end":{"row":23,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1680584546593,"hash":"773a2412f3ff09bae608c046bf4ee4639dbfacec"}