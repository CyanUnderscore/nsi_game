import pygame as pg
class HealthBar:
    def __init__(self):
        self.height = 50
        self.width = 200
        self.percent = 100
    
    def generate(self, owner):
        self.percent = owner.health/owner.max_health
        bg = pg.Rect((owner.pos.x - self.width/2, self.size/2), (self.width*2,self.height*2))
        fg = pg.Rect((owner.pos.x - self.width/2, self.size/2), (self.width*2*self.percent,self.height*2*self.percent))
        bg.fit(fg)
        return (bg, fg)
