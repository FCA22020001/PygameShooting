#=========================================================#
#   PygameShooting.ver2
#       using :
#           python 3.10
#           pygame 2.1.2
#       Created by FCA22020001
#=========================================================#

# ウィンドウの大きさ
screen_width = 600
screen_height = 600

# 画像のパス
image_bg = ('assets/images/game_background2.png')  # Background
image_player = ('assets/images/me.png')  # Player
image_enm = ('assets/images/enemy_ver2.png')  # Enemy
image_pbl = ('assets/images/bullet.png')  # Player bullet

# FPS値
FPS = 60

# 色(RGBで指定)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Loader Text
# lt1 = ('\n\n\n' +
#        '#=========================================================#\n' +
#        '#\n'
#        '#   Key Config\n' +
#        '#       W = Go up\n' +
#        '#       A = Go left\n' +
#        '#       S = Go down\n' +
#        '#       D = Go right\n' +
#        '#       Space = Fire bullets\n' +
#        '#       R = Reset(Restart) game\n' +
#        '#       ESC = End game(task)\n' +
#        '#')
# lt2 = ('#=========================================================#\n' +
#        '#\n'
#        '#   PygameShooting.ver2\n' +
#        '#       using :\n' +
#        '#           python 3.10\n' +
#        '#           pygame 2.1.2\n' +
#        '#       Created by KaRU3\n'+
#        '#')
# lt3 = ('#=========================================================#\n' +
#        '#\n'
#        '#    Using Sounds\n' +
#        '#       SongTitle : [FREE] Dark Techno / EBM / Industrial Type Beat \'HEINOUS\' | Background Music\n' +
#        '#          Artist : Aim To Head\n' +
#        '#            Link : https://www.youtube.com/watch?v=D7xS-50zHiE\n' +
#        '#\n'
#        '#=========================================================#\n')