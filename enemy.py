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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, bullet_group):
        super().__init__(groups)

        # Create bullet group
        self.bullet_group = bullet_group

        self.image_list = []
        for i in range(1):
        # Enemy image
            image = pygame.image.load(image_enm)
            self.image_list.append(image)
        
        # Enemy image settings
        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))

        # Enemy move settings
        move_list = [1, -1]
        self.direction = pygame.math.Vector2((random.choice(move_list), 1))
        self.speed = 1
        self.timer = 0

        # Enemy hit-point
        self.health = 3
        self.alive = True
    
    # Enemy movements
    def move(self):
        self.timer += 1
        if self.timer > 80:
            self.direction.x *= -1
            self.timer = 0
        
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
    
    # Enemy auto kill
    def check_off_screen(self):
        if self.rect.top > screen_height:
            self.kill()
    
    # Enemy HP Manager
    def collision_bullet(self):
        for bullet in self.bullet_group:
            if self.rect.colliderect(bullet.rect):
                bullet.kill()
                self.health -= 1
        
        if self.health <= 0:
            self.alive = False
    
    # Check enemy killed by player and delete enemy
    def check_death(self):
        if self.alive == False:
            self.kill()
    
    # Update
    def update(self):
        self.move()
        self.check_off_screen()
        self.collision_bullet()
        self.check_death()
