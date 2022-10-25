import pygame as pg
import sys
from random import randint

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
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 20)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0,scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    vx, vy = 1, 1

    Clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_stats = pg.key.get_pressed()#4
        if key_stats[pg.K_UP]: tori_rct.centery -=1 
        if key_stats[pg.K_DOWN]:tori_rct.centery +=1 
        if key_stats[pg.K_LEFT]:tori_rct.centerx -=1
        if key_stats[pg.K_RIGHT]:tori_rct.centerx +=1 
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko ==-1:
            if key_stats[pg.K_LEFT]:
                tori_rct.centerx +=1
            if key_stats[pg.K_RIGHT]:
                tori_rct.centerx -=1
        if tate == -1:
            if key_stats[pg.K_UP]:
                tori_rct.centery +=1
            if key_stats[pg.K_DOWN]:
                tori_rct.centery -=1
            
        scrn_sfc.blit(tori_sfc,tori_rct)

        if key_stats[pg.K_ESCAPE]:break

        #6
        yoko, tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        #3
        if tori_rct.collidedict(bomb_rct):
            return


        pg.display.update()
        Clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
