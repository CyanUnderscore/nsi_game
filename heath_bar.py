import pygame as pg
class HealthBar:
    def __init__(self):
        self.height = 25
        self.width = 100
        self.percent = 100
    
    def generate(self, owner):
        self.percent = owner.health/owner.max_health
        bg = pg.Rect((owner.pos.x - self.width/2, owner.pos.y - 10 -self.height*2), (self.width,self.height))
        fg = pg.Rect((owner.pos.x - self.width/2, owner.pos.y - 10- self.height*2), (self.width*self.percent,self.height))
        bg.fit(fg)
        return (bg, fg)

