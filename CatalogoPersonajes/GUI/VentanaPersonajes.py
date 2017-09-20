'''
Created on 20/09/2017

@author: juliana
'''

import pygame


def main():
    pygame.init()  # inicializacion de todos los modulos
    pantalla = pygame.display.set_mode([640, 640])  # fijacion del tamano de la ventana
    pygame.display.set_caption("Catalogo de Personajes")    
    salir = False
    reloj1 = pygame.time.Clock()
    blanco = (255, 255, 255)
    fondo = pygame.image.load("personajes2.jpg")
    
    
    while salir != True:  # Loop Principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                
        reloj1.tick(20)
        pantalla.fill(blanco)
        pantalla.blit(fondo, (0, 0))  # imagen de fondo
     

        pygame.display.update()
    
    pygame.quit()
main()
