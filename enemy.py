#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by FCA22020001
#=========================================================#

# システムインポート
import pygame
import random

# ファイルインポート
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, bullet_group):
        super().__init__(groups)

        # 弾のグループ
        self.bullet_group = bullet_group

        self.image_list = []
        for i in range(1):
            # エネミーの画像
            image = pygame.image.load(image_enm)
            self.image_list.append(image)

        # エネミーの画像設定
        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(
            self.pre_image, (50, 50))  # エネミーの画像をストレッチ
        self.rect = self.image.get_rect(center=(x, y))  # エネミーの中央の座標を所得

        # エネミーの動き
        move_list = [1, -1]  # 移動の状態
        self.direction = pygame.math.Vector2(
            (random.choice(move_list), 1))  # ランダムでmove_listから選ぶ
        self.speed = 1  # エネミーの速さ
        self.timer = 0  # エネミータイマー

        # エネミーの体力
        self.health = 3  # 体力は3
        self.alive = True  # aliveをTrueとしてエネミーが生きているとする

    # エネミーの動きを処理
    def move(self):
        self.timer += 1  # タイマーを+1し続ける
        if self.timer > 80:  # タイマーが80より大きくなったら
            self.direction.x *= -1  # direction.xを*-1する
            self.timer = 0  # タイマーをリセットする

        self.rect.x += self.direction.x * self.speed  # 横移動
        self.rect.y += self.direction.y * self.speed  # 縦移動

    # エネミーの画面外処理
    def check_off_screen(self):
        if self.rect.top > screen_height:  # エネミーの中央上の座標がscreen_heightより大きくなった時
            self.kill()  # エネミーを削除

    # エネミーに弾が当たった時の処理
    def collision_bullet(self):
        for bullet in self.bullet_group:  # 弾が自機のものであるとき
            if self.rect.colliderect(bullet.rect):  # 弾がエネミーの当たり判定と重なったときに
                bullet.kill()  # 弾の削除
                self.health -= 1  # エネミーの体力を-1する

        if self.health <= 0:  # エネミーの体力が0以下になったときに
            self.alive = False  # aliveをFalseとして死亡と判断する

    # エネミーの死亡処理
    def check_death(self):
        if self.alive == False:  # alliveがFalseのときに
            self.kill()  # エネミーを削除

    # 更新
    def update(self):
        self.move()
        self.check_off_screen()
        self.collision_bullet()
        self.check_death()