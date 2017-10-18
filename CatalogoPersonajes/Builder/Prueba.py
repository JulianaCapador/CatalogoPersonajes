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
            self.builder.BuildPartE()
            self.builder.BuildPartF()
            
class Builder:
    
    def Create(self):
        raise NotImplementedError("Create()must defined in subclass")
    def BulidPartA(self):
        raise NotImplementedError("BuildPartA()must defined in subclass")
    def BulidPartB(self):
        raise NotImplementedError("BuildPartB()must defined in subclass")
    def BulidPartC(self):
        raise NotImplementedError("BuildPartC()must defined in subclass")
    def BulidPartD(self):
        raise NotImplementedError("BuildPartD()must defined in subclass")
    def BuildPartE(self):
        raise NotImplementedError("BuildPartD()must defined in subclass")
    def BuildPartF(self):
        raise NotImplementedError("BuildPartD()must defined in subclass")


    
        
            