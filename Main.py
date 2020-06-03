#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Main del Proyecto integrador

#----MAIN----

from Proyecto_Integrador import *

menu=Menu()
menu.pre_menu()
option = Validaciones("","","",2)
option = option.validar_opcion_menu()

if option == 1:
    archive = CSV()
    archive = archive.leer()

elif option == 2:
    archive = CSV()
    archive = archive.crear()


while 1:

    menu=Menu(10)
    menu.menu_principal()
    option = Validaciones("","","",10)
    option = option.validar_opcion_menu()


    if option == 1:
        pass

    elif option == 2:
        pass

    elif option == 3:
        pass

    elif option == 4:
        pass 

    elif option == 5:
        pass

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
