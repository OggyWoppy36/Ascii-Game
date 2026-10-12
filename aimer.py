from ascii_grid import AsciiGrid

class Aimer:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.points = [None]*3
        for pt in self.points:
            pt = AsciiGrid(1,1,self.x,self.y)
            pt.set_texture(".",(255,255,255))