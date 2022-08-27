#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by FCA22020001
#=========================================================#

# システムインポート
import pygame

# ファイルインポート
from settings import *


class Bullet(pygame.sprite.Sprite):

    def __init__(self, groups, x, y):
        super().__init__(groups)

        self.image_list = []
        for i in range(1):
            # 弾の画像
            image = pygame.image.load(image_pbl)
            self.image_list.append(image)

        # 弾の画像設定
        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(
            self.pre_image, (24, 48))  # 弾の大きさをストレッチ
        self.rect = self.image.get_rect(midbottom=(x, y))  # 弾の中央下の座標を所得

        # 弾の速さ
        self.speed = 8

    def check_off_screen(self):
        if self.rect.bottom < 0:  # 弾の下が画面外に行ったら
            self.kill()  # 球を削除

    def move(self):
        self.rect.y -= self.speed  # 発射点からspeed分yを-する

    def update(self):
        self.move()
        self.check_off_screen()