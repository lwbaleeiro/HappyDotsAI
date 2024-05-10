import pygame
import sys
from goal import Goal
from population import Population

pygame.init()

width = 800
height = 900
top_panel = 50

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Dots AI - Fun Project")
paused = False
clock = pygame.time.Clock()

population = Population(window, 2)
goal = Goal(window)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    window.fill(WHITE)

    pygame.draw.rect(window, GRAY, (0, 0, width, top_panel))
    pygame.draw.rect(window, WHITE, (0, top_panel, width, height - top_panel))

    if not paused:
        if population.all_dots_dead_or_reached_goal():
            population.calculate_fitness()
            #population.natural_selection()
            #population.mutation()
            paused = True
        else:
            population.update()
    
    goal.show()
    population.show()

    pygame.display.flip()
    clock.tick(100)