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
        
        self.sum_fitness_population = 0
        self.min_steps = 0

    def calculate_population_fitness(self):
        sum_fitness = 0
        
        for dot in self.dots:
            dot.calculate_fitness()
            sum_fitness += dot.fitness

        self.sum_fitness_population = sum_fitness
    
    def get_best_dot(self):
        best_dot = max(self.dots, key=lambda dot: (dot.fitness, dot.reached_goal, -dot.brain.step))
        self.best_fitness = best_dot.fitness
        best_dot.is_best = True
        if best_dot.reached_goal:
            self.min_steps = best_dot.brain.step
        return best_dot

    def select_best_parents(self):
        parent1 = random.choice(self.dots)
        parent2 = random.choice(self.dots)

        return max(parent1, parent2, key=lambda dot: dot.fitness)
 
    def mutation(self, mutation_rate=0.01):
        for dot in self.dots:
            if not dot.is_best:
                dot.brain.mutate(mutation_rate)
    
    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            dot.update()

    def all_dots_dead_or_reached_goal(self):

        self.qtd_alives = sum(not dot.dead for dot in self.dots)
        self.qtd_reached_goal = sum(dot.reached_goal for dot in self.dots)

        return self.qtd_alives - self.qtd_reached_goal == 0

    def natural_selection(self):

        self.calculate_population_fitness()
        new_dots = [self.get_best_dot().reproduce()]
        for _ in range(self.size - 1):
            parent = self.select_best_parents()
            new_dots.append(parent.reproduce())
        
        self.generation += 1
        self.dots = new_dots
        self.mutation()
