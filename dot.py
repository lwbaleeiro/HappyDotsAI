import numpy as np
import math
from brain import Brain
import pygame

class Dot:
    def __init__(self, window, directions=None):
        self.window = window
        self.position = [window.get_width() / 2, window.get_height() - 700]
        self.velocity = np.zeros(2)
        self.acceleration = np.zeros(2)
        self.brain = Brain(directions)
        self.dead = False
        self.reached_goal = False
        self.fitness = 0
        self.max_speed = 3
        self.dot_radius = 4
        self.is_best = False

    def check_collision_with_edges(self, dot_x, dot_y):
        if (dot_x < 0) or (dot_y < 50) or (dot_y > self.window.get_height()) or (dot_x > self.window.get_width()):
            return True
        else:
            return False

    def check_goal_collision(self, dot_x, dot_y):
        goal_x = 300
        goal_y = 50
        goal_width = 200
        goal_height = 15

        if (dot_x > goal_x and dot_x < (goal_x + goal_width)) and (dot_y > goal_y and dot_y < (goal_y + goal_height)):
            return True
        else:
            return False 
        
    def get_distance_dot_goal(self, dot_x, dot_y, goal_x, goal_y):
        return math.sqrt((dot_x - goal_x) ** 2 + (dot_y - goal_y) ** 2)

    def move(self):
        next_acceleration = self.brain.get_next_acceleration()

        if next_acceleration is not None:
            self.acceleration = next_acceleration
        else:
            self.dead = True

        self.velocity += self.acceleration
        self.velocity = np.clip(self.velocity, -self.max_speed, self.max_speed)
        
        self.position += self.velocity

    def show(self):
        color = (254, 32, 32) if self.is_best else (0, 0, 0)
        radius = 12 if self.is_best else self.dot_radius
        pygame.draw.circle(self.window, color, (int(self.position[0]), int(self.position[1])), radius)

    def update(self):
        position_x = self.position[0]
        position_y = self.position[1]

        if self.check_collision_with_edges(position_x, position_y):
            self.dead = True
        if not self.dead and self.check_goal_collision(position_x, position_y):
            self.reached_goal = True

        if (not self.dead) and (not self.reached_goal):        
            self.move()

    def calculate_fitness(self):
        goal_x, goal_y = 300, 50
        goal_width, goal_height = 200, 15

        if self.reached_goal:
            self.fitness = 1.0 / 16.0 + 10000.0 / (self.brain.step * self.brain.step)
        else:
            distance = self.get_distance_dot_goal(self.position[0], self.position[1], 
                                            (goal_x + goal_width / 2), (goal_y + goal_height / 2))
            if distance == 0:
                self.fitness = 1.0
            else:
                self.fitness = 1.0 / (distance * distance)

    def reproduce(self, min_steps):
        child = Dot(self.window, self.brain.directions)
        child.brain.step = 0
        # Verifica se o número mínimo de passos foi atingido pelo melhor ponto da geração anterior
        if self.brain.step <= min_steps:
            child.brain.directions = self.brain.directions.copy()  # Mantém as direções do cérebro do ponto atual
        child.brain.mutate()
        child.is_best = False
        return child
