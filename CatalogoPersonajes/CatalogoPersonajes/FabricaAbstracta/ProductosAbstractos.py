'''
Created on 8/10/2017

@author: Juliana Alexandra Capador Ochoa
'''

#productos
class Producto():
    def __init__(self, nombre):
        self.nombre = ""

    def imprimir(self):
        print (self.nombre)

class Arma(Producto):
    def __init__(self, nombre):
        self.nombre = "Arma: " + nombre

class Escudo(Producto):
    def __init__(self, nombre):
        self.nombre = "Escudo: " + nombre

class Habilidad(Producto):
    def __init__(self, nombre):
        self.nombre = "Habilidad: " + nombre
        
#Productos Orco
class ArmaOrco(Arma):
    pass

class EscudoOrco(Escudo):
    pass

class HabilidadOrco(Habilidad):
    pass

#Productos Elfo
class ArmaElfo(Arma):
    pass

class EscudoElfo(Escudo):
    pass

class HabilidadElfo(Habilidad):
    pass

#Productos Mago
class ArmaMago(Arma):
    pass

class EscudoMago(Escudo):
    pass

class HabilidadMago(Habilidad):
    pass

# fabricas
class FabricaAbstracta():
    def getArma(self):
        pass

    def getEscudo(self):
        pass

    def getHabilidad(self):
        pass

class FabricaOrco(FabricaAbstracta):
    def getArma(self):
        return ArmaOrco("Mazo")

    def getEscudo(self):
        return EscudoOrco("Targa")

    def getHabilidad(self):
        return HabilidadOrco("Golpear")


class FabricaElfo(FabricaAbstracta):
    def getArma(self):
        return ArmaElfo("Arco y flechas")

    def getEscudo(self):
        return EscudoElfo("Broquel")

    def getHabilidad(self):
        return HabilidadElfo("Agilidad")

class FabricaMago(FabricaAbstracta):
    def getArma(self):
        return ArmaElfo("Cetro Infernal")

    def getEscudo(self):
        return EscudoElfo("Escudo energetico")

    def getHabilidad(self):
        return HabilidadElfo("Lanzar llamas")

opcion = raw_input(" 1 orcos - 2 elfos - 3 Magos\n")

if opcion == "1":
    fabrica = FabricaOrco()
elif(opcion == "2"):
    fabrica = FabricaElfo()
elif(opcion == "3"):
    fabrica = FabricaMago()
else :
    print("Seleccione una opcion correcta")

arma = fabrica.getArma() 
escudo = fabrica.getEscudo()
habilidad = fabrica.getHabilidad()

arma.imprimir()
escudo.imprimir()
habilidad.imprimir()
