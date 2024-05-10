import numpy as np

class Brain:

    def __init__(self, size):
        self.size = size
        self.step = 0
        self.directions = self.randomize_directions()
    
    def randomize_directions(self):
        random_directions = np.empty((self.size, 2))
        # Cria um array randomico do tamanho informado no parametro "size"
        random_angles = np.random.uniform(0, 2 * np.pi, len(random_directions))
        random_directions[:, 0] = np.cos(random_angles)
        random_directions[:, 1] = np.sin(random_angles)
        
        return random_directions

    def get_next_acceleration(self):
        # Cada passo é reproduzido e limitado ao tamanho de "self.directions" junto com size
        if self.step < len(self.directions):
            acceleration = self.directions[self.step]
            self.step += 1
            return acceleration
        else:
            return None
        
    def clone(self, brain_to_clone):
        self.directions = brain_to_clone.directions

    def mutation(self):
        self.directions = self.randomize_directions()