import pygame as pg
from heath_bar import HealthBar


class Monster:
    def __init__(self, pos):
        self.max_health = 100
        self.health = self.max_health
        self.damage = 30
        self.pos = pos
        self.size = 20
        self.speed = 5
        self.rect = pg.Rect((pos.x - self.size/2, pos.y - self.size/2), (self.size*2,self.size*2))
        self.health_bar = HealthBar

    def update(self, vector):
        self.pos += vector * self.speed 
        self.rect.center = self.pos
    
    def take_damage(self, bullet, damage):
        self.health -= damage
        self.pos += bullet.vector * 150
