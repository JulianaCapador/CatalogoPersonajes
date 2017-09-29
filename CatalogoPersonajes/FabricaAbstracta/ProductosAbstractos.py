'''
Created on 16/09/2017

@author: Juliana Alexandra Capador Ochoa
'''

class Equipamiento:
    def equipar(self,partes):
        pass
    
class EquiparOrco(Equipamiento):
    def equipar(self, partes):
        print("Orco tiene ",partes.action() )
        
class EquiparElfo(Equipamiento):
    def equipar(self, partes):
        print("Elfo tiene ",partes.action())
        
class EquiparHumano(Equipamiento):
    def equipar(self, partes):
        print("Humano tiene ",partes.action())
        
class EscudoO:
    def action(self):
        print("Tarja")
        
class ArmaO:
    def action(self):
        print("Mazo")

class HabilidadO:
    def action(self):
        print("Golpes Criticos")
        
class EscudoE:
    def action(self):
        print("Broquel")
        
class ArmaE:
    def action(self):
        print("Arco y Flechas")
        
class HabilidadE:
    def action(self):
        print("Agilidad")
        
class EscudoM:
    def action(self):
        print("Escudo Energetico")
        
class ArmaM:
    def action(self):
        print("Cetro infernal")
        
class HabilidadM:
    def action(self):
        print("Lanzar llamas")

#Fabricas Concretas



    