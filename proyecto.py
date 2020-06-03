class Menu():
    def despliegue(self):
        print("Escoja  1.- aGRE ")
        op=int(input("->"))
        

class Videos():
    def __init__(self,ID,Titulo,Duracion,Calificacion):
        self.ID=ID
        self.Titulo=Titulo
        self.Duracion=Duracion
        self.Calificacion=Calificacion
    @classmethod        
    def pide_datos(self):
        pass

    def muestra_datos(self):
        pass

