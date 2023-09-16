import pygame as pg

class Player:
    def __init__(self, screen):
        self.health = 100
        self.speed = 7
        self.range = 100
        self.alive = True
        self.pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)



    def take_damage(self, damage):
        self.health -= damage
    def heal(self, heal):
        self.health += heal
