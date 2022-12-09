import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONDO_MENU, FONDO_GAME, PORTAL, HEART, FONDO2
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstaclesManager import ObstacleManager
from dino_runner.components.cloud.cloud import Cloud
from dino_runner.components.score_menu.text_utils import *
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartMananger
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.obstacles2.obstaclesmanager2 import ObstacleManager2

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
        self.x_pos_portal = SCREEN_WIDTH
        self.y_pos_portal = -50
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.points = 0
        self.runing = True
        self.death_count = 0
        self.player_heart_manager = PlayerHeartMananger()
        self.power_up_manager = PowerUpManager()
        self.level_2 = False                             #activa el fondo en nivel 2
        self.level_1 = True
        self.x_pos_fondo2 = 0
        self.y_pos_fondo2 = 0
        self.obstacle_manager2 = ObstacleManager2()


    def run(self):
        self.player.dino_fly = False
        self.player.Y_POS = 310
        self.obstacle_manager.reset_obstacles(self)
        self.player_heart_manager.reset_hearts()
        self.points = 0                         # reseteamos los points del game
        self.game_speed = 20             #reseteamos la velocidad del juego
        self.power_up_manager.reset_power_ups(self.points)
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
        self.cloud.update(self.game_speed)
        if self.level_1:
            self.obstacle_manager.update(self , self.player)
            self.power_up_manager.update(self.points, self.game_speed, self.player)
        elif self.level_2:
            self.obstacle_manager2.update(self, self.player)





    def draw(self):
        self.clock.tick(FPS)
        self.score()
        if self.points >= 200 :           # dibujando el portal
            self.draw_portal()
        if self.level_2:
            self.fondo2()
            self.obstacle_manager2.draw(self.screen)
        elif self.level_1:
            self.fondo1()
        player_rect = pygame.draw.rect(self.screen, (0,0,0),((self.x_pos_portal + 200, self.y_pos_portal + 340), (50,50)))
        if self.player.dino_rect.colliderect(player_rect):
            pygame.time.delay(400)
            self.level_1 = False
            self.level_2 = True
            self.player.dino_fly = True
        self.player.draw(self.screen)
        self.player_heart_manager.draw(self.screen)     #dibujamos corazones

        pygame.display.update()
        pygame.display.flip()
    
    def fondo1(self):
        self.screen.fill((255,255,255))
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.draw_background()
        self.power_up_manager.draw(self.screen)

    def fondo2(self):
        self.screen.blit(FONDO2, (self.x_pos_fondo2, self.y_pos_fondo2))
        self.screen.blit(FONDO2, (SCREEN_WIDTH+self.x_pos_fondo2,self.y_pos_fondo2))
        if self.x_pos_fondo2 <= -1200:
            self.screen.blit(FONDO2, (SCREEN_WIDTH+self.x_pos_fondo2,self.y_pos_fondo2))
            self.x_pos_fondo2 = 0
        self.x_pos_fondo2 -= 1

        
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
        
        if self.points %  100 == 0 :
            self.game_speed += 1

        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)
        self.player.check_invincibility(self.screen)                  ###########

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
                self.level_1 =True
                self.level_2 =False
                self.run()

    def draw_portal(self):
        self.screen.blit(PORTAL, (self.x_pos_portal, self.y_pos_portal))
        self.x_pos_portal -= self.game_speed
    
