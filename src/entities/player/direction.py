from enum import Enum

# default =>


class Direction(Enum):
    LEFT = (-1, 0, +180)
    BOTTOM = (0, 1, -90)
    RIGHT = (1, 0, 0)
    TOP = (0, -1, +90)
