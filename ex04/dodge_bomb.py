import pygame as pg
import sys

def main():#1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))

    bg_sfc = pg.image.load("./ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("./fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

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
        scrn_sfc.blit(tori_sfc,tori_rct)
        pg.display.update()
        if key_stats[pg.K_ESCAPE]:break

        Clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
