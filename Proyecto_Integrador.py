#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Anatanael Jesus Miranda Faustino
#Actvidad en este programa: Proyecto Integrador

#----IMPORTS---

from Pide_valor import *

#----CLASES----

class Menu():
    def despliegue(self):
        print("-"*32)
        print("-"*8+" Menu Principal "+"-"*8)
        print("-"*32)
        print("-"*1+" Seleccione la opcion Deseada "+"-"*1)
        print("-"*32)
        print("1. Añadir Video")
        print("2. Buscar Video por Identificador")
        print("-"*32)
        print("-"*10+" Logistica "+"-"*11)
        print("-"*32)
        print("3. Consultar video por titulo")
        print("4. Consultar video por genero")
        print("5. Listado General")
        print("6. Listado de Peliculas")
        print("7. Listado de Series")
        print("8. Listado de Documentales")
        print("9. Listado por calificaciones")
        print("10. Salir")
        print("-"*32)
    
    


class validador ():
    def __init__(self, lim_in="", lim_sup="", tipo=""):
        self.lim_in     = lim_in
        self.lim_sup    = lim_sup
        self.tipo       = tipo

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
            
    

class Videos():
    def __init__(self,ID,Titulo,Duracion,Calificacion):
        self.ID=ID
        self.Titulo=Titulo
        self.Duracion=Duracion
        self.Calificacion=Calificacion      
    def pide_datos(self):
        meto_ext=PideValor()
        a=meto_ext.tomar_datos()

    def muestra_datos(self):
        pass

class Peliculas (Videos):
    def __init__(self,ID,Titulo,Duracion,Calificacion,Audiencia,Genero):
        super().__init__(ID,Titulo,Duracion,Calificacion)
        self.Audiencia=Audiencia
        self.Genero=Genero

     
    def pide_datos(self):
        pass

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
        pass

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
        pass

    def muestra_datos(self):
        super().muestra_datos()
        print("El tema del documental es: ", self.Tema)


#----MAIN----

#Despliegue y Funcionamiento del Menu
