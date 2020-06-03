
#from proyecto import *

class PideValor():

    def __init__(self, lim_in="", lim_sup="", tipo=""):
        self.lim_in     = lim_in
        self.lim_sup    = lim_sup
        self.tipo       = tipo

    def tomar_datos(self):
        
        datos_contenido=["¿Cual es el ID de la pelicula?","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Atributos del tema?" ]

        global datos 

        datos = []

    def validar_opcion_menu(self):
        
        while 1:

            opcion = input("->")

            try:

                while 1:     
                    opcion = int(opcion)
                    if opcion <=7:  
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
        





if __name__ == "__main__":
    yo=PideValor(1,5)
    a=yo.validar_string()



