from math import floor
from ascii_grid import AsciiGrid
from settings import FONT_SIZE as CHAR_H, CHAR_WIDTH as CHAR_W

def calc_grid_pt(screenx, screeny):
    x = floor(screenx / CHAR_W)
    y = floor(screeny / CHAR_H)
    return x, y

def lerp_grid_pt(x1, y1, x2, y2, percent):
    x = x1 + (x2-x1)*percent
    y = y1 + (y2-y1)*percent
    return round(x),round(y)

class Aimer:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.points = [AsciiGrid(1,1,self.x,self.y) for _ in range(3)]
        for pt in self.points:
            pt.set_texture("●",1)
        self.target = AsciiGrid(1,1,self.x,self.y)
        self.target.set_texture("X",1)

    def update_pts(self, mouseX, mouseY):
        tarx,tary = calc_grid_pt(mouseX,mouseY)
        self.target.move_to(tarx, tary)
        lerp_perc = 0.25
        for pt in self.points:
            x,y = lerp_grid_pt(self.x,self.y,tarx,tary,lerp_perc)
            pt.move_to(x,y)
            lerp_perc += 0.25

    def display(self, grid: AsciiGrid):
        grid.blit(self.target)
        for pt in self.points:
            grid.blit(pt)
        