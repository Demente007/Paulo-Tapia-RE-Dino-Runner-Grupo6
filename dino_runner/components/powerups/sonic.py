from dino_runner.utils.constants import POWER_SONIC,TYPE_SONIC
from dino_runner.components.powerups.powerups import PowerUp


class Sonic(PowerUp):
    def __init__(self):
        self.image = POWER_SONIC
        self.type = TYPE_SONIC
        super(Sonic, self).__init__(self.image, self.type)
