import csv
from modulo_taller import TallerCapacitacion
from modulo_maneja_persona import ManejaPersona
from modulo_inscripcion import Inscripcion

class ManejaTaller:
    __talleres= []
    
    def __init__(self):
        self.__talleres= []
        
    def carga_talleres(self): # Carga los talleres desde un archivo 
        archivo_talleres= open("Talleres.csv")
        reader= csv.reader(archivo_talleres,delimiter=',')
        
        for fila in reader:
            if (len(fila) == 4):
                ta= TallerCapacitacion(int(fila[0]), fila[1], int(fila[2]),int(fila[3]))
                self.__talleres.append(ta)
                
    def mostrar_talleres(self): # Muestra los talleres disponibles
        for i in self.__talleres:
            print(i)
            print("\n")
            
    def inscribir_persona(self,persona,inscripcion):
        print ("\nTalleres Disponibles\n")
        
        ## MUESTRA TALLERES DISPONIBLES QUE TIENEN VACANTES ##
        
        for i in range(len(self.__talleres)):
                print (f"{i+1}- {self.__talleres[i].get_nombre()} (Vacantes: {self.__talleres[i].get_vacante()})")
        op= int(input("Ingrese opcion: "))
        
        if (op > 0 and op <= len(self.__talleres)):           
            if self.__talleres[i].get_vacante() > 0:
                print (f">>> Inscripcion de una persona al {self.__talleres[op-1].get_nombre()} <<<")
                nom= input("Ingrese nombre: ")
                direc= input("Ingrese dirección: ")
                doc= int(input("Ingrese DNI: "))
                
                per= persona.agregar_persona(nom,direc,doc)
                self.__talleres[op-1].modifica_vacante() # Resto una vacante
                inscripcion.registrar_inscripcion(per,self.__talleres[op-1])
                
            else:
                print ("No hay vacantes en {self.__talleres[op-1].get_nombre()}")
        else:
            print ("Opcion Incorrecta, intente nuevamente")
            