import numpy as np
import random

class Brain:

    def __init__(self, directions = None):
        
        self.size = 1000
        self.step = 0   
        if directions is None:
            self.directions = self.randomize_directions(self.size)
        else:
            self.directions = directions 
    
    def randomize_directions(self, size):
        random_directions = np.empty((size, 2))
        random_angles = np.random.uniform(0, 2 * np.pi, len(random_directions))

        random_directions[:, 0] = np.cos(random_angles)
        random_directions[:, 1] = np.sin(random_angles)
        
        return random_directions

    def get_next_acceleration(self):
        
        if self.step < self.size :
            acceleration = self.directions[self.step]
            self.step += 1
            return acceleration
        else:
            return None

    def mutate(self, mutation_rate = 0.01):

        if np.random.rand() < mutation_rate:
            random_directions = np.empty((self.size, 2))
            random_angles = np.random.uniform(0, 2 * np.pi, len(random_directions))
            random_directions[:, 0] = np.cos(random_angles)
            random_directions[:, 1] = np.sin(random_angles)
            self.direction = random_directions