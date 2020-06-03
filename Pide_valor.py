
#from proyecto import *

class PideValor():
        
    def tomar_datos(self):

        datos_contenido=["¿Cual es el ID de la pelicula?","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Atributos del tema?" ]

        global datos 

        datos = []
        
        while 1:

            opcion = input("->")

            try:

                while 1:
                    
                    opcion = int(opcion)

                    if opcion == 1:  
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

                        elif ap=="s":
                            for i in range(1,9):
                                print(datos_contenido[i])
                                x=input("->")
                                datos.append(x)

                        elif ap=="d":
                            for i in range(1,10):
                                print(datos_contenido[i])
                                x=input("->")
                                datos.append(x)

                    elif opcion == 2:
                        pass
                        
                    elif opcion == 3:
                        pass

                    elif opcion == 4:
                        pass        

                    elif opcion == 5:
                        pass

                    elif opcion == 6:
                        pass

                    elif opcion == 7:
                        pass
                        
                    else:
                        print("Numero de opcion invalida (ERR_002)")
                        break


            except ValueError:
                print("La opcion seleccionada no es un numero (ERR_001)")
            
            
        


if __name__ == "__main__":
    yo=PideValor()
    a=yo.tomar_datos()
    print(a)



