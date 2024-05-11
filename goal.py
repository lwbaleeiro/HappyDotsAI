import pygame

class Goal:
    def __init__(self, window):
        self.window = window
        self.position = [300, 50]
        self.width = 200
        self.heigth = 15

    def show(self):
        pygame.draw.rect(self.window, (255, 200, 130), (self.position[0], self.position[1], self.width, self.heigth))