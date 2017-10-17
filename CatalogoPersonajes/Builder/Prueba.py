'''
Created on 16/10/2017

@author: juliana
'''

class Director:
    def __init__(self):
        self.builder = None
        
    def SetBuilder(self, builderObj):
        self.builder = builderObj
        
    def Construct (self, name):
        if name == "Orco":
            self.builder.Create()
            self.builder.BuildPartA()
            self.builder.BuildPartB()
        
        elif name == "Elfo":
            self.builder.Create()
            self.builder.BuildPartC()
            self.builder.BuildPartD()
        
        elif name == "Mago":
            self.builder.Create()
            self.builder.BuildPartC()
            self.builder.BuildPartD()
        
            