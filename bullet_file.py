import pygame as pg
class Bullet:
    def __init__(self, pos, vector):
        self.pos = pos
        self.speed = 0.4
        self.vector = vector
        self.rect = pg.Rect((pos.x - 5, pos.y - 5), (10,10))
    def update(self):
        self.pos += self.vector * self.speed