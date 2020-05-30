#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Metodo Especial String

#----CLASES----
class MetodoSTR():

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    def __str__(self):
        string = "El elemento 1 es: "+self.value1+"\nEl elemento 2 es: "+self.value2

        return string

#----MAIN----

while 1:
    
    print("Metodo Especial String")
    print("Seleccione una opcion:\n")
    print("1. Iniciar")
    print("2. Salir")
    opcion=int(input("-->"))

    if opcion == 1:
        print("Ingresa un elemento: ")
        valor1=input("-->")
        print("Ingresa el siguiente elemento: ")
        valor2=input("-->")
        print("\n")

        object=MetodoSTR(valor1,valor2)
        print("-"*15)
        print(object)
        print("-"*15)

    elif opcion == 2:
        print("OPERATION CANCELLED (0x037717)")
        break

    else:
        print("Opcion Invalida")