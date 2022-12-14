import pygame as pg
import sys
from random import randint

#キーの判定
key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}

#　キャラクターの画像
key_cr ={
    pg.K_0 : 0,
    pg.K_1 : 1,
    pg.K_2 : 2,
    pg.K_3 : 3,
    pg.K_4 : 4,
    pg.K_5 : 5,
    pg.K_6 : 6,
    pg.K_7 : 7,
    pg.K_8 : 8,
    pg.K_9 : 9,
}

#画面はじ判定
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
    pg.draw.circle(bomb_sfc, (0, 40, 0), (30, 30), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0,scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    #爆弾の速度
    vx, vy,bom_speed= 1, 1, 1

    
    Clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #矢印キーの操作
        key_stats = pg.key.get_pressed()#4
        for key, delta in key_delta.items():
            if key_stats[key]:
                tori_rct.centerx += delta[0]
                tori_rct.centery += delta[1]
                # 練習7
                if check_bound(tori_rct, scrn_rct) != (+1, +1):
                    tori_rct.centerx -= delta[0]
                    tori_rct.centery -= delta[1]

        for key, cr in key_cr.items():
            if key_stats[key]:
                tori_sfc = pg.image.load(f"./fig/{cr}.png")
                tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)



        scrn_sfc.blit(tori_sfc,tori_rct)

        #エスケープでゲーム終了
        if key_stats[pg.K_ESCAPE]:break

        if key_stats[pg.K_u]:
            bom_speed = 1.1
        if key_stats[pg.K_h]:
            bom_speed = 3
            pg.draw.circle(bomb_sfc, (255, 0, 0), (30, 30), 10)
        if key_stats[pg.K_n]:
            vx,vy =1, 1
            bom_speed = 1
            pg.draw.circle(bomb_sfc, (0, 40, 0), (30, 30), 10)
        if key_stats[pg.K_d]:
            bom_speed = 0.9

        #爆弾の挙動
        #6
        yoko, tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko * bom_speed
        vy *= tate * bom_speed
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        #当たり判定
        if tori_rct.colliderect(bomb_rct):
            return

        #爆弾の速度調整
        bom_speed = 1

        pg.display.update()
        Clock.tick(1000)


#ゲームオーバー画面
def gameover():
    pg.display.set_caption("ゲームが終わったよ")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    scrn_sfc.fill("white")
    fonto = pg.font.Font(None, 180)
    txt = fonto.render(str("GAME OVER"), True, "black")
    scrn_sfc.blit(txt,(scrn_rct.width/4,scrn_rct.height/2))
    pg.display.update()
    Clock_go = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:return

        key_stats = pg.key.get_pressed()#4
        if key_stats[pg.K_ESCAPE]:break
        Clock_go.tick(1000)



if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    pg.init()
    gameover()
    pg.quit()
    sys.exit()
