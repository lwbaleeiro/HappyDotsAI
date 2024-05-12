import pygame
import sys
from goal import Goal
from population import Population

pygame.init()

def show_information(window, population):
    font = pygame.font.Font(None, 26) 

    text_surface = font.render(f"Generation: {population.generation}", True, BLACK)
    window.blit(text_surface, (10, 15))

    text_surface = font.render(f"Best fitness: {round(population.best_fitness, 5)}", True, BLACK)
    window.blit(text_surface, (160, 15))

    text_surface = font.render(f"Alives: {population.qtd_alives}", True, BLACK)
    window.blit(text_surface, (450, 15))

    text_surface = font.render(f"Reached goal: {population.qtd_reached_goal}", True, BLACK)
    window.blit(text_surface, (600, 15))

width = 800
height = 900
top_panel = 50

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

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
    show_information(window, population)

    if not paused:
        if population.all_dots_finished():
            population.natural_selection()
        else:
            population.update()
    
    goal.show()
    population.show()

    pygame.display.flip()
    clock.tick(100)