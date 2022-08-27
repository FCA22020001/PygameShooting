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
from bullet import Bullet

# Player Movements & more
class Player(pygame.sprite.Sprite): # Create player class

    def __init__(self, groups, x, y, enemy_group):
        super().__init__(groups)

        self.screen = pygame.display.get_surface()

        # Group
        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = enemy_group

        self.image_list = []
        for i in range(1):
        # Player image
            image = pygame.image.load(image_player)
            self.image_list.append(image)
        
        # Player image settings
        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))

        # Move
        self.direction = pygame.math.Vector2() # Get where player go
        self.speed = 5 # Player speed

        # Bullet
        self.fire = False
        self.timer = 0

        # Health
        self.health = 1
        self.alive = True
    
    # Movements
    def input(self):
        key = pygame.key.get_pressed() # Getting key status

        # Up and Down
        if key[pygame.K_w]:
            self.direction.y = -1 # If w=1, do y-1
        elif key[pygame.K_s]:
            self.direction.y = +1 # If s=1, do y+1
        else:
            self.direction.y = 0 # If not input, do not move
        
        # Left and Right
        if key[pygame.K_a]:
            self.direction.x = -2 # If a=1, do x-2
        elif key[pygame.K_d]:
            self.direction.x = +2 # If d=1, do x+2
        else:
            self.direction.x = 0 # If not input, do not move
        
        # Fire
        if key[pygame.K_SPACE] and self.fire == False: # If space=1 and fire=false, do fire
            bullet = Bullet(self.bullet_group, self.rect.centerx, self.rect.top)
            self.fire = True

    # Bullet cooldown manager
    def cooldown_bullet(self):
        if self.fire:
            self.timer += 1
        if self.timer > 10:
            self.fire = False
            self.timer = 0

    # Movements manager
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.check_off_screen('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.check_off_screen('vertical')

    # Player area limit
    def check_off_screen(self, direction):
        if direction == 'horizontal':
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen_width:
                self.rect.right = screen_width

        if direction == 'vertical':
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height

    # Player health manager
    def collision_enemy(self):
        for enemy in self.enemy_group:
            if self.rect.colliderect(enemy.rect):
                self.health -= 1

        if self.health <= 0:
            self.alive = False

    # Check player death and delete
    def check_death(self):
        if self.alive == False:
            self.kill()

    # Update image
    def update_image(self):
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))

    # Update
    def update(self):
        self.input()
        self.move()
        self.update_image()
        self.cooldown_bullet()
        self.collision_enemy()
        self.check_death()

        # Group graphic and update
        self.bullet_group.draw(self.screen)
        self.bullet_group.update()
