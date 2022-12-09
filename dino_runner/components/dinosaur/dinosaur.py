import pygame
from dino_runner.utils.constants import (RUNNING, 
DUCKING, JUMPING, FLY, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, JUMPING_HAMMER, RUNNING_HAMMER, DUCKING_HAMMER,
SONIC_DUCK,SONIC_JUMP,SONIC_RUN,TYPE_SONIC, DINO_DEAD, RUNNING_FINAL, MISIL)
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER , TYPE_SONIC:SONIC_DUCK}
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, TYPE_SONIC: SONIC_RUN}
        self.run_end = {DEFAULT_TYPE: RUNNING_FINAL}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, TYPE_SONIC:SONIC_JUMP}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect =  self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_fly = False           #dino volando false
        self.jump_vel = self.JUMP_VEL
        self.setup_state_booleans()
        self.despedida = False
        self.balas = 0
        self.image_misil = MISIL
        self.misil_rect = self.image_misil.get_rect()
        self.misil_rectx = self.X_POS
        self.misil_recty = self.Y_POS
        self.misil_atack = False

    def misil_atack_on(self):
        self.misil_rectx = self.X_POS
        self.misil_recty = self.Y_POS
        self.balas -= 1

    def draw_misil_on(self, screen):
        screen.blit(MISIL,(self.misil_rectx ,self.misil_recty))

    



    def setup_state_booleans(self):
        self.has_powerup = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
    def update(self, user_imput, game_speed):

        if self.dino_fly:
            self.fly()
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = False

        elif self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        elif self.dino_duck:
            self.duck()
        


        if user_imput[pygame.K_SPACE] and self.dino_fly:
            self.Y_POS -= 15

        elif user_imput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_imput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True 

        
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False 
            self.dino_jump = False
        
        if self.step_index >= 10:
            self.step_index = 0
            

        if user_imput[pygame.K_RIGHT]: # and self.dino_fly:
            if self.balas >0:
               self.misil_atack_on()
               self.misil_atack = True
        
    def run(self):
        self.image = self.run_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
    
    def run_final(self):
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 400
        self.step_index += 1
        if self.step_index >= 10:
             self.step_index = 0
        if self.dino_rect.x <550:
             self.X_POS += 1
        elif self.dino_rect.x >= 550 and self.dino_rect.x <552:
            self.image = DINO_DEAD
            self.X_POS +=0.05
        elif self.dino_rect.x >= 552:
            self.despedida = True
            
    def run_final2(self):
        self.type = DEFAULT_TYPE
        self.image = self.run_end[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 400
        self.step_index += 1
        if self.step_index >= 10:
             self.step_index = 0
        self.X_POS -=3

    
    def duck(self):
        self.image = self.duck_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def fly(self):
        self.image = FLY[0] if self.step_index < 5 else FLY[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
        self.Y_POS += 4

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.show_text:
                    fond = pygame.font.Font('freesansbold.ttf', 18)
                    text = fond.render(f"POWER ENABLE FOR {time_to_show}", True, (0,0,0))
                    textRect = text.get_rect()
                    textRect.center = (500,40)
                    screen.blit(text, textRect)
            else:
                self.shield = False 
                self.type = DEFAULT_TYPE         # S
                #self.update_to_default(SHIELD_TYPE)



'''def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE'''
        
