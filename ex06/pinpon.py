import pygame as pg
import sys
from random import choice

# スクリーンに関するクラス
class Screen:
    def __init__(self, title, wh,bg):
        """
        titleは表示される画面の名前
        whは縦横のサイズ
        bgは背景画像のパス
        """
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode((wh))
        self.rct = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(bg)
        self.bg_rct = self.bg_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rct)


class User:
    # 上下キーの反応
    key_delta = {
    pg.K_UP:    [0, -5],
    pg.K_DOWN:  [0, +5],
    }

    def __init__(self, x,y,sc,scx,scy, color, name):
        """
        x,yはバーのサイズ
        scはこの者のゲームのスコア
        scx,scx,はこの者のスコアが表示される場所
        colorは何色でスコアとバーを表示させるか
        nameはこのバーの持ち主
        """
        self.sfc = pg.Surface((x,y))
        self.sfc.fill(color)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = x
        self.rct.centery = y
        self.sc = sc
        self.scx = scx
        self.scy = scy
        self.color = color
        self.name = name

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def updata(self,scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in User.key_delta.items():
            if key_states[key]:
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Ball:
    def __init__(self,color, r, spd,scr:Screen):
        """
        color,はボールの色
        rはボールの半径
        spdはボールの速度
        scrはボールの初期位置
        """
        self.sfc = pg.Surface((r*2,r*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (r,r), r)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = scr.rct.centerx
        self.rct.centery = scr.rct.centery
        self.vx, self.vy = spd
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    #基本的な動き
    def updata(self,scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

    # バーにあった時の動き
    def kabe_upd(self, other,scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound_ch(self.rct, other)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

#　対戦相手に関する動き
class Com:
    def __init__(self,x,y,sx,sy,spd,sc, scx, scy,color, name):
        """
        x,yはバーのサイズ
        sx,syはバーの初期位置
        spdはどのぐらいの速度で動くか
        scはこの者のゲームのスコア
        scx,scx,はこの者のスコアが表示される場所
        colorは何色でスコアとバーを表示させるか
        nameはこのバーの持ち主
        """
        self.sfc = pg.Surface((x,y))
        self.sfc.fill(color)
        self.rct = self.sfc.get_rect()
        self.rct.center = sx, sy
        self.vx = 0
        self.vy = spd
        self.sc = sc
        self.scx = scx
        self.scy = scy
        self.color = color
        self.name = name

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def updata(self,scr:Screen):
        self.rct.move_ip(self.vx, self.vy) # 練習6
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # 練習5


#壁にあった時の判定
def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def check_bound_ch(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.right <= scr_rct.left or scr_rct.left <= obj_rct.right:
        yoko = -2
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -2
    return yoko, tate

def score(sc,scr:Screen):
    font = pg.font.Font(None, 100)
    txt = font.render(str(sc.sc), True,sc.color)
    scr.sfc.blit(txt, (sc.scx, sc.scy))

def mode(speed,scr:Screen):
    font = pg.font.Font(None, 100)
    if speed == 1:
        spd = "Nomal"
    elif speed == 3:
        spd = "Second"
    elif speed ==6:
        spd = "Hyper"
    txt = font.render(str(spd), True,(0,0,0))
    scr.sfc.blit(txt, (scr.rct.centerx-100, 100))

def name(name,num,scr:Screen):
    font = pg.font.Font(None, 30)
    txt = font.render(str(name.name), True,(0,0,0))
    scr.sfc.blit(txt, (name.rct.centerx-num, 10))
  
  
def main():
    scre = Screen("ピンポン",(1600,900),"./fig/pg_bg.jpg")

    user = User(10, 100, 0,scre.rct.centerx-100,200,(0,255,0),"you")

    ball = Ball((255,0,0),10,(1,1),scre)
    com = Com(10, 500, 1570, 500,3,0,scre.rct.centerx+100,200,(0,0,255),"computer")
    speed = 1

    while True:
        scre.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type ==pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                speed = 3
            if event.type == pg.KEYDOWN and event.key == pg.K_n:
                speed = 1
            if event.type == pg.KEYDOWN and event.key == pg.K_h:
                speed = 6
            
        hantei =[user.rct,com.rct]
        # 練習8
        for obj in hantei:
            if ball.rct.colliderect(obj):
                ball.kabe_upd(obj,scre)

        user.updata(scre)
        ball.updata(scre)
        com.updata(scre)
        score(user, scre)
        score(com, scre)
        mode(speed, scre)
        name(user, 0,scre)
        name(com, 70,scre)

        if ball.vx < -1 :
            ball.vx = -1 * speed
        if ball.vx > 1:
            ball.vx = 1 * speed

        houko = [-1*speed,1*speed]
        if ball.rct.x <= 0:
            com.sc +=1
            ball.rct.centerx = scre.rct.centerx
            ball.rct.centery = scre.rct.centery 
            ball.vx, ball.vy = choice(houko), choice(houko)
        if ball.rct.x >= 1600:
            user.sc +=1
            ball.rct.centerx = scre.rct.centerx
            ball.rct.centery = scre.rct.centery
            ball.vx, ball.vy = choice(houko), choice(houko)
        if abs(user.sc - com.sc) == 10:
            return
    
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()