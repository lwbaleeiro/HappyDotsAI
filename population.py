from dot import Dot
import random
import numpy as np

class Population:
    def __init__(self, window, size):

        self.window = window
        self.size = size
        self.generation = 1
        self.best_fitness = 0
        self.qtd_alives = size
        self.qtd_reached_goal = 0
        self.dots = [Dot(window) for _ in range(size)]
        self.min_steps = 1000 # Mesmo que o brain, alterar depois
    
    def __get_best_dot(self):
        best_dot = max(self.dots, key=lambda dot: (dot.fitness, dot.reached_goal, -dot.brain.step))
        self.best_fitness = best_dot.fitness
        best_dot.is_best = True
        if best_dot.reached_goal:
           self.min_steps = best_dot.brain.step
        return best_dot

    def __select_best_parents(self):
        parent1 = random.choice(self.dots)
        parent2 = random.choice(self.dots)

        return max(parent1, parent2, key=lambda dot: dot.fitness)
    
    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            if dot.brain.step > self.min_steps:
                dot.dead = True
            else:
                dot.update()

    def all_dots_dead_or_reached_goal(self):

        self.qtd_alives = sum(not dot.dead for dot in self.dots)
        self.qtd_reached_goal = sum(dot.reached_goal for dot in self.dots)

        return self.qtd_alives - self.qtd_reached_goal == 0

    def natural_selection(self):    
        best_dot = self.__get_best_dot()
        new_dots = [best_dot]

        for _ in range(self.size - 1):
            parent = self.__select_best_parents()
            parent.brain.mutate()
            new_dots.append(parent.reproduce())
        
        self.generation += 1
        self.dots = new_dots
