from math import cos, radians, sin
from ascii_grid import AsciiGrid


def calculate_displacement(dir, power):
    x = round(cos(radians(dir)) * power)
    y = round(sin(radians(dir)) * power)
    return (x,y)

print(calculate_displacement(30,50))
class Cannonball:
    def __init__(self, player, x, y, dir, power):
        self.x = x
        self.y = y
        self.player = player
        self.texture = AsciiGrid(1,1,self.x,self.y)
        self.texture.set_texture(".",self.player+1)
        self.dir = dir
        self.power = power