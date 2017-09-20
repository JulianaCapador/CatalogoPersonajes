'''
Created on 16/09/2017

@author: juliana
'''

     
class Personaje(object):
    def __init__(self):
        self.__crear = None
        
    def get_crear(self):
        return self.__crear
    
class Orco(Personaje):
    def __init__(self):
        self.__crear = "Orco"
        
class Elfo(Personaje):
    def __init__(self):
        self.__crear = "Elfo"

class Enano(Personaje):
    def __init__(self):
        self.__crear = "Enano" 
        
class Humano(Personaje):
    def __init__(self):
        self.__crear = "Humano"
        
class PersonajeFactory(object):
    @staticmethod
    def crear_Personaje(personaje_type):
        if personaje_type == "Orco":
            return Orco()
        if personaje_type == "Elfo":
            return Elfo()
        if personaje_type == "Enano":
            return Enano()
        if personaje_type == "Humano":
            return Humano()
        
class Principal:

    print("1. Orco")
    print("2. Elfo")
    print("3. Enano")
    print("4. Humano")
    
    opcion = input("seleccione una opcion")
    
    if opcion == 1:
        return 
        
        
    
       