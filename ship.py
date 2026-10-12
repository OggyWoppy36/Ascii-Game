from ascii_grid import AsciiGrid
import pygame
from enum import Enum, unique
from load_ascii import load_ascii
import array

@unique
class Facing(Enum):
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3



SHIP_STRINGS = [None]*4
SHIP_STRINGS[0] = load_ascii("AsciiArt/Ship/up")
SHIP_STRINGS[1] = load_ascii("AsciiArt/Ship/left")
SHIP_STRINGS[2] = load_ascii("AsciiArt/Ship/right")
SHIP_STRINGS[3] = load_ascii("AsciiArt/Ship/down")


class Ship:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.texture = AsciiGrid(SHIP_STRINGS[0][1],SHIP_STRINGS[0][2], self.x, self.y)
        self.texture.set_texture(SHIP_STRINGS[0][0],8)
        self.facing = Facing.RIGHT

    def display(self, grid: AsciiGrid):
        # if self.facing == Facing.LEFT:
        #     self.texture.set(5,0,"(",1)
        #     self.texture.set(6,0,"|",8)
        # elif self.facing == Facing.RIGHT:
        #     self.texture.set(5,0,"|",8)
        #     self.texture.set(6,0,")",1)
        grid.blit(self.texture,self.x,self.y)

    def move(self, xoff, yoff):
        self.x += xoff
        self.y += yoff
        self.texture.move(xoff,yoff)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move(-1,0)
            self.facing = Facing.LEFT
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move(1,0)
            self.facing = Facing.RIGHT
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(0,1)
            self.facing = Facing.DOWN
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(0,-1)
            self.facing = Facing.UP
    