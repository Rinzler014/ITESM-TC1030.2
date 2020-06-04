
#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Validacion de Valores y Escritura de Datos

#----CLASES----
#from Proyecto_Integrador import *

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
        file_.write("ID"+",Titulo"+",Genero"+",Duración"+",Calificación"+",Audiencia"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        return file_
        

    def escribir(self): 
        file_=self.leer()
        file_.append("\n")
        objeto=PideValor()
        x=objeto.tomar_datos()
        file_list=file_+x
        _file_=open("Prueba.csv","w+")
        _file_.write("ID"+",Titulo"+",Genero"+",Duración"+",Calificación"+",Audiencia"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
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
            ap=ap[0]

            if ap == "P":
                for i in range(1,6):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                    if x[i]==1:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==2:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==3:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==4:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==5:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==6:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==7:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==8:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])
                    elif x[i]==9:
                        validar=Validaciones(30,1)
                        validar.validar_string(x[i])

                    
                    

                datos.append(",,,")
                
                return datos
                            
            elif ap == "S":
                
                for i in range(1,9):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                datos.append(",")
                return datos
                

            elif ap == "D":
                for i in range(1,10):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                return datos

            else:
                print("No se pudo determinar el tipo de contenido")
        print("s_______")
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

    def validar_string(self,str_):
            #Si se usa este metodo usar la siguiente nomenclatura:
            #nombre_objeto=PideValor(limite_inferior,limite_superior)
            #nombre_objeto.validar_string

        while 1:
            string = str(str_)
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


    def validar_numero(self):

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
                        integer = float(integer)
                    if len(str(integer))<self.lim_in or len(str(integer))>self.lim_sup:
                        print("El valor numerico debe estar entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" caracteres (INVALx002)")
                        break
                    else:
                        return int(integer)
            else:
                print("Los valores contienen caracteres no numericos (ERRx004)")
