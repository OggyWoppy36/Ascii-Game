from math import floor
from ascii_grid import AsciiGrid
from settings import FONT_SIZE as CHAR_H, CHAR_WIDTH as CHAR_W, GRAVITY as G, MAX_VEL, screen_to_grid, grid_to_screen
from settings import MOUSE as mouse
from pygame import math as m

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

def simulate_projectile(steps, x0, y0, vel):
    vx = vel.x
    vy = vel.y
    x = x0
    y = y0
    for i in range(steps):
        vy += G
        x += vx
        y += vy
    return x,y



class Aimer:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.screen_pos = grid_to_screen(self.x, self.y)

        self.points = [AsciiGrid(1,1, 0,0) for _ in range(4)]
        for pt in self.points:
            pt.set_texture("●",1)

        self.init_vel_vec = m.Vector2(0,0)
        self.mouse_vec = m.Vector2(0,0)

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def update(self, force_update = False):
        self.screen_pos = grid_to_screen(self.x, self.y)
        if (mouse.is_dragging() ):#or force_update):
            self.update_vel_vec()
            self.update_pts()
        #if (mouse.double_clicked):

    def update_vel_vec(self):
        self.mouse_vec = m.Vector2(mouse.x - self.screen_pos[0], mouse.y - self.screen_pos[1])
        if (self.mouse_vec.y > 0):
            self.mouse_vec.update(self.mouse_vec.x, 0)
        self.init_vel_vec = self.mouse_vec * 0.0025 * MAX_VEL
        self.init_vel_vec.clamp_magnitude_ip(MAX_VEL)

    def update_pts(self):
        for idx,pt in enumerate(self.points):
            # sx,sy = 0,0
            # disp = calc_x_pos(idx,self.init_vel_vec.x)
            # sx = disp
            # print(pt.x,sx,pt.y,sy)
            # sy = projectile_formula(sy, self.init_vel_vec, disp)
            # pt.x, pt.y = sx, sy
            pt.x, pt.y = 0, 0
            pt.x, pt.y = simulate_projectile((idx+1)*2, pt.x, pt.y, self.init_vel_vec)


    def get_init_vel(self):
        return self.init_vel_vec.copy()
    
    def reset(self):
        for pt in self.points:
            pt.x, pt.y = 0,0
        self.init_vel_vec = m.Vector2(0,0)
        self.mouse_vec = m.Vector2(0,0)

    def init_vel_mag_sq(self):
        return self.init_vel_vec.magnitude_squared()

    def display(self, grid: AsciiGrid):
        # for pt in self.points:
        #     print(str(self.x+pt.x),str(self.y+pt.y))
        #     grid.blit(pt, self.x + pt.x, self.y + pt.y)
        for pt in self.points:
            if (pt.x,pt.y) == (0,0):
                continue
            grid_x, grid_y = screen_to_grid(self.screen_pos[0] + pt.x, self.screen_pos[1] + pt.y)
            grid.blit(pt, grid_x, grid_y)