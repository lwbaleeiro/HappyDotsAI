import pygame
import numpy as np
import math
from brain import Brain

class Dot:
    def __init__(self, window):
        self.dot_width = 4
        self.window = window
        self.position = [window.get_width() / 2, window.get_height() - 100]
        self.velocity = np.array([0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0])
        self.brain = Brain(1000)
        self.max_speed = 3
        self.dead = False
        self.reached_goal = False
        self.fitness = 0

    def show(self):
        pygame.draw.circle(self.window, (0, 0, 0), (int(self.position[0]), int(self.position[1])), self.dot_width)

    def move(self):
        next_acceleration = self.brain.get_next_acceleration()

        if np.any(next_acceleration) != None:
            self.acceleration = next_acceleration
        else:
            self.dead = True

        self.velocity += self.acceleration
        self.velocity = np.clip(self.velocity, -self.max_speed, self.max_speed)
        
        self.position += self.velocity

    def update(self):
        position_x = self.position[0]
        position_y = self.position[1]
        if self.check_edges_collision(position_x, position_y):
            self.dead = True
        if not self.dead and self.check_goal_collision(position_x, position_y):
            self.reached_goal = True

        if not self.dead and not self.reached_goal:        
            self.move()

    def calculate_fitness(self):
        dot_x, dot_y = self.position[0], self.position[1]
        goal_x = 400
        goal_y = 60
        radius_goal = 8
        radius_dot = self.dot_width

        # Calcular a distancia entre os Dots e Goal, quanto menor, maior a pontuação
        distance = math.sqrt((dot_x - goal_x) ** 2 + (dot_y - goal_y) ** 2)
        self.fitness = distance - radius_dot - radius_goal
        print(f"distance: {distance} / fitness: {self.fitness}")

    def check_edges_collision(self, dot_x, dot_y):
        if (dot_x < 0) or (dot_y < 50) or (dot_y > self.window.get_height()) or (dot_x > self.window.get_width()):
            return True
        else:
            return False

    def check_goal_collision(self, dot_x, dot_y):
        goal_x = 400
        goal_y = 60
        radius_goal = 8
        radius_dot = self.dot_width

        distance = math.sqrt((dot_x - goal_x) ** 2 + (dot_y - goal_y) ** 2)
        if distance <= radius_goal + radius_dot:
            return True
        else:
            return False
        
    def clonar(self, brain):
        dot = Dot(self.window)
        dot.brain = brain


