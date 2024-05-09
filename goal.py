import pygame

class Goal:
    def __init__(self, window):
        self.window = window
        self.position = [400, 60]

    def show(self):
        pygame.draw.circle(self.window, (255, 200, 130), (self.position[0], self.position[1]), 8)