from modulo_inscripcion import Inscripcion
import csv

class ManejaInscripcion:
    __inscripciones= []
    
    def __init__(self):
        self.__inscripciones= []
        
    def mostrar_inscripciones(self):
        for i in range(len(self.__inscripciones)):
            print (i)
            
    def registrar_inscripcion(self,t,p):
        ins= Inscripcion(t,p)
        self.__inscripciones.append(ins)
        
    ''' def mostrar_inscripciones(self):
        for i in range(len(self.__inscripciones)):
            print (f"\n\n>>> INSCRIPCION {i+1} <<<")
            print (self.__inscripciones[i])''' 
            
    def buscar_inscripcion_por_DNI(self,DNI):
        lista_DNI= self.crea_lista_DNI()
        if (DNI in lista_DNI):
            i= self.get_indice(DNI,lista_DNI)
            taller= self.__inscripciones[i].get_taller_nombre()
            pago= self.__inscripciones[i].get_taller_monto()
            print (f"DNI: {DNI}\nTaller: {taller}")
            if (pago == 0):
                print ("Ya pagó")
            else:
                print (f"Adeuda ${pago}")
            
        else:
            print ("Ese DNI no está entre los inscriptos")
                
    def crea_lista_DNI(self):
        lista_aux= []
        for i in range(len(self.__inscripciones)):
            d= self.__inscripciones[i].get_persona_DNI()
            lista_aux.append(d)
            
        return lista_aux
    
    def get_indice(self,d,lista_d):
        i= 0
        while (d != lista_d[i]):
            i+=1
            
        return i
        
    def inscriptos_por_taller(self):
        idT= int(input("Ingrese ID de Taller: "))
        lista_Taller= self.crea_lista_ID_Talleres()
        j=1
        if (idT in lista_Taller):
            for i in range(len(self.__inscripciones)):
                if (self.__inscripciones[i].get_taller_ID() == idT):
                    print (f"\n>>> Alumno {j}")
                    self.__inscripciones[i].mostrar_datos_personas()
                    j+=1
        else:
            print ("Ese ID no corresponde a ningun taller")
            
    def crea_lista_ID_Talleres(self):
        lista_aux= []
        for i in range(len(self.__inscripciones)):
            Id= self.__inscripciones[i].get_taller_ID()
            lista_aux.append(Id)
            
        return lista_aux
        
    def registrar_pago(self,DNI):
        lista_DNI= self.crea_lista_DNI()
        if (DNI in lista_DNI):
             i= self.get_indice(DNI,lista_DNI)
             self.__inscripciones[i].confirmar_pago()
             print ("CURSO PAGADO")
        
    def generar_archivo(self): # Generar un nuevo archivo que contenga DNI, idTaller, fechaInsc y pago
        Datos= []
        Lista= []
        
        archivo_inscriptos= open('Inscriptos.csv','w', newline="")
        for i in range(len(self.__inscripciones)):
            dni= self.__inscripciones[i].get_persona_DNI()
            idTaller= self.__inscripciones[i].get_taller_ID()
            fechaIns= self.__inscripciones[i].get_fecha_inscripcion()
            pago= self.__inscripciones[i].estado_de_pago()
            
            if (pago == False):
                p = 'Adeuda'
            else:
                p = 'Pago'
                
            Lista= [str(dni),str(idTaller),str(fechaIns),str(p)]
            Datos.append(Lista)
            
        with archivo_inscriptos:
            writer= csv.writer(archivo_inscriptos)
            writer.writerows(Datos)
        print ("ARCHIVO INSCRIPTOS GUARDADOS")
        
        