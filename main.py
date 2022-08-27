#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by Okumura Naofumi
#=========================================================#

# System import
import pygame

# File import
from settings import *
from game import Game

# Init
pygame.init()

# Create Game Window
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Window Title
pygame.display.set_caption("Shooting Game ver2")

# Set up for FPS
# FPS -> set FPS = 60 in settings.py
clock = pygame.time.Clock()

# Loading Game
game = Game()

# Main Loop Space ==========================================

# If game is run
run = True

# Information log in cmd prompt
print(lt1)
print(lt2)
print(lt3)

while run:  # If keeping Run Game

    # Set Background Color
    screen.fill(BLACK)

    # Run Game
    game.run()

    # Getting Events
    for event in pygame.event.get():
        # Click "X" button
        if event.type == pygame.QUIT: # If click "x" button
            run = False # Game Quit and go without loop
        # Push "esc" key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # If get "esc" key
                run = False # Game Quit and go without loop
    
    # Update Display(or Window)
    pygame.display.update()
    clock.tick(FPS)

#===========================================================

pygame.quit() # If without loop(while run:) game is end
