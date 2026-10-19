from settings import FRAMERATE

import pygame

class MouseTracker:
    def __init__(self):
        self.timer = 0
        self.dragging = False
        self.held = False
        self.drag_delta = (0,0)
        self.double_clicked = False
        #self.update()
        

    def update(self):
        mouse = pygame.mouse

        self.timer = max(0,self.timer-1)
        self.double_clicked = False
        self.dragging = False

        self.held = mouse.get_pressed()[0]
        
        new_pos = mouse.get_pos()
        if self.held:
            self.drag_delta = (new_pos[0]-self.x,new_pos[1]-self.y)
            self.dragging = self.drag_delta != (0,0)

        self.x = new_pos[0]
        self.y = new_pos[1]

        if (mouse.get_just_pressed()[0]):
            if (self.timer > 0):
                self.double_clicked = True
                self.timer = 0
            else:
                self.timer = 0.5*FRAMERATE # 0.5 seconds
        
    def is_held(self):
        return self.held

    def dragged(self):
        return self.drag_delta

    def is_dragging(self):
        return self.dragging



