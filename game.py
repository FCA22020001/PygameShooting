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
from player import Player
from enemy import Enemy
from support import draw_text

# ゲームのコア ==================================================


class Game:  # ゲームのメインの処理クラス

    def __init__(self):
        # 画面の描画関連を所得
        self.screen = pygame.display.get_surface()

        # グループ作成 line = 38
        self.create_group()

        # プレイヤーを配置
        self.player = Player(self.player_group, 300, 500, self.enemy_group)

        # エネミーのタイマーを0にする(フレームレート基準)
        self.timer = 0

        # 背景画像の設定
        self.pre_bg_img = pygame.image.load(image_bg)  # 画像の読み込み
        self.bg_img = pygame.transform.scale(
            self.pre_bg_img, (screen_width, screen_height))  # 画像をウィンドウのサイズにストレッチさせる
        self.bg_y = 0  # デフォルトのイメージ原点
        self.scroll_speed = 0.5  # 背景のスクロールスピード

        # 音楽
        pygame.mixer.music.load('assets/sounds/bgsong.mp3')  # 音楽の読み込み
        pygame.mixer.music.play(-1)  # ループ再生する
        pygame.mixer.music.set_volume(0.3)  # 音量を30%で再生する

        # ゲームオーバー、死なない限りFalse
        self.game_over = False

    # グループ作成
    def create_group(self):
        # 自機は1人なのでGroupSingleで1体専用のグループを作成
        self.player_group = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()    # エネミーグループを通常のグループ(複数存在可)で作成

    # エネミーの生成
    def create_enemy(self):
        self.timer += 1  # エネミーのタイマーを+1していく
        if self.timer > 50:  # タイマーが50を超えたら
            enemy = Enemy(self.enemy_group, random.randint(
                50, 550), 0, self.player.bullet_group)  # エネミーをｘ50~550、ｙ0の間でランダム生成
            self.timer = 0  # 敵を生成したらタイマーを0にセット

    # 自機の死亡アクション
    def player_death(self):
        if len(self.player_group) == 0:  # 自機の数が０になったら
            self.game_over = True  # ゲームオーバー処理をTrueにする
            # リスタートを促すテキストを表示
            draw_text(self.screen, 'game over', screen_width //
                      2, screen_height // 2, 75, RED)
            draw_text(self.screen, 'press R KEY to reset',
                      screen_width // 2, screen_height // 2 + 100, 50, RED)

    # リスタートの処理
    def reset(self):
        if self.game_over == True:  # ゲームオーバー処理がTrueのとき
            key = pygame.key.get_pressed()  # キーボード入力を検出
            if self.game_over and key[pygame.K_r]:  # Rキーが押されたときに
                self.player = Player(self.player_group, 300,
                                     500, self.enemy_group)  # 自機を再配置
                self.enemy_group.empty()  # エネミーの数をemptyにする
                self.game_over = False  # ゲームオーバー処理をFalseに戻す

    # 背景のスクロール処理
    def scroll_bg(self):
        # 背景の原点を(原点+スクロールスピード)%スクリーンの縦で変更する
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height
        # 下の背景を0 ~ -599まで移動させる
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height))
        self.screen.blit(self.bg_img, (0, self.bg_y))  # 上の背景を+600 ~ 0まで移動させる

    # ゲームの実行
    def run(self):
        # 背景のスクロールの実行
        self.scroll_bg()

        # エネミーの生成の実行
        self.create_enemy()

        # 自機の死亡時アクションの実行
        self.player_death()
        self.reset()

        # グループの描画と更新
        self.player_group.draw(self.screen)
        self.player_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()

# ==========================================================
