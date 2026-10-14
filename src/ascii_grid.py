import array
from settings import COLOR_BITS as SHIFT, BITMASK as MASK

#just the grid, no font stuff
class AsciiGrid:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.grid = array.array('I', [0] * (width * height))

    def get_idx(self, x, y) -> int:
        if not self.is_in_bounds(x,y):
            raise IndexError(f"Position ({x},{y}) is out of bounds of grid ({self.width},{self.height}).")
        return y*self.width + x

    def set(self, x, y, char, col):
        idx = self.get_idx(x,y)
        char_int = ord(char)
        self.grid[idx] = (char_int << SHIFT) | (col & MASK)

    def set_col(self, x, y, col):
        idx = self.get_idx(x,y)
        packed = self.grid[idx]
        char_int = packed >> SHIFT
        self.grid[idx] = (char_int << SHIFT) | (col & MASK)

    def set_idx(self, idx, char, col):
        char_int = ord(char)
        self.grid[idx] = (char_int << SHIFT) | (col & MASK)

    def set_packed(self, x, y, packed):
        idx = self.get_idx(x, y)
        self.grid[idx] = packed

    def get(self, x, y):
        idx = self.get_idx(x, y)
        packed = self.grid[idx]
        char = chr(packed >> SHIFT)
        col = packed & MASK
        return char, col

    def get_packed(self, x, y):
        idx = self.get_idx(x,y)
        return self.grid[idx]

    def set_texture(self, data: str, col):
        for index, char in enumerate(data):
            self.set_idx(index, char, col)

    def is_in_bounds(self, x, y):
        return (x >= 0 and x < self.width and y >= 0 and y < self.height)


    def blit(self, object, x_pos = None, y_pos = None):
        if x_pos == None:
            x_pos = object.x
        if y_pos == None:
            y_pos = object.y
        for y in range(object.height):
            for x in range(object.width):
                tar_x = x_pos + x
                tar_y = y_pos + y
                if self.is_in_bounds(tar_x, tar_y):
                    char,col = object.get(x,y)
                    if char == ' ' or char == '\x00':
                        continue
                    self.set(tar_x, tar_y, char, col)
                    

    def move(self, xoff, yoff):
        self.x += xoff
        self.y += yoff

    def move_to(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    

