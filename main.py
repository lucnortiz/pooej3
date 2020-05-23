from modulo_maneja_persona import ManejaPersona
from modulo_maneja_taller import ManejaTaller
from modulo_maneja_inscripcion import ManejaInscripcion

from modulo_menu import Menu
import os

if __name__=='__main__':
    taller= ManejaTaller()
    persona= ManejaPersona()
    inscripcion= ManejaInscripcion()
    
    taller.carga_talleres()
    
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inscribir a una persona en un taller")
        print("2. Consultar Inscripcion por DNI\n3. Consultar inscriptos por taller")
        print("4. Registrar Pago\n5. Guardar inscripciones en un archivo")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, taller, persona, inscripcion)
        salir = op == 0
        
    print(salir)