#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Validacion de Cadena de Texto

#----CLASES----

class PideValor():
    def __init__(self, letreto, li=0, ls=0, ciclo="no", tipo=""):
        self.letreto=letreto
        self.li=li 
        self.ls=ls
        self.ciclo=ciclo.upper()
        self.tipo=tipo
    def __del__(self):
        pass
    def error_cadena(self):
        input(self.letreto)
    def pide_cadena(self):
        while True:
            cad=input(self.letreto)
            if self.ciclo=="NO": return cad
            else:
                if (self.li==0) and (self.ls==0):return cad
                else:
                    if len(cad)<self.li or len (cad)>self.ls:
                        er="Error, la cadena debe estar entre "+str(self.li)+" y "+str(self.ls)+" caracteres...."
                        eo=PideValor(er)
                        eo.error_cadena()
                        del eo
                    else: return cad

    def pide_numero(self):
        while True:
            cad=input (self.letreto)
            if not cad.isnumeric():
                eo=PideValor("Error, la cadena contiene caracteres no vailidos...")
                eo.error_cadena()
                del eo
            else:
                if self.tipo=="int": numero=int(cad)
                else: numero=float (cad)
                if self.ciclo=="NO" :return numero
                else:
                    if (self.li==0) and (self.ls==0): return numero
                    else:
                        if numero <self.li or numero>self.ls:
                            er="Error, el valor debe estar entre "+str(self.li)+" y "+str(self.ls)+".........."
                            oe=PideValor(er)
                            oe.error_cadena()
                            del oe 
                        else : return numero

#----MAIN----


