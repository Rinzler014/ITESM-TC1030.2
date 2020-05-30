#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Herencia Simple

#----CLASES----

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def __del__(self):
        pass

    def muestra(self):

        print("Nombre: ", self.nombre)
        print("Nombre: ", self.apellido)
        print("Nombre: ", self.edad)

class Estudiante(Persona):
    
    def __init__(self,mat,nom,ap,edad,car):
        self.mat=mat
        self.car=car
        #Dentro de la clase estudiante se ejecuta el contructor de la clase Persona
        super().__init__(nom,ap,edad)
    def muestra(self):

        #Llamando al metodo muestra de la clase persona
        super().muestra()
        if self.mat!="" and self.car!="":
            print("Matricula: ", self.mat)
            print("Carrera: ", self.car)


class Deportista(Estudiante):
    
    def __init__(self, mat, nom, ap, edad, car, deporte):
        self.deporte = deporte
        #Llamando al constructor de la clase estuduiante
        super().__init__(mat,nom,ap,edad,car)
    
    def muestra(self):
        
        #Llamando al metodo muestra de la clase estudiante
        super().muestra()
        print("Deporte: ", self.deporte)
        print("\n")


class Tallerista(Estudiante):

    def __init__(self, mat, nom, ap, edad, car, taller):

        self.taller = taller
        super().__init__(mat, nom, ap, edad, car)
    
    def muestra(self):

        super().muestra()
        print("Taller: ", self.taller)
        print("\n")



#----MAIN----

oe=Deportista("A01769410", "Ricardo", "Gonzalez", 25, "ITC", "Teatro")
oe.muestra()
print("-"*10)

oe_persona=Deportista("","Ricardo", "Gonzalez", "19", "", "Atletismo")
oe_persona.muestra()