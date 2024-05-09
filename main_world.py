import pygame
import sys

pygame.init()

width = 600
hight = 800
top_panel = 50

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

window = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Happy Dots AI - Fun Project")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    pygame.draw.rect(window, GRAY, (0, 0, width, top_panel))
    pygame.draw.rect(window, WHITE, (0, top_panel, width, hight - top_panel))

    pygame.display.flip()