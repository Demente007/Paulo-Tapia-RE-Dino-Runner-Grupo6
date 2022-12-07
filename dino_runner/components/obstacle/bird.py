from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random


class Bird(Obstacle):
    def __init__(self, image): 
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1 

    
