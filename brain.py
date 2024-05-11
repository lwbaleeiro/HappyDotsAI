import numpy as np
import random

class Brain:

    def __init__(self, size):

        self.step = 0
        self.directions = self.randomize_directions(size)
    
    def randomize_directions(self, size):
        random_directions = np.empty((size, 2))
        random_angles = np.random.uniform(0, 2 * np.pi, len(random_directions))

        random_directions[:, 0] = np.cos(random_angles)
        random_directions[:, 1] = np.sin(random_angles)
        
        return random_directions

    def get_next_acceleration(self):
        
        if len(self.directions) > self.step:
            acceleration = self.directions[self.step]
            self.step += 1
            return acceleration
        else:
            return None

    def mutate(self):
        mutation_rate = 0.01

        for i in range(len(self.directions)):
            if random.random() < mutation_rate:
                self.directions[i] = np.random.uniform(0, 2 * np.pi)