import pygame
import random
import numpy as np

class Dot:
    def __init__(self, window):
        self.dot_width = 4
        self.window = window
        self.position = [window.get_width() / 2, window.get_height() / 2]
        self.velocity = np.array([0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0])
        self.brain = None
        self.max_speed = 1
        self.dead = False
        self.reached_goal = False
        self.is_best = False
        self.fitness = 0

    def show(self):
        pygame.draw.circle(self.window, (0, 0, 0), (int(self.position[0]), int(self.position[1])), self.dot_width)

    def move(self):
        
        self.acceleration = np.array([random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)])

        self.velocity += self.acceleration
        # np.clip limita um valor entre um range de valores.
        self.velocity = np.clip(self.velocity, -self.max_speed, self.max_speed)
        
        self.position += self.velocity

    def update(self):
        position_x = self.position[0]
        position_y = self.position[1]
        if not self.dead and not self.reached_goal:
            self.move()
            # Verifica colisão com as bordas
            if (position_x < 0) or (position_y < 50) or (position_y > self.window.get_height()) or (position_x > self.window.get_width()):
                self.dead = True


