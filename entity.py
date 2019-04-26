import random

from player import *
from network import *

class Entity:

    def __init__(self, inputs, outputs, net=None):
        self.inputs = inputs
        self.outputs = outputs

        if net == None:
            self.brain = Network(inputs, outputs)
        else:
            self.brain = net

        self.fitness = 0
        self.score = 0
        self.best_score = 0
        self.alive = True

        self.player = Player(100, 485, 35, 35)
        self.player.brain = self.brain
        

    def think(self, vision):
        return self.brain.feed_forward(vision)

    def mutate(self):
        self.brain.mutate()

    def calculate_fitness(self):
        self.fitness = (self.player.score/5)**2

    def replicate(self):
        clone = Entity(self.inputs, self.outputs)
        clone.brain = self.brain.replicate()
        clone.best_score = self.best_score
        return clone

    def assess(self):
        return self.fitness
        
        
    
