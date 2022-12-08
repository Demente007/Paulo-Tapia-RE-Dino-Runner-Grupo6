from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    pos_bird_y = [150, 340, 250]
    def __init__(self, image): 
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.pos_bird_y)
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1 

    
