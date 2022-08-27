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
from bullet import Bullet


class Player(pygame.sprite.Sprite):  # 自機を動かすためのクラス

    def __init__(self, groups, x, y, enemy_group):
        super().__init__(groups)

        # スクリーンをサーフェスで所得(すみません、日本語化がうまくできませんでした)
        self.screen = pygame.display.get_surface()

        # 弾のグループ
        self.bullet_group = pygame.sprite.Group()
        # 敵のグループ
        self.enemy_group = enemy_group

        # 自機の画像処理
        self.image_list = []  # 画像リストを空にする
        for i in range(1):
            image = pygame.image.load(image_player)  # 自機の画像指定
            self.image_list.append(image)

        # 自機の画像設定
        self.index = 0  # 自機の状態を0に設定(これを変更することで下の行のpre_imageを変更できる)
        self.pre_image = self.image_list[self.index]  # 画像リストにindexを代入
        self.image = pygame.transform.scale(
            self.pre_image, (50, 50))  # 画像の大きさを固定する
        self.rect = self.image.get_rect(center=(x, y))  # 画像の中央を所得する

        # 自機の動作
        self.direction = pygame.math.Vector2()  # 動く方向の所得
        self.speed = 5  # 自機のスピード

        # 自機の弾
        self.fire = False  # 発射はデフォルトでFalse
        self.timer = 0  # 弾タイマーを0に設定

        # 自機の体力
        self.health = 1  # 体力(現在は１)
        self.alive = True  # aliveをTrueにして生きているとする

    # ムーブメント
    def input(self):
        key = pygame.key.get_pressed()  # キーボードの入力を所得

        # 上下移動
        if key[pygame.K_w]:
            self.direction.y = -1  # ｗが押されたときにyを-1し続ける
        elif key[pygame.K_s]:
            self.direction.y = +1  # ｓが押されたときにyを+1し続ける
        else:
            self.direction.y = 0  # 何も入力がなければ何もしない

        # 左右移動
        if key[pygame.K_a]:
            self.direction.x = -2  # aが押されたときにⅹを-2し続ける
        elif key[pygame.K_d]:
            self.direction.x = +2  # dが押されたときにxを+2し続ける
        else:
            self.direction.x = 0  # 何も入力がなければ何もしない

        # 自機の弾を発射
        if key[pygame.K_SPACE] and self.fire == False:  # spaceが押されたときに
            bullet = Bullet(self.bullet_group, self.rect.centerx,
                            self.rect.top)  # 弾グループを呼び、自機の中央トップにセットする
            self.fire = True  # 発射を実行

    # 自機の弾の発射間隔
    def cooldown_bullet(self):
        if self.fire:  # 弾が発射されているときに
            self.timer += 1  # 弾タイマーを+1し続ける
        if self.timer > 10:  # 弾タイマーが10より大きくなった時に
            self.fire = False  # 発射をFalseにする
            self.timer = 0  # 弾タイマーをリセット

    # 移動管理
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.check_off_screen('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.check_off_screen('vertical')

    # 自機の移動制限
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

    # 自機の体力管理
    def collision_enemy(self):
        for enemy in self.enemy_group:  # エネミーがグループ内にあるとき
            if self.rect.colliderect(enemy.rect):  # エネミーとの当たり判定が重なったときに
                self.health -= 1  # 自機の体力を-1する

        if self.health <= 0:  # 自機の体力が0以下になった時に
            self.alive = False  # aliveをFalseとして死んでいるとする

    # 自機の削除
    def check_death(self):
        if self.alive == False:  # aliveがFalseのときに
            self.kill()  # killを実行

    # 自機の画像の更新
    def update_image(self):
        self.pre_image = self.image_list[self.index]  # index番の画像をロード
        self.image = pygame.transform.scale(
            self.pre_image, (50, 50))  # 画像の大きさをストレッチ

    # 更新
    def update(self):
        # 自機の処理の更新
        self.input()  # 入力
        self.move()  # 移動
        self.update_image()  # アニメーション
        self.cooldown_bullet()  # 発射速度
        self.collision_enemy()  # 敵との当たり判定
        self.check_death()  # 死亡の判断

        # グループと描画の更新
        self.bullet_group.draw(self.screen)
        self.bullet_group.update()
