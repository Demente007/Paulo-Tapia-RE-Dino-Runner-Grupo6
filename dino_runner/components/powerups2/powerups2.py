import random
from dino_runner.utils.constants import SCREEN_HEIGHT

from pygame.sprite import Sprite

class PowerUp2(Sprite):
    def __init__(self, image):
        self.image = image               #pasaremos despues la imagen
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(400, 500)
        self.rect.y = random.randint(50, 300)            #variamos la altura donde apareceran
        self.width = self.image.get_width()

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed
        self.rect.x += 15

        if self.rect.x < -self.rect.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
            
