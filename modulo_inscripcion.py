import datetime

class Inscripcion:
    __fechaInscripcion= None
    __pago= False
    __persona= None
    __taller= None
    
    def __init__(self,persona,taller):
        self.__fechaInscripcion= datetime.datetime.now()
        self.__pago= False
        self.__persona= persona
        self.__taller= taller
        
    def confirmar_pago(self):
        self.__pago= True
        
    def estado_de_pago(self):
        return self.__pago
    
    def get_fecha_inscripcion(self):
        return self.__fechaInscripcion
    
    def __str__(self):
        cadenaInscripcion = 'Fecha de Inscripcion: ' + str(self.__fechaInscripcion)
        if (self.__pago == False):
            cadenaInscripcion += '\nCurso Impago\n'
        else:
            cadenaInscripcion += '\nCurso Pagado\n'
            
        cadenaInscripcion += str(self.__persona.get_nombre()) + ' se inscribió al ' + str(self.__taller.get_nombre())
        return cadenaInscripcion
    
    def get_taller_nombre(self):
        return self.__taller.get_nombre()
    
    def get_taller_monto(self):
        if (self.__pago == False):
            res= self.__taller.get_montoInscripcion()
        else:
            res= 0
            
        return res
    
    def get_persona_DNI(self):
        return self.__persona.get_DNI()
    
    def get_taller_ID(self):
        return self.__taller.get_ID()
    
    def mostrar_datos_personas(self):
        print (self.__persona)