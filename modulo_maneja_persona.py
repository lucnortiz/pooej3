from modulo_persona import Persona

class ManejaPersona:
    __personas= []
    
    def __init__(self):
        self.__personas= []

    def mostrar_personas(self):
        for i in range(len(self.__personas)):
            print (self.__personas[i])
            
    def agregar_persona(self,nom,direc,dni):
        persona= Persona(nom,direc,dni)
        self.__personas.append(persona)
        return persona
        