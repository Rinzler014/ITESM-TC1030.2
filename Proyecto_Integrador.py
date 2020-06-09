
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
                _datos_lec = archive.leer(archive_)
                objeto=Videos("","","","")
                x=objeto.pide_datos()
                escritura=CSV()
                escritura.escribir(_datos_lec,x)
                peli=Archivadora()
                peli.archivadora_general(archive_)
           
            elif option == 2:
                op_2 = Archivadora()
                op_2.archivadora_general(archive_)
                Consultas().consulta_por_id()

            elif option == 3:
                op_3 = Archivadora()
                op_3.archivadora_general(archive_)
                Consultas().consulta_por_titulo()

            elif option == 4:
                op_4 = Archivadora()
                op_4.archivadora_general(archive_) 
                Consultas().consulta_por_genero()

            elif option == 5:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general()


            elif option == 6:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_peliculas()
                pass

            elif option == 7:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_series()

            elif option == 8:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().listado_documentales()

            elif option == 9:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                inferio,superior=PideValor().tomar_limites_()
                Mostrar_listas().listado_por_calificación(inferio,superior)

            elif option ==10:
                print("EXIT REQUESTED BY USER...//")
                break

