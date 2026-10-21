from math import cos, radians, sin
from ascii_grid import AsciiGrid
from pygame import math as m
from settings import GRAVITY as G, grid_to_screen, screen_to_grid, GRID_DIMENSIONS as DIMS


class Cannonball:
    def __init__(self, player, x, y, init_vel: m.Vector2):
        self.screen_pos = m.Vector2(x,y)
        self.pos = screen_to_grid(x,y)
        self.player = player
        self.texture = AsciiGrid(1,1,self.pos[0],self.pos[1])
        self.texture.set_texture("O",self.player+1)
        self.vel = init_vel.copy()

        self.exploded = False

    def update(self):
        self.vel.y += G
        self.screen_pos += self.vel

        self.pos = screen_to_grid(self.screen_pos.x, self.screen_pos.y)

    def display(self, grid: AsciiGrid):
        # print("cannon",self.pos[0],self.pos[1])
        grid.blit(self.texture,self.pos[0],self.pos[1])

    def off_screen_x(self):
        return self.pos[0] < 0  or self.pos[0] >= DIMS[0]

    def above_screen(self):
        return self.pos[1] < 0

    def below_screen(self):
        return self.pos[1] >= DIMS[1]

    def should_remove(self):
        return self.exploded or self.off_screen_x() or self.below_screen()