'''
Created on 17/09/2017

@author: juliana
'''

from __future__ import generators

class Shape(object):
  
    def factory(type):

        if type == "Orco": return Orco()
        if type == "Elfo": return Elfo()
        if type == "Mago": return Mago()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Orco(Shape):
    def draw(self): print("Orco creado")
    

class Elfo(Shape):
    def draw(self): print("Elfo creado")
    

class Mago(Shape):
    def draw(self): print("Mago creado")
    
    
opcion = input("Cual desea crear:  \n 1. Orco 2. Elfo 3. Mago \n")
if (opcion == "1"):  
    obj1 = Shape.factory("Orco")
    obj1.draw()
elif(opcion == "2"):
    obj2 = Shape.factory("Elfo")
    obj2.draw()
else:
    obj3 = Shape.factory("Mago")
    obj3.draw()




