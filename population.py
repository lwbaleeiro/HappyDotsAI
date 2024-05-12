import random
from dot import Dot

class Population:
    def __init__(self, window, size):
        self.window = window
        self.size = size
        self.generation = 1
        self.qtd_alives = size
        self.dots = [Dot(window) for _ in range(size)]
        self.min_steps = 1000
        self.best_dot_of_all = None  # Manter o registro do melhor Dot de todas as gerações
        self.qtd_reached_goal = 0

    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            if dot.brain.step > self.min_steps:
                dot.dead = True
            else:
                dot.update()

    def get_best_dot(self):
        best_dot = max(self.dots, key=lambda dot: dot.fitness)
        if self.best_dot_of_all is None or best_dot.fitness > self.best_dot_of_all.fitness:
            best_dot.is_best = True
            self.best_dot_of_all = best_dot
            self.min_steps = best_dot.brain.step

        return self.best_dot_of_all

    def select_best_parents(self):
        parent1 = random.choice(self.dots)
        parent2 = random.choice(self.dots)
        return max(parent1, parent2, key=lambda dot: dot.fitness)

    def all_dots_finished(self):

        self.qtd_alives = sum(not dot.dead for dot in self.dots)
        self.qtd_reached_goal = sum(dot.reached_goal for dot in self.dots)

        return self.qtd_alives - self.qtd_reached_goal == 0

    def natural_selection(self):    

        for dot in self.dots:
            dot.calculate_fitness()

        best_dot = self.get_best_dot()
        print(f"fitness: {self.best_dot_of_all.fitness} - is best = {self.best_dot_of_all.is_best}")
        new_dots = [best_dot.reproduce(self.min_steps)]

        for _ in range(self.size - 1):
           
            parent = self.select_best_parents()
            parent.brain.mutate()
            new_dots.append(parent.reproduce(self.min_steps))
        
        self.generation += 1
        self.dots = new_dots
