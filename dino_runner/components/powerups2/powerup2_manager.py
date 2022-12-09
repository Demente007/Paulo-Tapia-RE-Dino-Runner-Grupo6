import random 
import pygame
from dino_runner.components.powerups2.misil import Misil

class PowerUpManager2:
    
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0         #multiplicador de puntage
        self.option_numbers = list(range(1,10))  

    def reset_power_ups(self, points):
        self.power_ups = []  
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        
        if len(self.power_ups) == 0:
            self.when_appears = random.randint(self.when_appears+200, 500+self.when_appears)
            self.power_ups.append(Misil())
        return self.power_ups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                player.balas += 30
                player.show_text = True
                
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)