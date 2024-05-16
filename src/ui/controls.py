import pygame
import sys

class Controls:
    def __init__(self, screen, start_button, quit_button, resume_button):
        self.screen = screen
        self.start_button = start_button
        self.quit_button = quit_button
        self.resume_button = resume_button

    def handle_events(self, game_running, paused, population_dots):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_running:
                        paused = not paused

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_running:
                    if self.start_button.collidepoint(event.pos):
                        game_running = True

                    elif self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                else:
                    if paused:
                        if self.resume_button.collidepoint(event.pos):
                            paused = False
                        elif self.quit_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                            
        return game_running, paused
