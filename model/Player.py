from .Bomb import Bomb
from .Monster import Monster

class Player:
    name: str
    x: int
    y:  int
    color: str
    health: int

    def __init__(self, name: str, x: int, y: int, color: str, health: int):

        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.health = health

    def move_player(self, direction: str):

        '''This method moves the player according to  the arrow keys on a keyboard'''
        if direction == "up":
            self.y -= 1

        elif direction == "down":
            self.y += 1

        elif direction == "right":
            self.x += 1

        elif direction == "left":
            self.x -= 1

    def is_dead_bomb(self, b: Bomb):

        if b.x == self.x and b.y == self.y:
            self.health = 0

    def is_dead_monster(self, m: Monster):

        if m.x == self.x and m.y == self.y:
            self.health = 0
