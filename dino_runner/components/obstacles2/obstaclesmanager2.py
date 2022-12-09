import pygame
from dino_runner.components.obstacles2.headobstacle import Head, HEAD_OBSTACLE
from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.bird import Bird
from dino_runner.utils.constants import HEAD_OBSTACLE
import random

class ObstacleManager2:
    def __init__(self):
        self.obstacles2= []

    def update(self, game, player):
        if len(self.obstacles2) == 0:
            self.obstacles2.append(Head(HEAD_OBSTACLE))

        for obstacle in self.obstacles2:
            obstacle.update(game.game_speed, self.obstacles2)
            if game.player.dino_rect.colliderect(obstacle.rect):
                    self.obstacles2 = []
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count == 0:
                        pygame.time.delay(500)
                        game.level_2 = False
                        game.playing = False
                        game.death_count += 1
                        break


    def draw(self, screen):
        for obstacle in self.obstacles2:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):  # lo vamos a llamar en el game
        self.obstacles = []