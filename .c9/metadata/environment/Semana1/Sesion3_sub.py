{"filter":false,"title":"Sesion3_sub.py","tooltip":"/Semana1/Sesion3_sub.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["class Numero:","","  def __init__(self, valor):","    self.valor = valor","","  def __sub__(self, objeto_1):","    return Numero(self.valor - objeto_1.valor)","","","# Restando objetos","lista = []","num_1 = Numero(5)","num_2 = Numero(10)","num_3 = Numero(20)","num_4 = Numero(10)","num_5 = Numero(20)","num_6 = Numero(10)","num_7 = Numero(20)","","suma_total = num_1 - num_2 - num_3 - num_4 - num_5 - num_6 - num_7","print(suma_total.valor)","","#Restando objetos:","","lista = []","","lista.append(Numero(5))","lista.append(Numero(10))","lista.append(Numero(20))","lista.append(Numero(10))","#...","resta = lista[0].valor","for i in range(1, len(lista)):","  resta = resta - lista[i].valor","","print(resta)",""],"id":1}]]},"ace":{"folds":[],"scrolltop":88,"scrollleft":0,"selection":{"start":{"row":36,"column":0},"end":{"row":36,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1680584542093,"hash":"2e81137b418ae4bcb03b1d8c0371cb53fab3f434"}