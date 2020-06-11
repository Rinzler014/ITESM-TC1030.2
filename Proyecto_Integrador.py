
#----IMPORTS---

from Pide_valor import CSV,Validaciones,Archivadora,Consultas,Videos,Peliculas,Mostrar_listas,Valores_usuario 


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
        option_pre = Validaciones("","","",2)
        option_pre = option_pre.validar_opcion_menu()

        if option_pre == 1:
            archive_=str(input("Ingrese el nombre de su archivo: "))

        elif option_pre == 2:
            archive = CSV()
            archive_=archive.crear()
            
        while 1:

            menu=Menu()
            menu.menu_principal()
            option = Validaciones("","","",10)
            option = option.validar_opcion_menu()


            if option == 1:
                archive = CSV()
                _datos_lec = archive.leer(archive_)
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                objeto=Valores_usuario()
                x=objeto.menu_op1()
                escritura=CSV()
                escritura.escribir(_datos_lec,x,archive_,option_pre)
                
           
            elif option == 2:
                op_2 = Archivadora()
                op_2.archivadora_general(archive_)
                Consultas().consulta_por_id()

            elif option == 3:
                op_3 = Archivadora()
                op_3.archivadora_general(archive_)
                Mostrar_listas().lista_general(3,"")

            elif option == 4:
                op_4 = Archivadora()
                op_4.archivadora_general(archive_) 
                Mostrar_listas().lista_general(4,"")

            elif option == 5:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general(2,"")


            elif option == 6:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general(1,"P")
                pass

            elif option == 7:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general(1,"S")

            elif option == 8:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general(1,"D")

            elif option == 9:
                op_5=Archivadora()
                op_5.archivadora_general(archive_)
                Mostrar_listas().lista_general(8,"")

            elif option ==10:
                print("EXIT REQUESTED BY USER...//")
                break

