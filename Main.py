#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Main del Proyecto integrador

#----MAIN----

from Proyecto_Integrador import *

menu=Menu()
menu.pre_menu()
option = Validaciones_1("","","",2)
option = option.validar_opcion_menu()

if option == 1:
    archive = CSV()
    archive_lec = archive.leer()


elif option == 2:
    archive = CSV()
    archive_lec = archive.crear()
    

 


while 1:

    menu=Menu()
    menu.menu_principal()
    option = Validaciones_1("","","",10)
    option = option.validar_opcion_menu()


    if option == 1:
        
        objeto=Videos("","","","")
        x=objeto.pide_datos()
        id_=x[0]
        id_=id_[0]
        id_=id_.lower()
        if id_[0]=="p":
            obj_peli=Peliculas(x[0],x[1],x[2],x[3],x[4],x[5])
            obj_peli.muestra_datos()
        elif id_[0]=="s":
            obj_peli=Serie(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
            obj_peli.muestra_datos()
        elif id_[0]=="d":
            obj_peli=Documental(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9])
            obj_peli.muestra_datos()
        escritura=CSV()
        escritura.escribir(archive_lec,x)


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
