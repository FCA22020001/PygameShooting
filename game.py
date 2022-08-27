#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by Okumura Naofumi
#=========================================================#

# System import
import pygame
import random

# File import
from settings import *
from player import Player
from enemy import Enemy
from support import draw_text

# Game Core ===============================================
class Game: # Create game class

    def __init__(self):
        self.screen = pygame.display.get_surface()

        # Create Group = line38
        self.create_group()

        # Player
        self.player = Player(self.player_group, 300, 500, self.enemy_group)

        # Enemy
        self.timer = 0

        # Background images
        self.pre_bg_img = pygame.image.load(image_bg) # Set background image
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_height)) # Stretch background image
        self.bg_y = 0 # Background image's default index
        self.scroll_speed = 0.5 # Backgrounds image's scroll speed

        # Music
        pygame.mixer.music.load('assets/sounds/bgsong.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        # Gameover
        self.game_over = False
    
    # Create Group
    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle() # 1 player
        self.enemy_group = pygame.sprite.Group()    # Some Enemy

    # Create Enemy
    def create_enemy(self):
        self.timer += 1
        if self.timer > 50: # After 50 flame
            enemy = Enemy(self.enemy_group, random.randint(50, 550), 0, self.player.bullet_group) # Summon enemy limited random place ((x,x) = (50,550), y = 0)
            self.timer = 0
    
    # Death action
    def player_death(self):
        if len(self.player_group) == 0:
            self.game_over = True
            draw_text(self.screen, 'game over', screen_width // 2, screen_height // 2, 75, RED)
            draw_text(self.screen, 'press R KEY to reset', screen_width // 2, screen_height // 2 + 100, 50, RED)

    # Reset the game
    def reset(self):
        key = pygame.key.get_pressed()
        if self.game_over and key[pygame.K_r]:
            self.player = Player(self.player_group, 300, 500, self.enemy_group)
            self.enemy_group.empty()
            self.game_over = False
    
    # Scroll Background
    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height # (BackgroundStartPoint + 0.3) / WindowY
        self.screen.blit(self.bg_img,(0, self.bg_y - screen_height)) # Image 1 move to -600 ~ -1
        self.screen.blit(self.bg_img, (0, self.bg_y)) # Image 2 move to 0 ~ 599

    # Do the Game
    def run(self):
        # Do scroll
        self.scroll_bg()

        # Summon enemy
        self.create_enemy()

        # Death actions
        self.player_death()
        self.reset()

        # Display groups and update
        self.player_group.draw(self.screen)
        self.player_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()

#==========================================================

