import numpy as np

class Brain:

    def __init__(self, size):
        self.step = 0
        self.directions = np.empty((size, 2))

        self.randomize()
    
    def randomize(self):
        # Cria um array randomico do tamanho informado no parametro "size"
        random_angles = np.random.uniform(0, 2 * np.pi, len(self.directions))
        self.directions[:, 0] = np.cos(random_angles)
        self.directions[:, 1] = np.sin(random_angles)


    def get_next_acceleration(self):
        # Cada passo é reproduzido e limitado ao tamanho de "self.directions" junto com size
        if self.step < len(self.directions):
            acceleration = self.directions[self.step]
            self.step += 1
            return acceleration
        else:
            return None