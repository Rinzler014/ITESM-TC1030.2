
from proyecto import *

class PideValor():
        
    
    def tomar_datos(self):

        datos_pelicula=["¿Cual es el ID de la pelicula?","¿Cual es el titulo ?","¿Cual es su duración?","¿Cual es la Calicación?","¿Cual es la audiencia?","¿Cual es el genero?","¿Cual es la temporada?","¿Qué episodio es?","¿Título del episodio?", "¿Atributos del tema?" ]


        global datos 
        datos=[]
        
        #Se debe tener listo el metodo de despliegue
        op=int(input("->"))

        if op ==1:  
            print(datos_pelicula[0])
            id=str(input("->"))
            ap=id[1]
            ap=ap.lower()
       
            datos.append(id)
            if ap=="s":
                for i in range(1,9):
                    print(datos_pelicula[i])
                    x=input("->")
                    datos.append(x)
                
            elif ap=="p":
                for i in range(1,6):
                    print(datos_pelicula[i])
                    x=input("->")
                    datos.append(x)

            elif ap=="d":
                for i in range(1,10):
                    print(datos_pelicula[i])
                    x=input("->")
                    datos.append(x)



        
            

        elif op==2:
            pass
          
        elif op ==3:
            pass
            

        elif op==4:
            pass        

        elif op ==5:
            pass
        elif op==6:
            pass


        elif op==7:
            pass
        return datos



if __name__ == "__main__":
    yo=PideValor()
    a=yo.tomar_datos()
    print(a)
        



