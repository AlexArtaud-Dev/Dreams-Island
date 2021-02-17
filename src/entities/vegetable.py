from pygame import image
from src.entities.consumable import Consumable


class Vegetable(Consumable):
    def __init__(self, name: str, tiredness: int, velocity: int, rotten: bool, seeds: int, exotic: bool, path: str):
        super().__init__(name, tiredness, velocity, seeds, path)
