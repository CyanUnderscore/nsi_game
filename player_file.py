import pygame as pg
from heath_bar import HealthBar


class Player:
    def __init__(self, screen):
        self.max_health = 100
        self.health = self.max_health
        self.speed = 7
        self.shot_speed = 30
        self.shot_size = 10
        self.range = 300
        self.damage = 30
        self.size = 25
        self.alive = True
        self.pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.rect = pg.Rect((self.pos.x - self.size/2, self.pos.y - self.size/2), (self.size*2,self.size*2))
        self.health_bar = HealthBar()
        self.shot_num = 1
        

    def take_damage(self, damage):
        self.health -= damage
    
    def heal(self, heal):
        self.health += heal

    def upgrade_shot(self, power):
        self.shot_num += power
        self.range += 10 * power

    def upgrade_pow(self, power):
        self.damage += power*5
        self.shot_size += power*3
    
    def update(self):
        self.rect.center = self.pos
