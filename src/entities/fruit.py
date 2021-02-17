from src.entities.consumable import Consumable


class Fruit(Consumable):
    def __init__(self, name: str, tiredness: int, velocity: int, seeds: int, path: str):
        super().__init__(name, tiredness, velocity, seeds, path)
