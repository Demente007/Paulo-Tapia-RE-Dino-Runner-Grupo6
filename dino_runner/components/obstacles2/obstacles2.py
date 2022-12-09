from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite

class Obstacle2(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = 0
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, Obstacle):
        self.rect.x -= game_speed
        self.rect.x += 5
        if self.rect.x < -self.rect.width:
            Obstacle.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)