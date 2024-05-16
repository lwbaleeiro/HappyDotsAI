import pygame
import random

class Resource:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 8
        self.color = (255, 0, 0)
        self.energy_value = 100
        self.bad_resource_chance = 30
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def resource_type(self):
        num = random.random()
        if num <= self.bad_resource_chance / 100:
            self.color = (128, 85, 0)
            self.energy_value = -15
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)