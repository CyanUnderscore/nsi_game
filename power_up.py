import pygame as pg
class Power_up:
    def __init__(self, pos):
        self.pos = pos
        self.power = 2
        self.size = 15
        self.rect = pg.Rect((pos.x - self.size/2, pos.y - self.size/2), (self.size*2,self.size*2))
