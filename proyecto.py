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
