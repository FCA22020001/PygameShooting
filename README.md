<div align = "left">
#=========================================================#<br>
#　　PygameShooting.ver2<br>
#　　　using :<br>
#　　　　　python 3.10<br>
#　　　　　pygame 2.1.2<br>
#　　　Created by FCA22020001<br>
#=========================================================#<br>
<div>
<br>

# How to start game?
Download release ver0.2.0 and double-click main.exe.

# HELP ME!!
- in [player.py](/player.py) line 90 ~<br>
    頭の中では想像できるのですが日本語化が難しかったです。


# 改善点
- コード
    - コードを書いているときに一緒にコメントを追加する
    - もっとsupport.pyみたいなファイルを増やす。↓こんなやつ
    ```py
    movement.py
    import pygame
    def input(self):
        key = pygame.key.get_pressed()
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
    ```
    - settingsは種類ごとに分ける
    ```py
    game_main
        | - main.py
        | - image_path.py   # 画像のパス
        | - general.py      # キーコンフィグSの設定
                ・
                ・
                ・
    ```
    - Scriptsフォルダーを作成して、その中にコードを入れる
    - .batファイルを作成しておく

- ゲーム内
    - UIを正しい位置に配置する。例えばレイヤーの順番とか
    - アスペクト比16:9でゲームを作る
    - 敵の攻撃が欲しい
    - 敵の動作を増やす
    - 難易度設定
    - メニュー画面など
    - ライフやスコアの追加
    - 縦スクロールから横スクロールにする
    - キー入力を増やす。例えばwasdと↑←↓→とか
    - エフェクトやアニメーション、効果音の追加

思ついた改善点はこのくらいです。もっとこうしたほうが良いことがあれば[issue](https://github.com/FCA22020001/PygameShooting/issues)にお願いします。