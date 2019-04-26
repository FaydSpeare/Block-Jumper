import pygame


from population import *
from player import *
from obstacle import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

pygame.font.init() 
myfont = pygame.font.SysFont('Times New Roman', 20)

pop = Population(3, 1, 150)

players = []
for e in pop.population:
    players.append(e.player)

obstacles = []
ob = Obstacle(800, 400, 40, 100)
obstacles.append(ob)

crashed = False
paused = False

speed = 5

best_score = 0

passed = True

full = False

tick_speed = 150

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)

    if not paused:

        if not full:
            if obstacles[0].x % 200 == 0 and obstacles[0].x < 800:
                obstacles.append(Obstacle(800, 400, 40, 100))
            if len(obstacles) == 4:
                full = True

        if best_score > 5000 and passed:
            print(players[0].brain)
            passed = False
            tick_speed = 4000
            #paused = True

        pygame.draw.rect(screen, (135, 206, 250), (0, 0, 800, 600))
        pygame.draw.rect(screen, (0, 0, 0), (0, 502, 800, 200))

        
        curr = players[0].score
        if curr > best_score:
            best_score = curr
        score = myfont.render(str("Best Score: {:.2f}     Score: {:.2f}     Players: {}".format(best_score, curr, len(players))), False, (0, 0, 0))
        screen.blit(score ,(50, 50))

        for player in players:
            player.render(screen)
        for ob in obstacles:
            ob.render(screen)
        #speed = min(14, speed + 0.01)
        for ob in obstacles:
            ob.tick(speed)
        for player in players:
            player.tick(obstacles)
            if not player.alive:
                players.remove(player)

        if len(players) == 0 or players[0].score > 200000:
            pop.natural_selection()
            pygame.time.wait(500)
            
            speed = 5
            obstacles = []
            ob = Obstacle(795, 400, 40, 100)
            obstacles.append(ob)
            full = False
            
            for e in pop.population:
                players.append(e.player)

    pygame.display.update()
    clock.tick(tick_speed)

pygame.quit()
quit()
