{"filter":false,"title":"Sesion2.py","tooltip":"/Semana1/Sesion2.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":50,"column":48},"action":"insert","lines":["#Objeto: Estudiante e1","#Atributos: codigo,nombre,nota_1,nota_2,nota_3","class Estudiante:","  #Inicializado, construido mi formato en blanco","  def __init__(self, cod, nom, n_1, n_2, n_3):","    self.codigo = cod","    self.nombre = nom","    self.nota_1 = n_1","    self.nota_2 = n_2","    self.nota_3 = n_3","","  #Funcion de promedio","  def promedio(self):","    return (self.nota_1 + self.nota_2 + self.nota_3) / 3","","","# Variables:","a = 561321","b = \"Fer\"","c = 15","d = 14","e = 18","","Fernando = Estudiante(a, b, c, d, e)","valor = Fernando.promedio()","","#********************************","#Aplicando Clean Code :","","class Estudiante:","","  def __init__(self, codigo, nombre, nota_1, nota_2, nota_3):","    self.codigo = codigo","    self.nombre = nombre","    self.nota_1 = nota_1","    self.nota_2 = nota_2","    self.nota_3 = nota_3","","  def calcular_promedio(self):","    return (self.nota_1 + self.nota_2 + self.nota_3) / 3","","","codigo_fernando = 561321","nombre_fernando = \"Fer\"","nota_1_fernando = 15","nota_2_fernando = 14","nota_3_fernando = 18","","fernando = Estudiante(codigo_fernando, nombre_fernando, nota_1_fernando,","                      nota_2_fernando, nota_3_fernando)","promedio_fernando = fernando.calcular_promedio()"],"id":1}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["''"],"id":2}],[{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"insert","lines":["'"],"id":3}],[{"start":{"row":50,"column":48},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":3},"action":"insert","lines":["'''"],"id":5}],[{"start":{"row":24,"column":27},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["p"]},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"insert","lines":["r"]},{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"insert","lines":["i"]},{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"insert","lines":["n"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":5},"end":{"row":25,"column":7},"action":"insert","lines":["()"],"id":7}],[{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["v"],"id":8},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["l"]}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":["l"],"id":9}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["a"],"id":10},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["l"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["o"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["r"]}]]},"ace":{"folds":[],"scrolltop":218,"scrollleft":0,"selection":{"start":{"row":25,"column":11},"end":{"row":25,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"state":"start","mode":"ace/mode/python"}},"timestamp":1680584042700,"hash":"b8d2c2411427b5fa4dacd5a47a71029ec8e4a443"}