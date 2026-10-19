from math import floor
from ascii_grid import AsciiGrid
from settings import FONT_SIZE as CHAR_H, CHAR_WIDTH as CHAR_W, GRAVITY as G, MAX_VEL, screen_to_grid, grid_to_screen
from settings import MOUSE as mouse
import pygame
import pygame.math as m

def calc_grid_pt(screenx, screeny):
    x = floor(screenx / CHAR_W)
    y = floor(screeny / CHAR_H)
    return x, y

def lerp_grid_pt(x1, y1, x2, y2, percent):
    x = x1 + (x2-x1)*percent
    y = y1 + (y2-y1)*percent
    return round(x),round(y)

def projectile_formula(y0,vel,x):
    vx = vel.x
    vy = vel.y
    if abs(vx) <= 0.01:
        return y0
    return y0 + (vy/vx)*x + (G / (2*vx*vx)) * (x*x)

def calc_x_pos(idx, velx):
    return (idx+1)*(velx)

class Aimer:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.screen_pos = grid_to_screen(self.x, self.y)
        self.points = [AsciiGrid(1,1,self.x,self.y) for _ in range(3)]
        for pt in self.points:
            pt.set_texture("●",1)
        #self.target = AsciiGrid(1,1,self.x,self.y)
        #self.target.set_texture("X",1)

        self.init_vel_vec = m.Vector2(0,0)
        self.mouse_vec = m.Vector2(0,0)

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def set_pts(self):
        for pt in self.points:
            pt.move_to(self.x,self.y)
        #self.target.move_to(self.x,self.y)


    def update(self, force_update = False):
        self.screen_pos = grid_to_screen(self.x, self.y)
        mouse.update()
        if (mouse.is_dragging() or force_update):
            self.update_pts()
        #if (mouse.double_clicked):


    def update_pts(self):
        self.mouse_vec = m.Vector2(mouse.x - self.screen_pos[0], mouse.y - self.screen_pos[1])
        if (self.mouse_vec.y > 0):
            self.mouse_vec.update(self.mouse_vec.x, 0)
        self.init_vel_vec = self.mouse_vec * 0.005 * MAX_VEL
        self.init_vel_vec.clamp_magnitude_ip(MAX_VEL)

        
        for idx,pt in enumerate(self.points):
            pt.x = self.x
            pt.y = self.y
            
            sx,sy = grid_to_screen(pt.x, pt.y)
            
            disp = calc_x_pos(idx,self.init_vel_vec.x)
            sx += disp
            print(pt.x,sx,pt.y,sy)
            sy = projectile_formula(sy, self.init_vel_vec, disp)
            pt.x, pt.y = screen_to_grid(sx,sy)
            #print(sx,sy)

    def get_init_vel(self):
        return self.init_vel_vec.copy()
    

    def display(self, grid: AsciiGrid):
        for pt in self.points:
            grid.blit(pt)
        #grid.blit(self.target)