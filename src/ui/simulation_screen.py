

import pygame

from ui.pause_screen import PauseScreen
from ui.start_screen import StartScreen
from ui.controls import Controls

from creatures.population_dots import PopulationDots
from environment.resource_generator import ResourceGemerator

class SimulationScreen:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 900

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Happy Dot's AI")

        self.start_button = pygame.Rect(300, 300, 200, 50)
        self.quit_button = pygame.Rect(300, 370, 200, 50)
        self.resume_button = pygame.Rect(300, 300, 200, 50)

        self.controls =  Controls(self.screen, self.start_button, self.quit_button, self.resume_button)

        self.background_image = pygame.image.load("src/ui/images/noise.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.resources_generator = ResourceGemerator(self.screen, 55)
        self.resources_generator.generate_resources()

        self.population_dots = PopulationDots(100)   

    def run(self):
        running = True
        game_running = False
        paused = False

        start_screen = StartScreen(self.screen, self.start_button, self.quit_button)
        pause_screen = PauseScreen(self.screen, self.resume_button, self.quit_button)

        while running:
            game_running, paused = self.controls.handle_events(game_running, paused, self.population_dots)

            if not game_running:
                start_screen.draw()
            elif paused:
                pause_screen.draw()
            else: # Simulação rodando...
                self.screen.blit(self.background_image, (0, 0))

                self.population_dots.check_collision(None)
                self.population_dots.check_resource_collision(self.resources_generator.resources)
                self.population_dots.update(self.resources_generator.resources)
                self.population_dots.draw(self.screen)
                self.resources_generator.draw()

            pygame.display.flip()