'''
Created on 20/09/2017

@author: juliana
'''

class Director:
    def __init__(self):
        self.builder = None
        
    def SetBuilder(self, builderObj):
        self.builder = builderObj
        
    def Construct (self, name):
        if name == "OrcoArmado":
            self.builder.Create()
            self.builder.BuildPartA()
            self.builder.BuildPartB()
        
        elif name == "ElfoArmado":
            self.builder.Create()
            self.builder.BuildPartC()
            self.builder.BuildPartD()
            
        elif name == "MagoArmado":
            self.builder.Create()
            self.builder.BuildPartC()
            self.builder.BuildPartD()   
            
class Builder:
    
    def Create(self):
        raise NotImplementedError("Create()must defined in subclass")
    def BulidPArtA(self):
        raise NotImplementedError("BuildPartA()must defined in subclass")
    def BulidPArtB(self):
        raise NotImplementedError("BuildPartB()must defined in subclass")
    def BulidPArtC(self):
        raise NotImplementedError("BuildPartC()must defined in subclass")
    def BulidPArtD(self):
        raise NotImplementedError("BuildPartD()must defined in subclass")
     