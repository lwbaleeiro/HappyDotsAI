from dot import Dot

class Population:
    def __init__(self, window, size):
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