
#from proyecto import *

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
        
    def tomar_datos(self):

        datos_contenido=["¿Cual es el ID del video ?","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Atributos del tema?" ]

        datos = []
           
        print(datos_contenido[0])
        id=str(input("->"))
        ap=id[1]
        ap=ap.lower()

        datos.append(id)

        if ap=="p":
            for i in range(1,6):
                print(datos_contenido[i])
                x=input("->")
                datos.append(x)
            datos.append(",,,")
                        

        elif ap=="s":
            for i in range(1,9):
                print(datos_contenido[i])
                x=input("->")
                datos.append(x)
            datos.append(",")

        elif ap=="d":
            for i in range(1,10):
                print(datos_contenido[i])
                x=input("->")
                datos.append(x)


        else:
            print("Numero de opcion invalida (ERR_002)")
           
        return datos



        


if __name__ == "__main__":
    loco=CSV()
    loco.escribir()


