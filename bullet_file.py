import pygame as pg
class Bullet:
    def __init__(self, pos, vector, shot_speed, shot_size):
        self.pos = pos
        self.speed = shot_speed
        self.vector = vector
        self.rect = pg.Rect((pos.x - shot_size/2, pos.y - shot_size/2), (shot_size, shot_size))
    
    def update(self):
        self.pos += self.vector * self.speed 
        self.rect.center = self.pos
    
    