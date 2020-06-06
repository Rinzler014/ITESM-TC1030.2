#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Anatanael Jesus Miranda Faustino
#Actvidad en este programa: Proyecto Integrador

#----IMPORTS---

from Pide_valor import *

#----CLASES----

class Menu():

    def pre_menu(self):
        print("-"*32)
        print("-"*7+" Antes de Iniciar "+"-"*7)
        print("-"*32)
        print("-"*1+" Seleccione la opcion deseada "+"-"*1)
        print("1. Ya cuento con un archivo (el archivo debe de ser)")
        print("2. No tengo archivo (crea uno y agrega videos)")
        print("-"*32)

    def menu_principal(self):
        print("-"*32)
        print("-"*8+" Menu Principal "+"-"*8)
        print("-"*32)
        print("-"*1+" Seleccione la opcion deseada "+"-"*1)
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


class Eleccion():
    
    def inicio_de_menu (self):
        menu=Menu()
        menu.pre_menu()
        option = Validaciones("","","",2)
        option = option.validar_opcion_menu()

        if option == 1:
            archive_=str(input("Ingrese el nombre de su archivo: "))

        elif option == 2:
            archive = CSV()
            

        


        while 1:

            menu=Menu()
            menu.menu_principal()
            option = Validaciones("","","",10)
            option = option.validar_opcion_menu()


            if option == 1:
                archive = CSV()
                archive_lec,_datos_lec = archive.leer(archive_)
                objeto=Videos("","","","")
                x=objeto.pide_datos()
                escritura=CSV()
                escritura.escribir(_datos_lec,x)
                peli=Archivadora()
                peli.archivadora_general(archive_)
           


            elif option == 2:
                pass

            elif option == 3:
                pass

            elif option == 4:
                pass 

            elif option == 5:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general()


            elif option == 6:
                pass

            elif option == 7:
                pass

            elif option == 8:
                pass

            elif option == 9:
                pass

            elif option ==10:
                print("EXIT REQUESTED BY USER...//")
                break

