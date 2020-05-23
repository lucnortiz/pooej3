
class Menu:
    __switcher=None
    
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            0:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, taller, persona, inscripcion):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(taller,persona,inscripcion)
        
    def salir(self):
        print('Programa Finalizado')
        
    def opcion1(self,taller,persona,inscripcion): # INSCRIBIR UNA PERSONA EN UN TALLER
        taller.inscribir_persona(persona,inscripcion)

    def opcion2(self,taller,persona,inscripcion): # CONSULTAR INSCRIPCION POR DNI
        dni = int(input("Ingrese DNI de la persona a buscar: "))
        inscripcion.buscar_inscripcion_por_DNI(dni)
        
    def opcion3(self,taller,persona,inscripcion): # CONSULTAR INSCRIPTOS
        inscripcion.inscriptos_por_taller()
    
    def opcion4(self,taller,persona,inscripcion): # REGISTRAR PAGO
         dni = int(input("Ingrese DNI: "))
         inscripcion.registrar_pago(dni)
         
    def opcion5(self,taller,persona,inscripcion): # GUARDAR INSCRIPCIONES
         inscripcion.generar_archivo()
    
    
    
    
    