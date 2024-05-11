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
        self.is_best = False

    def show(self):
        color = (0, 0, 0)
        if self.is_best:
            color = (0, 128, 0)

        pygame.draw.circle(self.window, color, (int(self.position[0]), int(self.position[1])), self.dot_width)

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

    def get_distance_dot_goal(self, dot_x, dot_y, goal_x, goal_y):

        return math.sqrt((dot_x - goal_x) **2 + (dot_y - goal_y) **2)

    def calculate_fitness(self):
        goal_x, goal_y = 300, 50
        goal_width, goal_height = 200, 15

        distance = self.get_distance_dot_goal(self.position[0], self.position[1], (goal_x + goal_width / 2), (goal_y + goal_height / 2))

        distance_fitness = 1 / (distance + 1) # Evitar divisão por zero
        step_fitness = 1 - (self.brain.step / 1000)

        fitness = distance_fitness * step_fitness
        return fitness
    
    def check_edges_collision(self, dot_x, dot_y):
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
        
    def reproduce(self):
        # O filho ira receber as mesmas coordenadas do cérebro do pai
        new_dot = Dot(self.window)
        new_dot.brain.clone(self.brain)

        return new_dot


        
       


