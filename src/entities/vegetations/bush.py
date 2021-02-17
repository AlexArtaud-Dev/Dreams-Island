from src.entities.vegetations.vegetation import Vegetation


class Bush(Vegetation):
    def __init__(self, x: int, y: int, path: str):
        super().__init__(x, y, path)
