from dot import Dot
import numpy as np

class Population:
    def __init__(self, window, size):
        self.size = size
        self.window = window
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
       
        for dot in self.dots:
            if (not dot.dead) and (not dot.reached_goal):
                return False
            
        return True

    def calculate_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()

    def natural_selection(self):
        dots_to_clone = []
        # A função do método "natural_selection" ele escolhe os Dots com menor fitness, o resto é descartado e criado novos.
        # Colocamos para pegar os 50% melhores fitness da ultima geração.
        percentage = int(len(self.dots) * 0.5)
        dots_best_fitness = np.argpartition([dot.fitness for dot in self.dots], percentage)[:percentage]
        for i in range(dots_best_fitness):
            dots_to_clone.append(self.dots[i])

        for dot in dots_to_clone:
            dot.clone(dot.brain)
        
