import pygame      #importamos pygame
from dino_runner.utils.constants import (        
    HEART 
)    #accedemos a la imagen del corazon 

class Heart: 
    def __init__(self, x_position, y_position):      #constructor con las posicines de los corazones
        self.image = HEART                              #damos la imagen
        self.rect = self.image.get_rect()          #obtenemos el rectangulo
        self.rect.x = x_position           
        self.rect.y = y_position
        
    def draw(self, screen):      #dibujamos  y le pasamos la pantalla
        screen.blit(self.image, self.rect)   