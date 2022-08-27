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

class Bullet(pygame.sprite.Sprite):

    def __init__(self, groups, x, y):
        super().__init__(groups)

        self.image_list = []
        for i in range(1):
        # Bullet image
            image = pygame.image.load(image_pbl)
            self.image_list.append(image)
        
        # Bullet image settings
        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (24, 48))
        self.rect = self.image.get_rect(midbottom = (x, y))
    
        # Bullet Speed
        self.speed = 8
    
    def check_off_screen(self):
        if self.rect.bottom < 0:
            self.kill()
    
    def move(self):
        self.rect.y -= self.speed
    
    def update(self):
        self.move()
        self.check_off_screen()
