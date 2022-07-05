import pygame as pg
import sys
import random

def main():
    #練習1
    clock=pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc=pg.display.set_mode((1600,900)) #Surface
    screen_rct=screen_sfc.get_rect()  #rect
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rct=bgimg_sfc.get_rect() #rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)
    #練習3
    kkimg_sfc=pg.image.load("fig/6.png") #Surface
    kkimg_sfc=pg.transform.rotozoom(kkimg_sfc,0,2.0) #Surface
    kkimg_rct=kkimg_sfc.get_rect() #rect
    kkimg_rct.center=900,400
    #練習5
    bmimg_sfc=pg.Surface((20,20)) #Surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rct=bmimg_sfc.get_rect() #rect
    bmimg_rct.centerx=random.randint(0,screen_rct.width)
    bmimg_rct.centery=random.randint(0,screen_rct.height)
    vx, vy=+1, +1 #練習6

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        #練習２
        for event in pg.event.get():
            if event.type==pg.QUIT: return
        #練習4,7
        key_states=pg.key.get_pressed() #辞書
        if key_states[pg.K_UP] == True: kkimg_rct.centery -=1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery +=1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -=1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx +=1
        if check_bound(kkimg_rct,screen_rct) != (1,1): #領域外だったら
            if key_states[pg.K_UP] == True: kkimg_rct.centery +=1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -=1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx +=1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -=1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        bmimg_rct.move_ip(vx,vy) #練習6
        screen_sfc.blit(bmimg_sfc,bmimg_rct) #練習5
        #練習7
        yoko, tate=check_bound(bmimg_rct,screen_rct)
        vx*=yoko
        vy*=tate
        #練習8
        if kkimg_rct.colliderect(bmimg_rct): return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct): #1.こうかとんor爆弾のrect 2.スクリーンのrect
    yoko, tate =+1, +1 #領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1 #領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1 #領域外
    return yoko, tate

if __name__=="__main__":
    pg.init()
    main() #これから実装するゲームのメイン部分
    pg.quit()
    sys.exit()