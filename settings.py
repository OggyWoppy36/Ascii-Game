SCREEN_DIMENSIONS = (1280, 720)
FONT_SIZE = 16
CHAR_WIDTH = FONT_SIZE // 2
GRID_DIMENSIONS = (SCREEN_DIMENSIONS[0] // CHAR_WIDTH, SCREEN_DIMENSIONS[1] // FONT_SIZE) #idk prob wrong


COLOR_PALETTE = [
    (0, 0, 0),       # 0: Black
    (255, 255, 255), # 1: White
    (255, 0, 0),     # 2: Red
    (0, 255, 0),     # 3: Green
    (0, 0, 255),     # 4: Blue
    (255, 255, 0),   # 5: Yellow
    (0, 35, 180),    # 6: Dark Blue
    (150,180,255),   # 7: Light Blue
    (160,120,10),    # 8: Brown
    (70,100,230),    # 9: Med Blue
] + [(200, 200, 200)] * (32-9)

COLOR_BITS = 6 # COLS = 2^COLOR_BITS = 32
