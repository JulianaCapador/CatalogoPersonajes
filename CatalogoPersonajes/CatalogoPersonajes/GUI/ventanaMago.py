'''
Created on 16/10/2017

@author: juliana
'''

import pygame

def main():
    pygame.init() #inicializacion de todos los modulos
    pantalla = pygame.display.set_mode([700,700]) #fijacion del tamano de la ventana
    pygame.display.set_caption("Catalogo de Personajes")    
    salir = False
    reloj1=pygame.time.Clock()

    mago = pygame.image.load("mago.png")
    cetro = pygame.image.load("cetroMago.png")
    habil = pygame.image.load("habilidadMago.png")
    escudoM = pygame.image.load("escudoMago.png")

    while salir != True: #Loop Principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                
        reloj1.tick(20)
        pantalla.blit(mago,(50,20))
        pantalla.blit(cetro,(170,20))
        pantalla.blit(habil,(300,20))
        pantalla.blit(escudoM,(500,20))
        pygame.display.update()
    
    pygame.quit()
    
main()