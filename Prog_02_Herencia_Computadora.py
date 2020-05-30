#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Herencia Computadora

#Diagrama

# Clase Computadora : mem, dd, pro, mon
# Clase Escritorio  : gabinete, todo en uno
# Clase LapTop      : tipo, dos en uno(laptop y tablet)
# Gamer             : diadema, tarjeta gráfica, controles, tipo controles, vel. monitor
# Trabajo           : Conexiones USB, Entrada red alámbrica, salida video (HDMI, VGA, DP)

#----CLASES----

from Prog_00_Pide_valor import PideValor

class Computadora():

    def __init__(self, pro,mem,dd,mon):

        self.mem = mem
        self.dd = dd
        self.pro = pro
        self.mon = mon

    def muestra(self):
        
        print("Procesador_______: ", self.pro)
        print("Disco Duro_______: ", self.dd)
        print("Memoria RAM______: ", self.mem)
        print("Monitor__________: ", self.mon)

#End Class Computer

class Escritorio(Computadora):

    def __init__(self,pro,mem,dd,mon,gabinete,all_in_one):

        super().__init__(pro,mem,dd,mon)
        self.gabinete = gabinete
        self.all_in_one = all_in_one
    
    def muestra(self):
        super().muestra()
        print("Gabinete__________: ", self.gabinete)
        print("Todo en uno_______: ", self.all_in_one)
        print("Categorizado como: PC de Escritorio")

#End Class Desktop

class TrabajoEscritorio(Escritorio):

    def __init__(self,pro,mem,dd,mon,gabinete,all_in_one,usb,ethernet,svideo):

        self.usb = usb
        self.ethernet = ethernet
        self.svideo = svideo
        super().__init__(pro,mem,dd,mon,gabinete,all_in_one)
    
    def muestra(self):

        super().muestra()
        print("Puertos USB_______: ", self.usb)
        print("Red Alambrica_____: ", self.ethernet)
        print("Salida de Video___: ", self.svideo)
        print("Categorizado como: PC de Escritorio para Trabajo")
        
#End Class WorkDesktop

class GamerEscritorio(Escritorio):
    
    def __init__(self,pro,mem,dd,mon,gabinete,all_in_one,diadema,controles,tipo_ctrl,vel_mon):

        self.diadema=diadema
        self.controles=controles
        self.tipo_ctrl=tipo_ctrl
        self.vel_mon=vel_mon
        super().__init__(pro,mem,dd,mon,gabinete,all_in_one)
    
    def muestra(self):

        super().muestra()
        print("Diadema___________:", self.diadema)
        print("Controles_________: ", self.controles)
        print("Tipo de Control___: ", self.tipo_ctrl)
        print("Vel. del monitor__: ", self.vel_mon)
        print("Categorizado como: PC de Escritorio Gamer")

#End Class GamerDesktop

class Laptop(Computadora):
    def __init__(self,pro,mem,dd,mon,tipo,two_in_one):
        super().__init__(pro,mem,dd,mon)
        self.tipo = tipo
        self.two_in_one = two_in_one

    def muestra(self):
        super().muestra()
        print("Tipo de Laptop____: ", self.tipo)
        print("Todo en uno_______: ", self.two_in_one)
        print("Categorizado como: Laptop")

#End Class Laptop

class TrabajoLaptop(Laptop):
    def __init__(self,pro,mem,dd,mon,tipo,two_in_one,usb,ethernet,svideo):
        super().__init__(pro,mem,dd,mon,tipo,two_in_one)
        self.usb=usb
        self.ethernet=ethernet
        self.svideo=svideo
    
    def muestra(self):
        super().muestra()
        print("Conexiones USB____: ", self.usb)
        print("Red Alambrica_____: ", self.ethernet)
        print("Salida de Video___: ", self.svideo)
        print("Categorizado como: Laptop de Trabajo")

#End Class WorkLaptop

class GamerLaptop(Laptop):
    def __init__(self,pro,mem,dd,mon,tipo,two_in_one,diadema,controles,tipo_ctrl,vel_mon):
        super().__init__(pro,mem,dd,mon,tipo,two_in_one)
        self.diadema=diadema
        self.controles=controles
        self.tipo_ctrl=tipo_ctrl
        self.vel_mon=vel_mon
    
    def muestra(self):
        super().muestra()
        print("Diadema___________: ", self.diadema)
        print("Controles_________: ", self.controles)
        print("Tipo de Controles_: ", self.tipo_ctrl)
        print("Velocidad del Monitor: ", self.vel_mon)
        print("Categorizado como: Laptop Gamer")

#End Class GamerLaptop

class Ordenadores(TrabajoEscritorio,TrabajoLaptop,GamerEscritorio,GamerLaptop):

    def categorizacion(self):
        
        if self.pro !="" and self.mem!="" and self.dd!="" and self.mon!="" and self.gabinete!="" and self.all_in_one!="" and self.tipo=="" and self.two_in_one=="" and self.diadema!="" and self.controles!="" and self.tipo_ctrl!="" and self.vel_mon!="" and self.usb=="" and self.ethernet=="" and self.svideo=="":

            GamerEscritorio.muestra(self)





#Clase Ordenadores es la herencia multiple
#End Class Ordenadores 

#----MAIN----

def pide_computadora():

    pc=PideValor("Indica el tipo de Procesador                  :" )
    pro=pc.pide_cadena()
    pc=PideValor("Indica la capacidad de Memoria RAM            :" )
    mem=pc.pide_cadena()
    pc=PideValor("Indica la capacidad del disco duro            :" )
    dd=pc.pide_cadena()
    pc=PideValor("Indica el tamaño y tipo de Monitor            :" )
    mon=pc.pide_cadena()
    pc=PideValor("Indica el tipo de gabinete                    :" )
    gabinete=pc.pide_cadena()
    pc=PideValor("Indica si es todo en uno                      :" )
    all_in_one=pc.pide_cadena()
    pc=PideValor("Indica su tipo                                :" )
    tipo=pc.pide_cadena()
    pc=PideValor("Indica si es 2 en uno (Plegable)              :" )
    two_in_one=pc.pide_cadena()
    pc=PideValor("Cuenta con diadema                            :" )
    diadema=pc.pide_cadena()
    pc=PideValor("Cuenta con controles                          :" )
    controles=pc.pide_cadena()
    pc=PideValor("Indica el tipo de controles                   :" )
    tipo_ctrl=pc.pide_cadena()
    pc=PideValor("Indica la velocidad del monitor               :" )
    vel_mon=pc.pide_cadena()
    pc=PideValor("Cantidad de puertos USB                       :" )
    usb=pc.pide_cadena()
    pc=PideValor("Cuenta con red alambrica (Ethernet)           :" )
    ethernet=pc.pide_cadena()
    pc=PideValor("Indica la(s) salidas de Video                 :" )
    svideo=pc.pide_cadena()
    
    Object=Ordenadores(pro=pro,mem=mem,dd=dd,mon=mon,gabinete=gabinete,all_in_one=all_in_one,tipo=tipo,two_in_one=two_in_one,diadema=diadema,controles=controles,tipo_ctrl=tipo_ctrl,vel_mon=vel_mon,usb=usb,ethernet=ethernet,svideo=svideo)
    Object.muestra()

#pro,mem,dd,mon,gabinete,all_in_one,tipo,two_in_one,diadema,controles,tipo_ctrl,vel_mon,usb,ethernet,svideo

pide_computadora()



