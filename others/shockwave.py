import pygame
import sys
import random
import math

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Explosion Effect")

# Cores
WHITE = (245, 66, 66)

# Função para desenhar o círculo
def draw_circle(radius, width, color, position):
    pygame.draw.circle(screen, color, position, radius, width)

# Função para desenhar as partículas
def draw_particles(particles):
    for particle in particles:
        pygame.draw.circle(screen, particle[2], (int(particle[0]), int(particle[1])), 2)

# Configurações iniciais do círculo
radius = 6
width = 36
color = WHITE
position = (WIDTH // 2, HEIGHT // 2)

# Lista de partículas
particles = []

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Atualizando o círculo
    width -= 1  # Reduzindo a largura da borda
    radius += 1  # Aumentando o raio

    # Dispersando partículas se a largura do círculo atingir zero
    if width <= 0:
        for _ in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            particles.append([position[0], position[1], WHITE, speed * math.cos(angle), speed * math.sin(angle)])
    
    # Atualizando a posição das partículas
    for particle in particles:
        particle[0] += particle[3]
        particle[1] += particle[4]

    # Limpando a tela
    screen.fill((0, 0, 0))

    # Desenhando o círculo
    if width > 0:
        draw_circle(radius, width, color, position)

    # Desenhando as partículas
    draw_particles(particles)

    # Atualizando a tela
    pygame.display.flip()

    # Delay para controlar a taxa de atualização
    pygame.time.delay(60)

pygame.quit()
sys.exit()
