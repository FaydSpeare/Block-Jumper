import pygame
import random

class Obstacle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.x = 800
        h = random.randint(0,160)
        if random.random() < 0.5:
            self.y = 400 - h
        else:
            self.y = 500 - h
        self.h = h
            

        self.colour = (255, 0, 0)

    def render(self, screen):
        b = 2
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, self.colour, (self.x+b, self.y+b, self.w-2*b, self.h-2*b))

    def tick(self, speed):
        self.x -= speed
        if self.x < -self.w:
            self.x = 800
            h = random.randint(0,160)
            if random.random() < 0.5:
                self.y = 400 - h
            else:
                self.y = 500 - h
            self.h = h

    
