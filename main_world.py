import pygame
import sys
from dot import Dot
from population import Population

pygame.init()

width = 800
height = 900
top_panel = 50

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Dots AI - Fun Project")

population = Population(window, 100)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    # Top panel
    pygame.draw.rect(window, GRAY, (0, 0, width, top_panel))
    # Game panel
    pygame.draw.rect(window, WHITE, (0, top_panel, width, height - top_panel))

    population.update()
    population.show()

    pygame.display.flip()