import pygame

class StartScreen:
    def __init__(self, screen, start_button, quit_button):
        self.screen = screen
        self.start_button = start_button
        self.quit_button = quit_button
        self.font = pygame.font.Font(None, 26)

    def draw(self):
        self.screen.fill((0, 0, 0, 128))
        text = self.font.render("Happy Dot's AI", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() - 785, self.screen.get_height() - 640))
        self.screen.blit(text, text_rect)
        self.draw_button(self.start_button, "Start Simulation")
        self.draw_button(self.quit_button, "Quit")

    def draw_button(self, rect, text):
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        text_render = self.font.render(text, True, (0, 0, 0))
        text_rect = text_render.get_rect(center=rect.center)
        self.screen.blit(text_render, text_rect)