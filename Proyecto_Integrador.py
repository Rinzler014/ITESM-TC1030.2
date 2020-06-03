#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Proyecto Integrador

#----IMPORTS---

from Pide_valor import PideValor

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
        

class Videos():
    def __init__(self,ID,Titulo,Duracion,Calificacion):
        self.ID             = ID
        self.Titulo         = Titulo
        self.Duracion       = Duracion
        self.Calificacion   = Calificacion      
    def pide_datos(self):
        pass
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

menu=Menu()
menu.despliegue()
option = PideValor()
option = option.validar_opcion_menu()
print("-"*32)

'''

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
'''