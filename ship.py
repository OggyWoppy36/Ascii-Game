from ascii_grid import AsciiGrid
import pygame
from load_ascii import load_ascii
from settings import res_path

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3



STRINGS = [None]*4
SIZES = [(0,0)]*4
CENTERS = [(0,0)]*4

STRINGS[UP], width, height = load_ascii(res_path("AsciiArt/Ship/up"))
SIZES[UP] = (width, height)
CENTERS[UP] = (2,3)

STRINGS[RIGHT], width, height = load_ascii(res_path("AsciiArt/Ship/right"))
SIZES[RIGHT] = (width, height)
CENTERS[RIGHT] = (5,1)

STRINGS[DOWN], width, height = load_ascii(res_path("AsciiArt/Ship/down"))
SIZES[DOWN] = (width, height)
CENTERS[DOWN] = (2,2)

STRINGS[LEFT], width, height = load_ascii(res_path("AsciiArt/Ship/left"))
SIZES[LEFT] = (width, height)
CENTERS[LEFT] = (6,1)



def get_vector(dir,reverse=1):
    if dir == UP:
        return (0,-reverse)
    elif dir == LEFT:
        return (-reverse, 0)
    elif dir == DOWN:
        return (0,reverse)
    elif dir == RIGHT:
        return (reverse,0)



class Ship:
    def __init__(self, x, y, player=1):
        self.x = x
        self.y = y
        self.player = player

        self.textures = [None]*4
        for i in range(4):
            print(i)
            self.textures[i] = AsciiGrid(SIZES[i][0], SIZES[i][1], self.x, self.y)
            self.textures[i].set_texture(STRINGS[i],8)

        
        self.dir = RIGHT

    def display(self, grid: AsciiGrid):
        cent_x = self.x - CENTERS[self.dir][0]
        cent_y = self.y - CENTERS[self.dir][1]
        grid.blit(self.textures[self.dir],cent_x, cent_y)

    def move(self, vec):
        self.x += vec[0]*2
        self.y += vec[1]
        for text in self.textures:
            text.move(vec[0],vec[1])

    def rotate(self, dir):
        self.dir = (self.dir + dir) % 4

    def update(self):
        keys = pygame.key.get_just_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-1)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(1)
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(get_vector(self.dir,-1))
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(get_vector(self.dir))
    