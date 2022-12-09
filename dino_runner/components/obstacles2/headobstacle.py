
from dino_runner.components.obstacles2.obstacles2 import Obstacle2
from dino_runner.utils.constants import HEAD_OBSTACLE
import random

class Head(Obstacle2):
    pos_head_y = [150, 340, 250]
    def __init__(self, image): 
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.pos_head_y)
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1 

    
