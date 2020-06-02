#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Anatanael Jesus Miranda Faustino
#Actvidad en este programa: Pedir Valor

#----CLASES----

class PideValor():

    def __init__(self, message, lim_in=0, lim_sup=0, tipo=""):
        self.message    = message
        self.lim_in     = lim_in
        self.lim_sup    = lim_sup
        self.tipo       = tipo
    
    def __del__(self):
        pass
    
    def error_string(self):
        pass
    
    def pide_str(self):
        while True:
            string = input(self.message)
            if (self.lim_in==0) and (self.lim_sup==0)
                return string
            else:
                if len(string)<self.lim_in or len(string)>self.lim_sup:
                    no_way="La cadena debe estar entre"+str(self.lim_in)+"y"+str(self.lim_sup)+"caracteres (ERR_01)"
                    eo=PideValor(no_way)
                    eo.error_string()
                    del eo
                else:
                    return string
    
    def pide_numero(self):
        while True:
            num = input(self.message)
            if not num.isnumeric():
                no_way = "El valor ingresado contiene caractres invalidos (ERR_02)"
                eo=PideValor(no_way)
                eo.error_string()
                del eo
            else:
                if self.tipo=="int": numero = int(num)
                else:
                    if (self.lim_in==0) and (self.lim_sup==0):
                        return num
                    else:
                        if numero<self.lim_in or numero>lim_sup:
                            no_way="El valor debe estar entre"+str(self.lim_in)+"y"+str(self.lim_sup)+"(ERR_03)"
                            eo=PideValor(no_way)
                            oe.error_string()
                            del eo
                        else:
                            return numero
#----MAIN----