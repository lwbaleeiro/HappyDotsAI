from dot import Dot
import random

class Population:
    def __init__(self, window, size):

        self.generation = 1
        self.best_fitness = 0
        self.qtd_alives = size
        self.qtd_reached_goal = 0

        self.dots = []

        for _ in range(size):
            self.dots.append(Dot(window))

    def __get_best_dot(self):
        best_dot = None

        for dot in self.dots:
            if dot.fitness > self.best_fitness:
                self.best_fitness = dot.fitness
                best_dot = dot
        
        best_dot.is_best = True
        return best_dot

    def __calculate_population_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()
    
    def __sum_population_fitness(self):
        sum_fitness = 0
        for dot in self.dots:
            sum_fitness += dot.fitness

        return sum_fitness
        
    def __select_best_parents(self):
        sum_fitness = self.__sum_population_fitness()
        random_finess_value = random.uniform(0.0, sum_fitness)

        fitness_sum = 0
        for dot in self.dots:
            fitness_sum += dot.fitness
            if (fitness_sum > random_finess_value):
                return dot
            
        return None
    
    def __mutation(self):
        for dot in self.dots:
            if not dot.is_best:
                dot.brain.mutate()
    
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

    def natural_selection(self):

        self.__calculate_population_fitness()

        new_dots = []
        new_dots.append(self.__get_best_dot())

        for _ in self.dots:
            parent = self.__select_best_parents()
            new_dots.append(parent.reproduce())

        self.generation += 1
        self.dots = new_dots
        self.__mutation()