#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by Okumura Naofumi
#=========================================================#

# System import
import pygame

def draw_text(screen, txt, x, y, size, color):
    font = pygame.font.Font(None, size)
    surface = font.render(txt, True, color)
    x = x - surface.get_width() / 2
    y = y - surface.get_height() / 2
    screen.blit(surface, (x, y))
    