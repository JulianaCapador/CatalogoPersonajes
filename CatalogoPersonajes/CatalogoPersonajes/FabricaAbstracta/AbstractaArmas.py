'''
Created on 8/10/2017

@author: juliana
'''
import __main__

class FabricaAbstracta():
    
    def crearArma(self):
        pass
    def crearEscudo(self):
        pass
    def crearHabilidad(self):
        pass

# Fabricas Concretas

class ArmarOrco(FabricaAbstracta):
    
    def crearArma(self):
        return ArmaOrco()        
    def crearEscudo(self):
        return EscudoOrco()
    def crearHabilidad(self):
        return HabilidadOrco()
        
class ArmarElfo(FabricaAbstracta):
    
    def crearArma(self):
        return ArmaElfo()
    def crearEscudo(self):
        return EscudoElfo()     
    def crearHabilidad(self):
        return HabilidadElfo()
        
class ArmarMago(FabricaAbstracta):
    
    def crearArma(self):
        return ArmaMago()
    def crearEscudo(self):
        return EscudoMago()   
    def crearHabilidad(self):
        return HabilidadMago()
        
# Partes
class Armas():
    def otorgarArma(self):
        pass
    
class ArmaOrco(Armas):
    def otorgarArma(self):
        print("Mazo")
class ArmaElfo(Armas):
    def otorgarArma(self):
        print("Arco y Flechas")
class ArmaMago(Armas):
    def otorgarArma(self):
        print("Cetro Infernal")

class Escudos():
    def otorgarEscudo(self):
        pass
    
class EscudoOrco(Escudos):
    def otorgarEscudo(self):
        print("Tarja")
class EscudoElfo(Escudos):
    def otorgarEscudo(self):
        print("Broquel")
class EscudoMago(Escudos):
    def otorgarEscudo(self):
        print("Escudo energetico")

class Habilidad():
    def otorgarHabilidad(self):
        pass
    
class HabilidadOrco(Habilidad):
    def otorgarHabilidad(self):
        print("Golpes criticos")
        
class HabilidadElfo(Habilidad):
    def otorgarHabilidad(self):
        print("Agilidad")
        
class HabilidadMago(Habilidad):
    def otorgarHabilidad(self):
        print("Lanzar llamas")
        
  
fabrica = FabricaAbstracta()
armitas = Armas()
escuditos = Escudos()
habil = Habilidad()

fabrica = ArmarOrco()


armitas = fabrica.crearArma()
escuditos = fabrica.crearEscudo()
habil = fabrica.crearHabilidad()

print(armitas.otorgarArma())
print(escuditos.otorgarEscudo())
print(habil.otorgarHabilidad())
        
fabrica = ArmarElfo()
armitas = fabrica.crearArma()
escuditos = fabrica.crearEscudo()
habil = fabrica.crearHabilidad()

print(armitas.otorgarArma())
print(escuditos.otorgarEscudo())
print(habil.otorgarHabilidad())


fabrica = ArmarMago()
armitas = fabrica.crearArma()
escuditos = fabrica.crearEscudo()
habil = fabrica.crearHabilidad()

print(armitas.otorgarArma())
print(escuditos.otorgarEscudo())
print(habil.otorgarHabilidad())

