'''
Created on 17/09/2017

@author: juliana
'''

# Factory/shapefact1/ShapeFactory1.py
# A simple static factory method.
from __future__ import generators
import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        # return eval(type + "()")
        if type == "Orco": return Orco()
        if type == "Elfo": return Elfo()
        if type == "Humano": return Humano()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Orco(Shape):
    def draw(self): print("Orco creado")
    

class Elfo(Shape):
    def draw(self): print("Elfo creado")
    

class Humano(Shape):
    def draw(self): print("Humano creado")
    
    
# Generate shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = \
  [ Shape.factory(i) for i in shapeNameGen(1)]

for shape in shapes:
    shape.draw()
   
