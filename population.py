from dot import Dot
import random

class Population:
    def __init__(self, window, size):

        self.generation = 1
        self.best_fitness = 0
        self.qtd_alives = size
        self.qtd_reached_goal = 0
        self.sum_fitness_population = 0

        self.dots = []

        for _ in range(size):
            self.dots.append(Dot(window))

    def __calculate_population_fitness(self):
        sum_fitness = 0
        
        for dot in self.dots:
            dot.calculate_fitness()
            sum_fitness += dot.fitness

        self.sum_fitness_population = sum_fitness

    def __get_best_dot(self):
        best_dot = None
        best_fitness = 0

        for dot in self.dots:
            if dot.fitness > best_fitness:
                best_fitness = dot.fitness
                best_dot = dot
        
        self.best_fitness = best_fitness
        best_dot.is_best = True
        return best_dot.reproduce()
        
    def __select_best_parents(self):
        random_finess_value = random.uniform(0, self.sum_fitness_population)
        running_sum = 0

        for dot in self.dots:
            running_sum += dot.fitness
            if (running_sum  > random_finess_value):
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
        new_dots = []

        self.__calculate_population_fitness()

        best_dot = self.__get_best_dot()
        if best_dot is not None:
            new_dots.append(best_dot)

        for _ in range(len(self.dots) -1):
            parent = self.__select_best_parents()
            new_dots.append(parent.reproduce())
        
        print(f"new dots {len(new_dots)}")

        self.generation += 1
        self.dots = new_dots
        self.__mutation()