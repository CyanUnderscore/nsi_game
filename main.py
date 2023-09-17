import pygame as pg
from math import *
from player_file import Player
from bullet_file import Bullet
from monster_file import Monster
from heath_bar import HealthBar


#pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
player = Player(screen=screen)
background = pg.image.load("diego-lopez-groundtiles.jpg")
bullets = []
monsters = []
i = 0

def GetVector(origin, target):
    target -= origin
    divider = (Positive(target.x)+Positive(target.y))
    print("divider = ", divider, target.x, target.y)
    if divider == 0:
        divider += 1
    x = target.x/divider
    y = target.y/divider
    return pg.Vector2(x=x, y=y)

def Positive(x):
    if x < 0:
        return x*-1
    return x

while running:
    #event handler
    if player.health <= 0:
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

    pg.draw.circle(screen, "white", player.pos, player.size)
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
        pg.draw.rect(screen, "purple", monster.rect)
        i+=1
    
    
    pg.display.flip() #register changes
    
    clock.tick(60) # set the fps of the game 