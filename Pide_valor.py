
#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Validacion de Valores y Escritura de Datos

#----CLASES----

class Videos():
    def __init__(self,ID,Titulo,Duracion,Calificacion):
        self.ID=ID
        self.Titulo=Titulo
        self.Duracion=Duracion
        self.Calificacion=Calificacion      
    def pide_datos(self):
        metodo_=PideValor()
        x=metodo_.tomar_datos()
        return x

    def muestra_datos(self):
        print("El ID es: ", self.ID)
        print("El titulo es: ",self.Titulo)
        print("la duración es: ",self.Duracion)
        print("La calificación es: ",self.Calificacion)

class Peliculas (Videos):
    def __init__(self,ID,Titulo,Duracion,Calificacion,Audiencia,Genero):
        super().__init__(ID,Titulo,Duracion,Calificacion)
        self.Audiencia=Audiencia
        self.Genero=Genero
     
    def pide_datos(self):
        super().pide_datos()

    def muestra_datos(self):
        super().muestra_datos()
        print("La audiencia para esta serie es: ",self.Audiencia)
        print("La genero para esta serie es: ",self.Genero)

class Serie (Peliculas):
    def __init__(self,ID,Titulo,Duracion,Calificacion,Audiencia,Genero,Temporada,Episodio,Til_episodio):
        super().__init__(ID,Titulo,Duracion,Calificacion,Audiencia,Genero)
        self.Temporada=Temporada
        self.Episodio=Episodio
        self.Til_episodio=Til_episodio

    def pide_datos(self):
        super().pide_datos()

    def muestra_datos(self):
        super().muestra_datos()
        print("La temporada es: ",self.Temporada)
        print("El episodio es: ",self.Episodio)
        print("El tilulo del episodio es: ",self.Til_episodio)

class Documental (Serie):
    def __init__(self,ID,Titulo,Duracion,Calificacion,Audiencia,Genero,Temporada,Episodio,Til_episodio,Tema):
        super().__init__(ID,Titulo,Duracion,Calificacion,Audiencia,Genero,Temporada,Episodio,Til_episodio)
        self.Tema=Tema
     
    def pide_datos(self):
        super().pide_datos()

    def muestra_datos(self):
        super().muestra_datos()
        print("El tema del documental es: ", self.Tema)


class Validaciones():

    def __init__(self, lim_sup = "", lim_in = "", tipo = "", opciones_menu = ""):
        self.lim_sup = lim_sup
        self.lim_in = lim_in
        self. tipo = tipo
        self.opciones_menu = opciones_menu

    def validar_opcion_menu(self):
            
        while 1:
            opcion = input("->")
            try:
                while 1:     
                    opcion = int(opcion)
                    if opcion>=1 and opcion <=self.opciones_menu:  
                        return   opcion
                    else:
                        print("Numero de opción no valida (ERRx002)")
                        break                          
            except ValueError:
                print("La opcion seleccionada no es un numero (ERRx001)")

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
        
            
        return _datos_line,_datos_lec
    
    
    def crear(self):
        print("Indique el nombre de su csv")
        name_file=str(input("->"))
        file_=open(name_file+".csv","w+")
        file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        file_.close()
        file_list=[]
        return file_list
        

    def escribir(self,lectura,x): 
        file_=lectura
        file_.append("\n")
        x=x
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
                    datos.append(str(x))

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


class Archivadora():
    def archivar_peliculas(self,_datos_line,nuevo_peli):
        lista=_datos_line
        global peliculas 
        peliculas={}
        for line in lista:
            fields = line.split(",")
            id_key = fields[0]
            titulo=fields[1]
            genero=fields[2]
            duración=fields[3]
            calificaci=fields[4]
            audien=fields[5]
            cla=id_key[0]
            peliculon=Peliculas(id_key,titulo,genero,duración,calificaci,audien)
            peliculas[cla]=peliculon
        peliculon=Peliculas(nuevo_peli[0],nuevo_peli[1],nuevo_peli[2],nuevo_peli[3],nuevo_peli[4],nuevo_peli[5])
        cla=nuevo_peli[0]
        cla=cla[1]
        peliculas[cla]=peliculon
        peliculon.muestra_datos()

    
    def archivar_series(self,_datos_line,nuevo_seri):
        lista=_datos_line
        global series
        series={}
        for line in range(len(lista)):
            id_key = line[0]
            titulo=line[1]
            genero=line[2]
            duración=line[3]
            calificaci=line[4]
            audien=line[5]
            temporada=line[6]
            episodio=line[7]
            til_epi=line[8]
            key=id_key[1]
            series_odj=Serie(id_key,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi)
            series[key]=series_odj
        series_odj.muestra_datos()
         

            
    
    def archivar_documentales(self,_datos_line,nuevo_docu):
        lista=_datos_line
        global archivar_documentales
        archivar_documentales={}
        for line in lista:
            id = line[0]
            titulo=line[1]
            genero=line[2]
            duración=line[3]
            calificaci=line[4]
            audien=line[5]
            temporada=line[6]
            episodio=line[7]
            til_epi=line[8]
            tema=line[9]
            documen_obj=Documental(id,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi,tema)
            key=id[1]
            series[key]=documen_obj
        documen_obj.muestra_datos()
            #documental=
            
            




 