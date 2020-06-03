
#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Actvidad en este programa: Validacion de Valores y Escritura de Datos

#----CLASES----

class CSV():

    def leer(self):
        name_file=str(input("Ingrese el nombre de su archivo: "))
        file_=open(name_file+".csv","r")
        _datos_lec=file_.readlines()
        _datos_lec.pop(0)
        file_.close()
        _datos_line=[]
        for line in _datos_lec:
            columna=line.split(",")
            for i in range (len(columna)):
                _datos_line.append(columna[i])
        
            
        return _datos_line
    
    
    def crear(self):
        print("Indique el nombre de su csv")
        name_file=str(input("->"))
        file_=open(name_file+".csv","w+")
        file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        return file_
        

    def escribir(self): 
        file_=self.leer()
        file_.append("\n")
        objeto=PideValor()
        x=objeto.tomar_datos()
        file_list=file_+x
        _file_=open("Prueba.csv","w+")
        _file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        for i in range (len (file_list)):
            if file_list[i]=="\n":

                _file_.write(file_list[i])
            else:
                _file_.write(file_list[i]+",")
        _file_.close()


class PideValor():

    def __init__(self, lim_in="", lim_sup="", tipo=""):
        self.lim_in     = lim_in
        self.lim_sup    = lim_sup
        self.tipo       = tipo
        
    def tomar_datos(self):
        
        while 1:

            datos_contenido=["¿Cual es el ID del video ?","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Atributos del tema?" ]

            datos = []
            
            print(datos_contenido[0])
            id=str(input("->"))
            ap=id[1]
            ap=ap.upper()

            datos.append(id)

            if ap == "P":
                for i in range(1,6):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                datos.append(",,,")
                return datos
                            
            elif ap == "S":
                for i in range(1,9):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                datos.append(",")
                return datos

            elif ap == "D":
                for i in range(1,10):
                    print(datos_contenido[i])
                    x=input("->")
                    datos.append(x)
                return datos

            else:
                print("No se pudo determinar el tipo de contenido")