from pygame import image


class Consumable(object):
    def __init__(self, name: str, tiredness: int, velocity: int, seeds: int, path: str):
        self.name = name
        self.tiredness = tiredness
        self.velocity = velocity
        self.image = image.load(path)
        self.seeds = seeds
