from ascii_grid import AsciiGrid
from pygame.key import get_pressed as get_pressed_keys
from pygame import K_LEFT, K_RIGHT, K_a, K_d
from load_ascii import load_ascii
from settings import grid_to_screen, res_path, MOUSE as mouse
from aimer import Aimer
from cannonball import Cannonball

RIGHT = 0
LEFT = 1

STRINGS = [None]*2
CANNON_OFFSET = [(0,0)]*2

STRINGS[RIGHT], width, height = load_ascii(res_path("res/AsciiArt/Ship/side-right"))
SIZE = (width, height)
CANNON_OFFSET[RIGHT] = (11,2)

STRINGS[LEFT],_,_ = load_ascii(res_path("res/AsciiArt/Ship/side-left"))
CANNON_OFFSET[LEFT] = (0,2)



# def get_vector(dir,reverse=1):
#     if dir == UP:
#         return (0,-reverse)
#     elif dir == LEFT:
#         return (-reverse, 0)
#     elif dir == DOWN:
#         return (0,reverse)
#     elif dir == RIGHT:
#         return (reverse,0)



class Ship:
    def __init__(self, x, y, player=1):
        self.x = x
        self.y = y
        self.player = player
        self.cannonball = None
        self.textures = [None]*2
        for i in range(2):
            self.textures[i] = AsciiGrid(SIZE[0], SIZE[1], self.x, self.y)
            self.textures[i].set_texture(STRINGS[i],8)

        self.dir = RIGHT
        self.aimer = Aimer(self.get_cannon_pos())

    # def get_current_center_pos(self):
    #     return (CENTERS[self.dir][0] + self.x, CENTERS[self.dir][1] + self.y)

    def get_cannon_pos(self):
        return self.x+CANNON_OFFSET[self.dir][0],self.y+CANNON_OFFSET[self.dir][1]

    def display(self, grid: AsciiGrid):
        cent_x = self.x
        cent_y = self.y
        grid.blit(self.textures[self.dir],cent_x, cent_y)
        self.aimer.display(grid)

        if (self.cannonball is not None):
            self.cannonball.display(grid)

    def move(self, vec):
        self.x += vec[0]
        self.y += vec[1]
        for text in self.textures:
            text.move(vec[0],vec[1])
        self.aimer.set_pos(self.get_cannon_pos())
        self.aimer.update(True)
        

    # def rotate(self, dir):
    #     self.dir = (self.dir + dir) % 4
    def shoot_cannonball(self):
        x,y = self.get_cannon_pos()
        screenx, screeny = grid_to_screen(x,y)
        self.cannonball = Cannonball(self.player,screenx,screeny,self.aimer.get_init_vel())


    def update(self):
        keys = get_pressed_keys()

        if keys[K_LEFT] or keys[K_a]:
            #self.dir = LEFT
            self.move((-1,0))
        elif keys[K_RIGHT] or keys[K_d]:
            #self.dir = RIGHT
            self.move((1,0))
            
        self.aimer.set_pos(self.get_cannon_pos())
        #mouse = pygame.mouse.get_pos()
        self.aimer.update()

        if (self.cannonball is not None and self.cannonball.should_remove()):
            self.cannonball = None

        if (mouse.double_clicked and self.cannonball is None):
            self.shoot_cannonball()

        if (self.cannonball is not None):
            self.cannonball.update()
        
    