class TallerCapacitacion:
    __idTaller= 0
    __nombre= ''
    __vacantes= 0
    __montoInscripcion= 0
    
    def __init__(self,idT,nom,vac,montoIns):
        self.__idTaller= idT
        self.__nombre= nom
        self.__vacantes= vac
        self.__montoInscripcion= montoIns
        
    def __str__(self):
        cadenaTaller = ("ID Taller: ")+ str(self.__idTaller)
        cadenaTaller += ("\nNombre: ")+ self.__nombre
        cadenaTaller += ("\nVacantes: ")+ str(self.__vacantes)
        cadenaTaller += ("\nMonto Inscripcion: ")+ str(self.__montoInscripcion)
        return cadenaTaller
   
    def get_ID(self):
        return self.__idTaller
    
    def get_nombre(self):
        return self.__nombre
    
    def get_vacante(self):
        return int(self.__vacantes)
    
    def get_montoInscripcion(self):
        return self.__montoInscripcion
    
    def modifica_vacante(self):
        self.__vacantes -= 1
