
#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Validacion de Valores y Escritura de Datos

#----CLASES----

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

        datos_contenido=["¿Cual es el ID del video ?","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Atributos del tema?" ]

        #global datos

        datos = []
           
        print(datos_contenido[0])
        id=str(input("->"))
        ap=id[1]
        ap=ap.lower()

        datos.append(id)

        if ap=="p":
            for i in range(1,6):
                print(datos_contenido[i])
                x=input("->")
                datos.append(x)
            datos.append(",,,")
                        

        elif ap=="s":
            for i in range(1,9):
                print(datos_contenido[i])
                x=input("->")
                datos.append(x)
            datos.append(",")

        elif ap=="d":
            for i in range(1,10):
                print(datos_contenido[i])
                x=input("->")
                datos.append(x)
        else:
            print("Numero de opcion invalida (ERR_002)")
           
        return datos

    def validar_opcion_menu(self):
            
        while 1:

            opcion = input("->")

            try:

                while 1:     
                    opcion = int(opcion)
                    if opcion <=10:  
                        return   opcion
                    else:
                        print("Numero de opción no valida (ERRx002)")
                        break
                        
            except ValueError:
                print("La opcion seleccionada no es un numero (ERRx001)")

    def validar_string(self):
            #Si se usa este metodo usar la siguiente nomenclatura:
            #nombre_objeto=PideValor(limite_inferior,limite_superior)
            #nombre_objeto.validar_string

        while 1:
            string = input("-->")
            if string.isalpha():
                while 1:
                    string = str(string)
                    if len(string)<self.lim_in or len(string)>self.lim_sup:
                        print("La cadena debe estar entre "+str(self.lim_in)+" y "+str(self.lim_sup)+" caracteres (INVALx001)")
                        break
                    else:
                        return string
            
            else:
                print("La cadena contiene valores numericos (ERRx003)")

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

#----MAIN----



