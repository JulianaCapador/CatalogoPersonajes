'''
Created on 17/09/2017

@author: juliana
'''

# Factory/shapefact1/ShapeFactory1.py
# A simple static factory method.
from __future__ import generators

class Shape(object):
    # Create based on class name:
    def factory(type):
        # return eval(type + "()")
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
    
    
# Generate shape name strings:
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




