import random
from dot import Dot

class Population:
    def __init__(self, window, size):
        self.window = window
        self.size = size
        self.generation = 1
        self.best_fitness = 0
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
        self.best_fitness = best_dot.fitness
        return best_dot

    def select_best_parents(self):
        parent1 = random.choice(self.dots)
        parent2 = random.choice(self.dots)
        return max(parent1, parent2, key=lambda dot: dot.fitness)

    def all_dots_finished(self):

        self.qtd_alives = sum(not dot.dead for dot in self.dots)
        self.qtd_reached_goal = sum(dot.reached_goal for dot in self.dots)

        return self.qtd_alives - self.qtd_reached_goal == 0

    def natural_selection(self):    
        best_dot = self.get_best_dot()
        if self.best_dot_of_all is None or best_dot.fitness > self.best_dot_of_all.fitness:
            self.best_dot_of_all = best_dot  # Atualiza o melhor Dot de todos se necessário

        new_dots = [best_dot]
        
        print(best_dot.brain.directions)

        for _ in range(self.size - 1):
           
            parent = self.select_best_parents()
            parent.brain.mutate()
            print(parent.fitness)
            new_dots.append(parent.reproduce(self.min_steps))
        
        print(f"best dot fitness {best_dot.fitness} - is best {best_dot.is_best}")
        # Reinicializa o melhor Dot de todas as gerações para próxima geração
        if self.best_dot_of_all is not None:
            new_dots[0].position = self.best_dot_of_all.position.copy()  # Reinicializa a posição inicial
            new_dots[0].velocity = self.best_dot_of_all.velocity.copy()  # Reinicializa o estado de movimento
            new_dots[0].brain.directions = self.best_dot_of_all.brain.directions.copy()  # Mantém as direções do cérebro
        
        self.generation += 1
        self.dots = new_dots
