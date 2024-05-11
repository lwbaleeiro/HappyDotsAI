import pygame
import numpy as np
import math
from brain import Brain

class Dot:
    def __init__(self, window):
        self.dot_radius = 4
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

    def __check_edges_collision(self, dot_x, dot_y):
        if (dot_x < 0) or (dot_y < 50) or (dot_y > self.window.get_height()) or (dot_x > self.window.get_width()):
            return True
        else:
            return False

    def __check_goal_collision(self, dot_x, dot_y):
        goal_x = 300
        goal_y = 50
        goal_width = 200
        goal_height = 15

        if (dot_x > goal_x and dot_x < (goal_x + goal_width)) and (dot_y > goal_y and dot_y < (goal_y + goal_height)):
            return True
        else:
            return False 
        
    def __get_distance_dot_goal(self, dot_x, dot_y, goal_x, goal_y):
        return math.sqrt((dot_x - goal_x) **2 + (dot_y - goal_y) **2)

    def __move(self):
        next_acceleration = self.brain.get_next_acceleration()

        if np.any(next_acceleration) != None:
            self.acceleration = next_acceleration
        else:
            self.dead = True

        self.velocity += self.acceleration
        self.velocity = np.clip(self.velocity, -self.max_speed, self.max_speed)
        
        self.position += self.velocity

    def show(self):
        color = (0, 0, 0)
        radius = self.dot_radius

        if self.is_best:
            color = (0, 128, 0)
            radius = 6

        pygame.draw.circle(self.window, color, (int(self.position[0]), int(self.position[1])), radius)

    def update(self):
        position_x = self.position[0]
        position_y = self.position[1]

        if self.__check_edges_collision(position_x, position_y):
            self.dead = True
        if not self.dead and self.__check_goal_collision(position_x, position_y):
            self.reached_goal = True

        if (not self.dead) and (not self.reached_goal):        
            self.__move()

    def calculate_fitness(self):
        goal_x, goal_y = 300, 50
        goal_width, goal_height = 200, 15

        # 1.0/16.0: Este termo é adicionado como um bônus fixo para recompensar o Dot por alcançar o objetivo, 
        # podendo ser alterado para melhor pontuação.
        ##############################################
        # 10000.0/(float)(brain.step * brain.step): Este termo é inversamente proporcional ao quadrado do número de passos (brain.step * brain.step). 
        # Isso significa que quanto menos passos o Dot leva para alcançar o objetivo, maior será a aptidão. 
        # O fator 10000 é usado para garantir que a aptidão seja significativamente afetada pela quantidade de passos, 
        # proporcionando uma recompensa substancial para Dots que alcançam o objetivo em menos passos.

        if self.reached_goal:
            fitness = 1.0 / 16.0 + 10000.0 / (self.brain.step * self.brain.step)
        else:
            distance = self.__get_distance_dot_goal(self.position[0], self.position[1], 
                                              (goal_x + goal_width / 2), (goal_y + goal_height / 2))
            fitness = 1.0 / (distance * distance)

        self.fitness = fitness
        
    def reproduce(self):
        new_generation_dot = Dot(self.window)
        new_generation_dot.brain = self.brain

        return new_generation_dot

        
       


