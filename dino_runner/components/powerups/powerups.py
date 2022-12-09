import random
from dino_runner.utils.constants import SCREEN_HEIGHT

from pygame.sprite import Sprite

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image               #pasaremos despues la imagen
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.x = SCREEN_HEIGHT + random.randint(400, 500)
        self.rect.y = random.randint(100, 150)            #variamos la altura donde apareceran
        self.start_time = 0 
        self.width = self.image.get_width()

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
            
