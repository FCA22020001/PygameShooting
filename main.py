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
from game import Game

# ゲームの初期化
pygame.init()

# ゲームのウィンドウ表示と設定
screen = pygame.display.set_mode((screen_width, screen_height))

# ゲームウィンドウの左上の名前
pygame.display.set_caption("Shooting Game ver2")

# FPSの設定
# 時間ベースのFPS管理
clock = pygame.time.Clock()

# ゲームの読み込み
game = Game()

# メインループ ==================================================

# ゲームが起動されている状態
run = True

# デバッグウィンドウの方にキーコンフィグ等を表示する
# print(lt1)
# print(lt2)
# print(lt3)

while run:  # ゲームが起動され続けている間の処理(run = trueの間)

    # 背景画像のさらに後ろの色を黒で塗りつぶす
    screen.fill(BLACK)

    # ゲームを実行
    game.run()

    # イベントを所得
    for event in pygame.event.get():
        # バツボタンを押したとき
        if event.type == pygame.QUIT:
            run = False  # 実行をFalseに設定する
        # エスケープキーを押したとき
        if event.type == pygame.KEYDOWN:  # キーダウンのイベントを所得
            if event.key == pygame.K_ESCAPE:
                run = False  # 実行をFalseにする

    # ディスプレイの更新
    pygame.display.update()
    # FPSの設定
    clock.tick(FPS)

# ===========================================================

pygame.quit()  # ループを抜け出したときにゲームを終了する
