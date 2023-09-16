import pygame as pg
from player_file import Player
from bullet_file import Bullet
#pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
player = Player(screen=screen)
background = pg.image.load("diego-lopez-groundtiles.jpg")
bullets = []
i = 0

while running:
    #event handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type + pg.MOUSEBUTTONDOWN:
            i+=1
            print(i)
    
    keys = pg.key.get_pressed()
    if keys[pg.K_z]:
        player.pos.y -= player.speed
    if keys[pg.K_s]:
        player.pos.y += player.speed
    if keys[pg.K_q]:
        player.pos.x -= player.speed
    if keys[pg.K_d]:
        player.pos.x += player.speed
     
    #renderer
    #screen.fill("black")
    screen.blit(background, (0, 0))
    screen.blit(background, (512, 0))
    screen.blit(background, (1024, 0))
    screen.blit(background, (0, 512))
    screen.blit(background, (512, 512))
    screen.blit(background, (1024, 512))

    pg.draw.circle(screen, "red", player.pos, 50)
    pg.draw.circle(screen, "green", pg.mouse.get_pos(), 10)
    for bullet in bullets:
        bullet.update()
        pg.draw.rect(screen, "purple", bullet.rect)
        pg.draw.circle(screen, "blue", bullet.pos, 10)
    
    
    pg.display.flip() #register changes
    
    clock.tick(60) # set the fps of the game 