import pygame
from environment.rock import Rock
import random

class RockGenerator:
    def __init__(self, screen, num_rocks=10, min_size=20, max_size=50, density=1.0, image_path=None):
        self.screen = screen
        self.rocks = pygame.sprite.Group()
        self.num_rocks = num_rocks
        self.min_size = min_size
        self.max_size = max_size
        self.density = density
        self.image_path = image_path

    def generate_rocks(self):
        area = self.screen.get_width() * self.screen.get_height()
        target_num_rocks = int(area * self.density / (self.max_size * self.max_size))
        actual_num_rocks = min(self.num_rocks, target_num_rocks)

        for _ in range(actual_num_rocks):
            x = random.randint(0, self.screen.get_width())
            y = random.randint(0, self.screen.get_height())
            width = random.randint(self.min_size, self.max_size)
            height = random.randint(self.min_size, self.max_size)
            rock = Rock(x, y, width, height, self.image_path)
            self.rocks.add(rock)

    def draw_rocks(self):
        self.rocks.draw(self.screen)

    def check_collisions(self, sprite):
        return pygame.sprite.spritecollide(sprite, self.rocks, False)
