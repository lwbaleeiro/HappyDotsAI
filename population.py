from dot import Dot
import numpy as np
import random

class Population:
    def __init__(self, window, size):
        self.generation = 1
        self.size = size
        self.window = window
        self.best_fitness = 0
        self.qtd_alives = size
        self.qtd_reached_goal = 0
        self.dots = []
        for _ in range(size):
            self.dots.append(Dot(window))

    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            dot.update()

    def all_dots_dead_or_reached_goal(self):

        self.qtd_alives = sum(not dot.dead for dot in self.dots)
        self.qtd_reached_goal = sum(dot.reached_goal for dot in self.dots)
        
        if ((self.qtd_alives - self.qtd_reached_goal) == 0):
            return True
                    
        return False

    def calculate_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()

    def natural_selection(self):
        new_dot_population = []

        # Pega o melhor Dot
        best_dot_fitness = self.calculate_best_dot_fitness()
        best_dot_son = best_dot_fitness.reproduce()
        best_dot_son.is_best = True
        # Adiciona ele a nova geração
        new_dot_population.append(best_dot_son)

        # A função do método "natural_selection" ele escolhe os Dots com menor fitness, o resto é descartado e criado novos.
        # Colocamos para pegar os 50% melhores fitness da ultima geração.
        percentage = int(len(self.dots) * 0.5)
        dots_best_fitness = np.argpartition([dot.fitness for dot in self.dots], percentage)[:percentage]
        for i in dots_best_fitness:
            new_dot_population.append(self.dots[i].reproduce())

        # Adiciona o restante da população -1 o melhor 
        for _ in range(int(len(self.dots) / 2) - 1):
            new_dot_population.append(Dot(self.window))   

        self.generation += 1
        self.dots = new_dot_population

    def calculate_best_dot_fitness(self):
        best_fiteness = 0
        best_dot = None

        for dot in self.dots:
            if (dot.fitness <= best_fiteness) or (best_fiteness == 0):
                best_fiteness = dot.fitness
                best_dot = dot

        self.best_fitness = best_dot.fitness
        return best_dot

    def mutation(self):
        # 1% de chance de acontecer uma mutação
        mutation_rate = 0.01
        num_dots_to_mutate = int(len(self.dots) * mutation_rate)
        dots_to_mutate = random.sample(self.dots, num_dots_to_mutate)

        for dot in dots_to_mutate:
            dot.brain.mutation()
