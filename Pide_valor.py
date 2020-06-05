
import time 

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

    def validar_string(self, message = ""):
        
        #Si se usa este metodo usar la siguiente nomenclatura:
        #nombre_dobjeto=PideValor(limite_inferior,limite_superior)
        #nombre_objeto.validar_string

        while 1:
            string = input("-->")
            if string.isalnum():
                while 1:
                    string = str(string)
                    if len(string)<self.lim_in or len(string)>self.lim_sup:
                        print("La cadena debe estar entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" caracteres (INVALx001)")
                        print(message)
                        break
                    else:
                        return string
            else:
                print("No se indico ningun valor (ERRx003)")
                print(message)

    def validar_numero(self, messsage = ""):

        #Si se usa este metodo usar la siguiente nomenclatura:
        #nombre_objeto=PideValor(limite_inferior,limite_superior,tipo(solo "int", de lo contrario dejar en blanco))
        #nombre_objeto.validar_numero

        while 1:
            integer = input("-->")
            if integer.isdigit():
                while 1:
                    if self.tipo == "int":
                        integer = int(integer)
                    else:
                        integer = int(integer)
                    if integer<self.lim_in or integer>self.lim_sup:
                        print("El valor numerico debe estar en el rango de "+str(self.lim_in)+" y "+str(self.lim_sup)+" (INVALx002)")
                        print(messsage)
                        break
                    else:
                        return int(integer)
            else:
                print("Los valores contienen caracteres no numericos (ERRx004)")
                print(messsage)

    def validacion_del_id(self, datos_contenido):

        while 1:

            #Validacion del ID del contenido
            print(datos_contenido[0])
            validar_id=Validaciones(1,1)
            id_contenido=validar_id.validar_string(datos_contenido[0])
            id_contenido=id_contenido.upper()
            id_contenido=id_contenido[0]
            if id_contenido == "P" or id_contenido == "S":
                break
            elif id_contenido == "D":
                break
            else:
                print("No se pudo determinar el tipo de contenido\n")
                
        while 1:

            #Validacion de la clasificación
            print(datos_contenido[1])
            validar_clasif = Validaciones(1,1)
            clasif_contenido = validar_clasif.validar_string(datos_contenido[1])
            clasif_contenido = clasif_contenido.upper()
            clasif_contenido = clasif_contenido[0]
            if clasif_contenido == "A" or clasif_contenido == "B":
                break
            elif clasif_contenido == "C" or clasif_contenido == "D":
                break
            else:
                print("No se pudo determinar la clasificacion del contenido\n")

        #Validacion del numero de contenido
        print(datos_contenido[2])
        validar_num_contenido = Validaciones(3,1)
        num_contenido = str(validar_num_contenido.validar_numero(datos_contenido[2]))
        num_contenido = num_contenido

        #Escritura del ID completo
        id_completo = id_contenido+clasif_contenido+num_contenido

        return id_completo

class CSV():

    def leer(self,archive):
        name_file=archive
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

                _file_.write(file_list[i])
        _file_.close()

class PideValor():

    def __init__(self, lim_in="", lim_sup="", tipo=""):
        self.lim_in     = lim_in
        self.lim_sup    = lim_sup
        self.tipo       = tipo
        
    def tomar_datos(self):
        
        while 1:

            datos_contenido=["Ingrese el identificador de contenido (P = Pelicula, S = Serie, D= Documental)","Ingrese la clasificacion del contenido (A = Todo Publico, B = Mayores de 15 años, C = Adultos de 18 años, D = Publico de alto criterio)","Ingrese el numero de contenido (Solo 3 digitos [Ej. 001])","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Cual es el tema?" ]

            datos = []
            
            val_id = Validaciones()
            id_completo = val_id.validacion_del_id(datos_contenido)

            datos.append(id_completo)

            if id_completo[0] == "P":
                for i in range(3,8):
                    print(datos_contenido[i])
                    
                    if i==3:
                        #Titulo
                        validar=Validaciones(30,1)
                        x=validar.validar_string()
                    elif i==4:
                        #Duracion
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==5:
                        #Calificacion
                        validar=Validaciones(5,1)
                        x=str(validar.validar_numero())
                    elif i==6:
                        #Audiencia
                        validar=Validaciones(15,1)
                        x=validar.validar_string()
                    elif i==7:
                        #Genero
                        validar=Validaciones(15,1)
                        x=validar.validar_string()

                    datos.append(","+x)
                datos.append(",,,")
                return datos
                            
            elif id_completo[0] == "S":
                for i in range(3,11):
                    print(datos_contenido[i])

                    if i==3:
                        #Titulo
                        validar=Validaciones(30,1)
                        x=validar.validar_string()
                    elif i==4:
                        #Duracion
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==5:
                        #Calificacion
                        validar=Validaciones(5,1)
                        x=str(validar.validar_numero())
                    elif i==6:
                        #Audiencia
                        validar=Validaciones(15,1)
                        x=validar.validar_string()
                    elif i==7:
                        #Genero
                        validar=Validaciones(15,1)
                        x=validar.validar_string()
                    elif i==8:
                        #Temporada
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==9:
                        #Episodio
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==10:
                        #Titulo del Episodio
                        validar=Validaciones(30,1)
                        x=validar.validar_string()

                    datos.append(","+x)
                    datos.append(",")
                    x=input("->")
                    datos.append(x)

                datos.append(",")
               
                return datos

            elif id_completo[0] == "D":

                for i in range(3,12):
                    print(datos_contenido[i])

                    if i==3:
                        #Titulo
                        validar=Validaciones(30,1)
                        x=validar.validar_string()
                    elif i==4:
                        #Duracion
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==5:
                        #Calificacion
                        validar=Validaciones(5,1)
                        x=str(validar.validar_numero())
                    elif i==6:
                        #Audiencia
                        validar=Validaciones(15,1)
                        x=validar.validar_string()
                    elif i==7:
                        #Genero
                        validar=Validaciones(15,1)
                        x=validar.validar_string()
                    elif i==8:
                        #Temporada
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==9:
                        #Episodio
                        validar=Validaciones(500,1)
                        x=str(validar.validar_numero())
                    elif i==10:
                        #Titulo del Episodio
                        validar=Validaciones(30,1)
                        x=validar.validar_string()
                    elif i==11:
                        #Tema
                        validar=Validaciones(30,1)
                        x=validar.validar_string()

                    datos.append(","+x)
                return datos

class Archivadora():

    def archivadora_general (self,_datos_line,x):
        lista=_datos_line+x
        for line in lista:
            fields = line.split(",") 
            id = fields[0]
            titulo=fields[1]
            genero=fields[2]
            duración=fields[3]
            calificaci=fields[4]
            audien=fields[5]
            temporada=fields[6]
            episodio=fields[7]
            til_epi=fields[8]
            tema=fields[9]
            cla=id[1]
            id_key=id[0]
            cla=cla.lower()
            id_key=id_key.lower()
            if id_key =="p":
                self.archivar_peliculas(id,titulo, genero,duración,calificaci,audien)
                

            elif id_key == "s": 
                self.archivar_series(id,titulo, genero,duración,calificaci,audien,temporada,episodio,til_epi)
            
            elif id_key =="d":
                self.archivar_documentales(id,titulo, genero,duración,calificaci,audien,temporada,episodio,til_epi,tema)
            


    def archivar_peliculas(self,id,titulo, genero,duración,calificaci,audien):
        global peliculas 
        peliculas={}
        cla=id[1]
        id_key=id[0]
        peliculon=Peliculas(id,titulo,genero,duración,calificaci,audien)
        peliculas[id_key+cla]=peliculon
        peliculon.muestra_datos()
        time.sleep(4)


    
    def archivar_series(self,id_key,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi):


        global serie_dic
        serie_dic={}
        serie_obj=Serie(id_key,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi)
        cla=id_key[1]
        id_key__=id_key[0]
        serie_dic[id_key__+cla]=serie_obj
        serie_obj.muestra_datos()
        time.sleep(4)
        

            
    
    def archivar_documentales(self,id,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi,tema):
        global archivar_documentales
        archivar_documentales={}
        document_obj=Documental(id,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi,tema)
        key=id[1]
        id_key=id[0]
        serie_dic[id_key+key]=document_obj
        document_obj.muestra_datos()
        time.sleep(4)
        
        
            #documental=
            




 