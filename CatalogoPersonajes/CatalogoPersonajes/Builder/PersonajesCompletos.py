'''
Created on 16/10/2017

@author: juliana
'''

import SimpleFactory.Personajes 
import FabricaAbstracta.ProductosAbstractos
from FabricaAbstracta.ProductosAbstractos import FabricaOrco, FabricaMago

builder = FabricaMago


class Constructor:
    
    def construirPersonaje(self):
        pass

class ConstructorConcreto(Constructor):
    
    def construirPersonaje(self):
        pass
 
class Director:
    
    def construirOrco(self):
        return FabricaMago()

