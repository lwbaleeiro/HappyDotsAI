import pygame

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path=None):
        super().__init__()
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((100, 100, 100))  # Cor padrão caso não haja imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
