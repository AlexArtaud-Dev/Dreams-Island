from enum import Enum
from pygame import image


class FlaskEffect(Enum):
    FREEZE = 0
    VELOCITY = 1
    TIREDNESS = 2


class Flask(object):
    def __init__(self, name: str, tiredness: int, velocity: int, health: int, path: str):
        self.velocity = velocity
        self.tiredness = tiredness
        self.health = health
        self.name = name
        self.image = image.load(path)
