import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONDO_MENU, FONDO_GAME
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstaclesManager import ObstacleManager
from dino_runner.components.cloud.cloud import Cloud
from dino_runner.components.score_menu.text_utils import *
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartMananger

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.points = 0
        self.runing = True
        self.death_count = 0
        self.player_heart_manager = PlayerHeartMananger()

    def run(self):
        self.player.dino_fly = False
        self.player.Y_POS = 310
        self.obstacle_manager.reset_obstacles(self)
        self.player_heart_manager.reset_hearts()
        self.playing = True 
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()       #quitamos este envento para que funcione el menu 


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.runing = False

    def update(self): 
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.player.draw(self.screen)
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.score()
        self.player_heart_manager.draw(self.screen)     #dibujamos corazones
        pygame.display.update()
        pygame.display.flip()
    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0 
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1 

        if self.points == 200:
            self.player.dino_fly = True
        elif self.points < 400:
            self.player.dino_fly = False

        

        

        if self.points %  100 == 0 :
            self.game_speed += 1

        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)

    def show_menu(self):
        self.runing = True
        white_color = (FONDO_MENU)
        self.screen.blit(white_color, [0,0])
        self.print_menu_elements(self.death_count)
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count = 0):
        half_screen_heigth = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2

        if death_count == 0:
            text, text_rect = get_centered_message("Press any key to Start")
            self.screen.blit(text, text_rect)
        elif death_count > 0:
            text, text_rect = get_centered_message("Press any Key to Restart")
            score, score_rect = get_centered_message('Your Score: '+ str(self.points), heigth=half_screen_heigth+40)####### observacion
            death, death_rect = get_centered_message("your death: "+ str(self.death_count), heigth=half_screen_heigth+90)

            self.screen.blit(score,score_rect)     # imprimimos el socore y su rectangulo 
            self.screen.blit(text, text_rect)    #imprimimos el texto y su rectangulo'''
            self.screen.blit(death, death_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():     #for para obtener eventos
            if event.type == pygame.QUIT:         #si el evento es exit imprimimos dino bye
                print('Dino: Good bye!!')
                self.runing = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:   #si el evento detecta una tecla presionada empieza el juego
                self.points = 0                         # reseteamos los points del game
                self.game_speed = 20             #reseteamos la velocidad del juego
                self.run()




