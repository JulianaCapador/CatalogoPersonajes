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
    
obj1 = Shape.factory("Orco")
obj2 = Shape.factory("Elfo")
obj3 = Shape.factory("Mago")
    
obj1.draw()
obj2.draw()
obj3.draw()

