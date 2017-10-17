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
    imagen = pygame.image.load("cetroMago.png")
    (x,y)=(50,50)
    #blanco = (255, 255, 255)
    fondo = pygame.image.load("personajes2.jpg")
    miFuente = pygame.font.SysFont('Algerian', 45)
    miTexto=miFuente.render("CATALOGO DE PERSONAJES",0,(5,4,4))
    
   
    
    while salir != True:  # Loop Principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                
        reloj1.tick(20)
        #pantalla.fill(blanco)
        pantalla.blit(fondo, (0, 0))  # imagen de fondo
        pantalla.blit(miTexto,(5,5))
        pygame.display.update()
        pantalla.blit(imagen,(x,y))
    
    pygame.quit()
main()
