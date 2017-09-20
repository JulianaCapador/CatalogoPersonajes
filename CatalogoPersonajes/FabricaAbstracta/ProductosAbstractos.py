'''
Created on 16/09/2017

@author: Juliana Alexandra Capador Ochoa
'''

class Equipar:
    def action(self): pass
    
class TipoPersonaje:
    def interactuaCon(self, equipar): pass
        
class CuerpoACuerpo(TipoPersonaje):
    def interactuaCon(self, equipar):
        print("Cuerpo a cuerpo tiene ", equipar.action())
        
class Distancia(TipoPersonaje):
    def interactuaCon(self, equipar):
        print("Distancia tiene", equipar.action())
        
class Magico(TipoPersonaje):
    def interactuaCon(self, equipar):
        print("Magico tiene", equipar.action())
        
class EscudoC(Equipar):
    def action(self):
        print("Tarja")
        
class ArmaC(Equipar):
    def action(self):
        print("Mazo")

class HabilidadC(Equipar):
    def action(self):
        print("Golpes Criticos")
        
class EscudoD(Equipar):
    def action(self):
        print("Broquel")
        
class ArmaD(Equipar):
    def action(self):
        print("Arco y Flechas")
        
class HabilidadD(Equipar):
    def action(self):
        print("Agilidad")
        
class EscudoM(Equipar):
    def action(self):
        print("Escudo Energetico")
        
class ArmaM(Equipar):
    def action(self):
        print("Cetro infernal")
        
class HabilidadM(Equipar):
    def action(self):
        print("Lanzar llamas")

# Fabrica Abstracta
class ElementosPersonaje:
    def crearEscudos(self):
        pass
    def crearArmas(self):
        pass
    def crearHabilidades(self):
        pass
    def tipo(self):
        pass
    
    
# Fabricas Concretas
class PCuerpoACuerpo(ElementosPersonaje):
    def crearEscudos(self):
        return  EscudoC()
    def crearArmas(self):
        return ArmaC()
    def crearHabilidades(self):
        return HabilidadC
    def tipo(self):
        return CuerpoACuerpo()
    
class PDistancia(ElementosPersonaje):
    def crearEscudos(self):
        return EscudoD()
    def crearArmas(self):
        return ArmaD()
    def crearHabilidades(self):
        return HabilidadD()
    def tipo(self):
        return Distancia()

class PMagico(ElementosPersonaje):
    def crearEscudos(self):
        return EscudoM()
    def crearArmas(self):
        return ArmaM()
    def crearHabilidades(self):
        return HabilidadM()
    def tipo(self):
        return Magico()
    
class AmbientePersonaje:
    def __init__(self, fabrica):
        
        self.fabrica = fabrica
        self.es = fabrica.crearEscudos()
        self.ar = fabrica.crearArmas()
        self.ha = fabrica.crearHabilidades()
        self.ti = fabrica.tipo()
        
    def realizarEscudos(self):
        self.ti.interactuaCon(self.es)
        
    def realizarArmas(self):
        self.ti.interactuaCon(self.ar)
        
    def realizarHabilidades(self):
        self.ti.interactuaCon(self.ha)

                
g1 = AmbientePersonaje(PCuerpoACuerpo())
g2 = AmbientePersonaje(PDistancia())
g3 = AmbientePersonaje(PMagico())

g1.realizarEscudos()
g2.realizarArmas()
g3.realizarHabilidades()

        
        
