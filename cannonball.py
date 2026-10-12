from ascii_grid import AsciiGrid
import pygame

class Cannonball:
    def __init__(self, player, x, y, dir):
        self.x = x
        self.y = y
        self.player = player
        self.texture = AsciiGrid(1,1,self.x,self.y)
        self.texture.set_texture(".",self.player+1)