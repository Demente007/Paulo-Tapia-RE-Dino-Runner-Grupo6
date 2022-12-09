import pygame
from dino_runner.components.obstacle.largeCactus import LargeCactus
from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.azar = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if self.azar == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.azar == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif self.azar == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                #pygame.time.delay(100)
               # game.playing = False                  #en la colision el juego termina
    
                #break                                            #rompemos el while
                if not game.player.shield:
                    pygame.time.delay(100)
                    self.obstacles = []

                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000

                    else : 
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    self.obstacles.remove(obstacle)



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):  # lo vamos a llamar en el game
        self.obstacles = []