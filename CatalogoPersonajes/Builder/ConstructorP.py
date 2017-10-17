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
        if name == "Product1":
            self.builder.Create()
            self.builder.BuildPartA()
            self.builder.BuildPartB()
        
        elif name == "Product2":
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
    
class ConcreteBuilder1 (Builder):
    def __init__(self):
        self.product = None
        
    def Create(self):
        self.product = Product1()
        
    def BuildPartA(self):
        pass    
    
    def BuildPartB(self):
        pass    
    
    def BuildPartC(self):
        pass    
    
    def BuildPartD(self):
        pass    
    
    def getProduct(self):
        return self.product
    
class ConcreteBuilder2 (Builder):
    
    def __init__(self):
        self.product = None
    
        
    def Create(self):
        self.product = Product2()
        
    def BuildPartA(self):
        pass    
    
    def BuildPartB(self):
        pass    
    
    def BuildPartC(self):
        pass    
    
    def BuildPartD(self):
        pass    
    
    def getProduct(self):
        return self.product
    
class Product1:
    
    def UseProduct(self):
        print("Inside Product 1: Use Product()")
        

class Product2:
    
    def UseProduct(self):
        print("Inside Product 1: Use Product()")
        
director = Director()

builder1 = ConcreteBuilder1()
director.SetBuilder(builder1)
director.Construct('Product1')

prod1 = builder1.getProduct()
prod1.UseProduct()

builder2 = ConcreteBuilder2()
director.SetBuilder(builder2)
director.Construct('Product2')

prod2 = builder2.getProduct()
prod2.UseProduct()


        