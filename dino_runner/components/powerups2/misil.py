from dino_runner.utils.constants import CARTUCHOS
from dino_runner.components.powerups2.powerups2 import PowerUp2

class Misil(PowerUp2):
    def __init__(self):
        self.image = CARTUCHOS

        super(Misil, self).__init__(self.image)    