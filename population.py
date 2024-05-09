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