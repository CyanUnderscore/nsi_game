import pygame as pg
from random import randint
from math import *
from player_file import Player
from bullet_file import Bullet
from monster_file import Monster
from heath_bar import HealthBar
from medpack_file import MedPack


#pygame setup
pg.init()
screen = pg.display.set_mode((1920, 1080))
clock = pg.time.Clock()
running = True
player = Player(screen=screen)
background = pg.image.load("diego-lopez-groundtiles.jpg")
spawn = [
    pg.Vector2(0,0),
    pg.Vector2(screen.get_width(),0),
    pg.Vector2(0,screen.get_height()),
    pg.Vector2(screen.get_width(),screen.get_height())
]
playing = 1
bullets = []
monsters = []
medpacks = []
i = 0
acceleration = 0

playButton_Rect = pg.Rect((screen.get_width()/2, screen.get_height()/2), (screen.get_height()/6, screen.get_width()/6))

def GetVector(origin, target):
    target -= origin
    divider = (Positive(target.x)+Positive(target.y))
    if divider == 0:
        divider += 1
    x = target.x/divider
    y = target.y/divider
    return pg.Vector2(x=x, y=y)

def Positive(x):
    if x < 0:
        return x*-1
    return x
n=0
while running:

    if playing == 0:
        pg.draw.rect(screen, "blue", playButton_Rect)
        if player.health <= 0:
            print("yo ded")
            running = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and playButton_Rect.collidepoint(pg.mouse.get_pos()):
                playing = 1
        
    else:
        #event handler
        if player.health <= 0:
            print("yo ded")
            running = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                bullets.append(Bullet(player.pos.copy(), GetVector(player.pos, pg.mouse.get_pos()), player.shot_speed, player.shot_size))


        keys = pg.key.get_pressed()
        if keys[pg.K_z] and player.pos[1] > screen.get_height()/15:
            player.pos.y -= player.speed
        if keys[pg.K_s] and player.pos[1] < screen.get_height()/15*14:
            player.pos.y += player.speed
        if keys[pg.K_q]and player.pos[0] > screen.get_width()/20:
            player.pos.x -= player.speed
        if keys[pg.K_d] and player.pos[0] < screen.get_width()/15*14:
            player.pos.x += player.speed
        
        if keys[pg.K_e]:
            monsters.append(Monster(pg.Vector2(x=700, y=700)))
        
        #renderer
        #screen.fill("black")
        screen.blit(background, (0, 0))
        screen.blit(background, (512, 0))
        screen.blit(background, (1024, 0))
        screen.blit(background, (0, 512))
        screen.blit(background, (512, 512))
        screen.blit(background, (1024, 512))
        screen.blit(background, (0, 1024))
        screen.blit(background, (512, 1024))
        screen.blit(background, (1024, 1024))

        screen.blit(background, (1024, 512))
        screen.blit(background, (1536, 512))
        screen.blit(background, (1536, 0))


        pg.draw.circle(screen, "white", player.pos, player.size)
        (bg, fg) = player.health_bar.generate(player) 
        pg.draw.rect(screen, "red", bg)
        pg.draw.rect(screen, "green", fg)
        pg.draw.circle(screen, "green", pg.mouse.get_pos(), 10)
        
        i = 0
        for bullet in bullets:
            bullet.update()
            if(pg.Vector2.distance_to(player.pos, bullet.pos) > player.range):
                bullets.pop(i)
            
            colision = pg.Rect.collidelist(bullet.rect, [monster.rect for monster in monsters])
            if colision != -1: # because return -1 if no collision
                monsters[colision].take_damage(bullet, player.damage)
                if len(bullets) >= 1: # looks weird but can happen when a lot of things are going on
                    bullets.pop(i)
                continue


            pg.draw.circle(screen, "blue", bullet.pos, player.shot_size)
            pg.draw.rect(screen, "purple", bullet.rect)
            i+=1
        
        i=0 
        for monster in monsters:
            monster.update(GetVector(monster.pos, player.pos.copy()))
            if monster.health <= 0:
                monsters.pop(i)
            if pg.Rect.colliderect(monster.rect, player.rect):
                player.take_damage(monster.damage)

            (bg, fg) = monster.health_bar.generate(monster) 
            pg.draw.rect(screen, "red", bg)
            pg.draw.rect(screen, "green", fg)
            pg.draw.circle(screen, "red", monster.pos, monster.size)
            #pg.draw.rect(screen, "purple", monster.rect)
            i+=1
        
        i = 0
        for medpack in medpacks:
            if pg.Rect.colliderect(medpack.rect, player.rect):
                player.heal(medpack.power)
                medpacks.pop(i)
            pg.draw.circle(screen, "green", medpack.pos, medpack.size)
            #pg.draw.rect(screen, "purple", monster.rect)
            i+=1
        
        player.update()
        print(player.pos)
        pg.display.flip() #register changes

        if n%(60*2) == 0:
            monsters.append(Monster(spawn[randint(0,3)].copy()))
            #monsters.append(Monster(pg.Vector2(1200, 800)))

        if n%(60*8) == 0:
            medpacks.append(MedPack(pg.Vector2(x=randint(0, 1500), y=randint(0,800))))

        if n%(60*5) == 0:
            acceleration += 1
        n += 1
        clock.tick(60+ 5 * acceleration) # set the fps of the game 