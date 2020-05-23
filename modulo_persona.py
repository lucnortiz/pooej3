class Persona:
    __nombre= ''
    __direccion= ''
    __DNI= 0
    
    def __init__(self,nom,direc,dni):
        self.__nombre= nom
        self.__direccion= direc
        self.__DNI= dni
        
    def __str__(self):
        cadenaPersona = 'Nombre: '+ self.__nombre +'\nDireccion: '+ self.__direccion + '\nDNI: '+ str(self.__DNI)
        return (cadenaPersona)
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_DNI(self):
        return self.__DNI