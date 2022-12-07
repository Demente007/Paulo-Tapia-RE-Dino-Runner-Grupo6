import random 
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH
from pygame.sprite import Sprite

class Cloud(Sprite):
    def __init__(self):
        self.rect_x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect_y = random.randint(50, 100)
        self.image = CLOUD
        self.image_width = self.image.get_width()

    def update(self, game_speed):
        self.rect_x -= game_speed
        if self.rect_x < -self.image_width:
            self.rect_x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.rect_y = random.randint(50, 100)            

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))    #dibujame la image no me dibujes el secren que torpe que eres    