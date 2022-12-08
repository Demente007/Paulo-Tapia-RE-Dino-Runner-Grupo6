from dino_runner.components.player_hearts.heart import Heart     #importamos clase heart
from dino_runner.utils.constants import HEART_COUNT             #importamos el contador

class PlayerHeartMananger:     

    def __init__(self):              
        self.heart_count = HEART_COUNT

    def reduce_heart(self):       #funcion para reducir los corazones
        self.heart_count -= 1

    def draw(self, screen):   #dibujamos
        x_position = 10 
        y_position = 20
        for counter in range(self.heart_count):  #usamos un contador 
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30                       #actulizamos los corazones para que vayan recorriendo    

    def reset_hearts(self):
        self.heart_count = HEART_COUNT      #reseteamos para cuando reinicie vuelva a lo de antes