import pygame
from ascii_grid import AsciiGrid
from settings import res_path,FRAMERATE,SCREEN_DIMENSIONS as SCREEN_DIMS, FONT_SIZE, GRID_DIMENSIONS as GRID_DIMS, COLOR_PALETTE
from ship import Ship
from mouse_tracker import MouseTracker
import random

pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode(SCREEN_DIMS)
font = pygame.Font(res_path("res/CONSOLA.TTF"), FONT_SIZE)
pygame.display.set_caption("Ascii Renderer")
clock = pygame.time.Clock()

screen_grid = AsciiGrid(GRID_DIMS[0], GRID_DIMS[1])
sea = AsciiGrid(screen_grid.width, screen_grid.height-25, 0, 25)
sea.set_texture("~"*(sea.width*sea.height),6)
sea.set_texture("".join(random.choices("SRHGB",k=(sea.width*sea.height))),6)
for x in range(sea.width):
    sea.set(x,0,"S",6)

sky = AsciiGrid(screen_grid.width, 25, 0, 0)
sky.set_texture("@" * sky.width*sky.height, 7)
ship = Ship(30,20)


def render(grid):
    for y in range(grid.height):
        for x in range(grid.width):
            char, col_idx = grid.get(x, y)
            if char != '\x00' and char != ' ' and char != 't':
                color = COLOR_PALETTE[col_idx % len(COLOR_PALETTE)]
                text_surface = font.render(char, True, color)
                screen.blit(text_surface, (x * char_w, y * FONT_SIZE))
            



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
            
    screen.fill(0)
    char_w = FONT_SIZE // 2
    
    screen_grid.blit(sea)
    screen_grid.blit(sky)
    ship.display(screen_grid)
    ship.update()
    
    
    render(screen_grid)
    pygame.draw.aaline(screen,"red",(ship.aimer.screen_pos[0],ship.aimer.screen_pos[1]),(ship.aimer.screen_pos[0]+ship.aimer.init_vel_vec.x,ship.aimer.screen_pos[1]+ship.aimer.init_vel_vec.y),3)
    pygame.display.flip()
    clock.tick(FRAMERATE)

pygame.quit()
