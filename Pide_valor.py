
#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Validacion de Valores y Escritura de Datos

#----CLASES----

class Validaciones():

    def __init__(self, lim_sup = "", lim_in = "", tipo = "", opciones_menu = ""):
        self.lim_sup = lim_sup
        self.lim_in = lim_in
        self. tipo = tipo
        self.opciones_menu = opciones_menu

    def validar_string(self, string_):
            #Si se usa este metodo usar la siguiente nomenclatura:
            #nombre_dobjeto=PideValor(limite_inferior,limite_superior)
            #nombre_objeto.validar_string

        while 1:
            string = str(string_)
            if len(string)<self.lim_in or len(string)>self.lim_sup:
                print("La cadena debe estar entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" caracteres (INVALx001)")
                string=input("->")
                while 1:
                    if len(string)<self.lim_in or len(string)>self.lim_sup:
                        print("La cadena debe estar entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" caracteres (INVALx001)")
                        string=input("->")
                    else:
                        return string
            else:
                return string
            return string

    def validar_numero(self, integer_):

        #Si se usa este metodo usar la siguiente nomenclatura:
        #nombre_objeto=PideValor(limite_inferior,limite_superior,tipo(solo "int", de lo contrario dejar en blanco))
        #nombre_objeto.validar_numero

        while 1:  

            integer =int( integer_)
            if integer<self.lim_in or integer>self.lim_sup:
                print("El valor debe estat entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" valor numerico (INVALx001)")
                integer = int(input("-->"))
                while 1:
                    if integer<self.lim_in or integer>self.lim_sup:
                        print("El valor debe estat entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" valor numerico(INVALx001)")
                        integer = int(input("-->"))
                    else:
                        return integer
            else:
                return integer
            return integer


class CSV():

    def leer(self):
        name_file=str(input("Ingrese el nombre de su archivo: "))
        file_=open(name_file+".csv","r")
        _datos_lec=file_.readlines()
        _datos_lec.pop(0)
        file_.close()
        _datos_line=[]
        for line in _datos_lec:
            columna=line.split(",")
            for i in range (len(columna)):
                _datos_line.append(columna[i])
        
            
        return _datos_line
    
    
    def crear(self):
        print("Indique el nombre de su csv")
        name_file=str(input("->"))
        file_=open(name_file+".csv","w+")
        file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        return file_
        

    def escribir(self): 
        file_=self.leer()
        file_.append("\n")
        objeto=PideValor()
        x=objeto.tomar_datos()
        file_list=file_+x
        _file_=open("Prueba.csv","w+")
        _file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        for i in range (len (file_list)):
            if file_list[i]=="\n":

                _file_.write(file_list[i])
            else:
                _file_.write(file_list[i]+",")
        _file_.close()

class PideValor():

    def __init__(self, lim_in="", lim_sup="", tipo=""):
        self.lim_in     = lim_in
        self.lim_sup    = lim_sup
        self.tipo       = tipo
        
    def tomar_datos(self):
        
        while 1:

            datos_contenido=["¿Cual es el ID del video ?","¿Cual es el titulo ?","¿Cual es el genero?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Cual es el tema?" ]

            datos = []
            
            print(datos_contenido[0])
            id=str(input("->"))
            ap=id[0]
            ap=ap.upper()
            validar_id=Validaciones(5,1)
            ap=validar_id.validar_string(id)
            datos.append(ap)
            ap=ap.upper()
            ap=ap[0]

            if ap == "P":
                for i in range(1,6):
                    print(datos_contenido[i])
                    x=input("->")
                    
                    if i==1:
                        validar=Validaciones(30,1)
                        x=validar.validar_string(x)
                        
                    elif i==2:
                        validar=Validaciones(15,1)
                        x=validar.validar_string(x)
                        
                    elif i==3:
                        validar=Validaciones(500,1)
                        x=validar.validar_numero(x)
                       
                    elif i==4:
                        validar=Validaciones(5,1)
                        x=validar.validar_numero(x)
                        
                    elif i==5:
                        validar=Validaciones(15,1)
                        x=validar.validar_string(x)
                    elif i==6:
                        validar=Validaciones(500,1)
                        x=validar.validar_numero(x)
                    elif i==7:
                        validar=Validaciones(500,1)
                        x=validar.validar_numero(x)
                    elif i==8:
                        validar=Validaciones(30,1)
                        x=validar.validar_string(x)
                    elif i==9:
                        validar=Validaciones(30,1)
                        x=validar.validar_string(x)
                    datos.append(x)

                datos.append(",,,")
                
                return datos
                            
            elif ap == "s":
                for i in range(1,9):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                datos.append(",")
                return datos

            elif ap == "d":
                for i in range(1,10):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                return datos

            else:
                print("No se pudo determinar el tipo de contenido")
