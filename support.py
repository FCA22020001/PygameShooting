#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by FCA22020001
#=========================================================#

# システムインポート
import pygame

# テキストを画像に変換する


def draw_text(screen, txt, x, y, size, color):
    font = pygame.font.Font(None, size)  # フォントはpygameのデフォルト
    surface = font.render(txt, True, color)  # テキストを画像にする
    x = x - surface.get_width() / 2  # 横幅
    y = y - surface.get_height() / 2  # 縦幅
    screen.blit(surface, (x, y))  # 描画
