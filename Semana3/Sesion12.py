class EquipoElectronico:
    def __init__(self,num_serie,fabricante,modelo,color):
        self.num_serie = num_serie
        self.fabricante = fabricante
        self.modelo = modelo
        self.color = color

class Televisor(EquipoElectronico):
    def __init__(self,num_serie,fabricante,modelo,color,tamanio,resolucion,tecnologia,conexion_bluetooth,entradas_USB,control_remoto):
        super().__init__(num_serie,fabricante,modelo,color)
        self.tamanio = tamanio
        self.__resolucion = resolucion
        self.tecnologia = tecnologia
        self.conexion_bluetooth = conexion_bluetooth
        self.entradas_USB = entradas_USB
        self.control_remoto = control_remoto
    
    def getResolucion(self):
        return self.__resolucion
        
    def setResolucion(self,resolucion):
        self.__resolucion = resolucion
    
    def costo(self):
        if self.tamanio == 43:
            return print(1500)
        elif self.tamanio == 55:
            return print(1900)
        elif self.tamanio == 65:
            return print(2500)
        else:
            return print("No tiene precio en el catalogo")
    
    def imprimir(self):
        return print(self.num_serie,self.fabricante, self.modelo, self.color, self.tamanio,self.__resolucion, self.tecnologia, self.conexion_bluetooth, self.entradas_USB, self.control_remoto)
            
    
class EquipoSonido(EquipoElectronico):
    def __init__(self,num_serie,fabricante,modelo,color,radio,alto,control_remoto,entrada_HDMI,num_parlantes):
        super().__init__(num_serie,fabricante,modelo,color)
        self.radio = radio
        self.alto = alto
        self.control_remoto = control_remoto
        self.entrada_HDMI = entrada_HDMI
        self.num_parlantes = num_parlantes
    
    def imprimir(self):
        return print(self.num_serie,self.fabricante, self.modelo, self.color,self.radio,self.alto,self.control_remoto,self.entrada_HDMI,self.num_parlantes)
    

tv1 = Televisor("121","LG","4K","Negro",55,"Alta","LED","Si","Si","Si")
tv1.imprimir()
tv1.costo()
tv1.setResolucion("Baja")
tv1.imprimir()

radio = EquipoSonido("100","Radioshack","Plus ultra","Blanco","Si",10,"Si","Si",8)
radio.imprimir()
    