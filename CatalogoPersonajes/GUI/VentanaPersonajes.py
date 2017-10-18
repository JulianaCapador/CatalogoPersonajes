'''
Created on 20/09/2017

@author: juliana
'''

import pygame

#cursor que es un rectangulo
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect. __init__(self,0,0,100,100)
    def update(self):
        self.left,self.top =pygame.mouse.get_pos()
#clase boton
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=300,y=300):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect= self.imagen_actual.get_rect()
        self.rectleft, self.rect.top = (x,y)
        
        
    def update(self,pantalla,cursor):  
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else: 
            self.imagen_actual = self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
  
def main():
    pygame.init()  # inicializacion de todos los modulos
    pantalla = pygame.display.set_mode([640, 640])  # fijacion del tamano de la ventana
    pygame.display.set_caption("Catalogo de Personajes")    
    salir = False
    reloj1 = pygame.time.Clock()
    
    btn1 = pygame.image.load("botoncito1.png")
    btn2 = pygame.image.load("botoncito2.png")
    boton1 = Boton(btn1,btn2,200,200)
    cursor1 = Cursor()
    
    blanco = (255, 255, 255)
    fondo = pygame.image.load("personajes2.jpg")
    miFuente = pygame.font.SysFont('Algerian', 45)
    miTexto=miFuente.render("CATALOGO DE PERSONAJES",0,(5,4,4))
    
    while salir != True:  # Loop Principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                
        reloj1.tick(20)
        pantalla.fill(blanco)
        pantalla.blit(fondo, (0, 0))  # imagen de fondo
        cursor1.update()
        boton1.update(pantalla,cursor1)

        
        pantalla.blit(miTexto,(5,5))
        pygame.display.update()
    
    pygame.quit()
main()
