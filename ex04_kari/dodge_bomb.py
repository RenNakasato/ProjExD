from turtle import speed
import pygame as pg
import sys
from random import randint

key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}

cr = {
    pg.K_0:0,
    pg.K_1:1,
    pg.K_2:2,
    pg.K_3:3,
    pg.K_4:4,
    pg.K_5:5,
    pg.K_6:6,
    pg.K_7:7,
    pg.K_8:8,
    pg.K_9:9,
}

def check_bound(obj_rct, scr_rct):
    """
    obj_rct:爆弾_rctまたはこうかとん_rct
    scr_rct:スクリーン_rct
    領域外になった時に反転します。
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():#1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("./ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()


    #鳥の中
    tori_sfc = pg.image.load("./fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #爆弾の中身
    bomb_sfc = pg.Surface((40,40))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (20, 20), 20)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0,scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    vx, vy, bom_speed = 1, 1, 1

    Clock = pg.time.Clock()
    while True:
        """
        キー入力関係
        矢印キーの移動
        こうかとん画像の変化
        速度変化
        """
        scrn_sfc.blit(bg_sfc,bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_stats = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_stats[key]:
                tori_rct.centerx += delta[0]
                tori_rct.centery += delta[1]
                # 練習7
                if check_bound(tori_rct, scrn_rct) != (+1, +1):
                    tori_rct.centerx -= delta[0]
                    tori_rct.centery -= delta[1]
            
        scrn_sfc.blit(tori_sfc,tori_rct)

        if key_stats[pg.K_ESCAPE]:break

        for key, num in cr.items():
            if key_stats[key]:
                tori_sfc = pg.image.load(f"./fig/{num}.png")
                tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)


        if key_stats[pg.K_h]:
            bom_speed = 3
        if key_stats[pg.K_u]:
            bom_speed = 1.1
        if key_stats[pg.K_n]:
            vx, vy = 1,1
    
        yoko, tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko * bom_speed
        vy *= tate * bom_speed
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        bom_speed =1

        #3
        if tori_rct.colliderect(bomb_rct):
            return


        pg.display.update()
        Clock.tick(1000)


def gameover():
    pg.display.set_caption("GAME OVER")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_sfc.fill("white")
    scrn_rct = scrn_sfc.get_rect()
    fonto = pg.font.Font(None, 180)
    txt = fonto.render(str("GAME OVER"), True,"black")
    scrn_sfc.blit(txt, (scrn_rct.width/4,scrn_rct.height/2))
    pg.display.update()
    Clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type ==pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
        Clock.tick(1000)


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    pg.init()
    gameover()
    pg.quit()
    sys.exit()
