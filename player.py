import pygame
import random

from network import *

class Player:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.colour = (0, 0, 255)

        self.jumping = False
        self.velocity = 0

        self.gravity = 1

        self.score = 0

        self.t = 0

        self.brain = None

        self.alive = True

    def render(self, screen):
        if self.alive:
            b = 2
            pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.w, self.h))
            pygame.draw.rect(screen, self.colour, (self.x+b, self.y+b, self.w-2*b, self.h-2*b))

    def collision(self, obstacles):
        for ob in obstacles:
            if (self.y + self.h < ob.y) or (self.y > ob.y + ob.h):
                x = 1
            elif (self.x + self.w < ob.x) or (self.x > ob.x + ob.w):
                x = 1
            else:
                return True

        if self.x < 0 or self.x + self.w >400:
            return True
        return False
            
            
            

        
    def tick(self, obstacles):
        ob = None
        ob2 = None
        closest = 1000
        closest2 = 1000
        for obs in obstacles:
            if obs.x > self.x and (obs.x-self.x) < closest:
                closest = (obs.x-self.x)
                ob = obs
        for obs in obstacles:
            if obs.x > self.x and (obs.x-self.x) < closest2 and obs != ob:
                closest2 = (obs.x-self.x)
                ob2 = obs
        if len(obstacles) == 1:
            ob2 = ob
        if self.alive:

            self.t += 1
            if self.t == 1:
                self.score += 1
                self.t = 0

            if not self.jumping:
                dist = (ob.x - self.x)/800
                a = (500 - (ob.y + ob.h))/360
                b = (500 - ob.y)/360
                dist2 = (ob2.x - self.x)/800
                a2 = (500 - (ob2.y + ob2.h))/360
                b2 = (500 - ob2.y)/360
                #print(dist, a, b)
                #height = 1 if self.y > (ob.y + ob.h) else 0
                #obh = ob.h/160
                #print(dist, height)
                output = self.brain.feed_forward([dist, a, b])
                output1 = output[0]
                #output2 = output[1]
                #output3 = output[2]
                #output4 = output[3]
                #print(output)
                if  output1 > 0.5:
                    self.velocity = 20
                    self.jumping = True
                '''
                if  output2 > 0.5:
                    self.velocity = 20
                    self.jumping = True
                if  output3 > 0.5:
                    self.x += 1
                if  output4 > 0.5:
                    self.x -= 1
                '''
                

            self.y = min(465, self.y - self.velocity )

            if self.y < 465:
                self.velocity -= self.gravity

            if self.y == 465:
                self.velocity = max(0, self.velocity)
                self.jumping = False

            if self.collision(obstacles):
                self.alive = False

        

            
            
            
        
        
