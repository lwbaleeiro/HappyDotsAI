import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições da janela
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Map Generator")

# Cores
COLORS = {
    "dark_blue": (0, 0, 128),
    "blue": (0, 0, 255),
    "light_grey": (192, 192, 192),
    "green": (0, 255, 0),
    "dark_green": (0, 128, 0),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255)
}

# Classe Node
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.el = 0
        self.temp = 0
        self.neighbors = []
        self.active = True

    def render(self):
        if self.el <= -25:
            color = "dark_blue"
        elif self.el <= map_data["cLevel"]:
            color = "blue"
        elif self.el <= 25 and self.temp <= 0:
            color = "light_grey"
        elif self.el <= 25 and self.temp <= 5:
            color = "green"
        elif self.el <= 25 and self.temp <= 10:
            color = "dark_green"
        elif self.el <= 25 and self.temp <= 100:
            color = "yellow"
        else:
            color = "white"
        
        rect = pygame.Rect(self.x * 5, self.y * 5, 5, 5)
        pygame.draw.rect(screen, COLORS[color], rect)

# Funções de geração e processamento do mapa
def generate_nodes():
    nodes = []
    for i in range(map_data["xy"][0]):
        for j in range(map_data["xy"][1]):
            nodes.append(Node(i, j))
    return nodes

def get_neighbors(nodes):
    for n1 in nodes:
        for n2 in nodes:
            if n1 != n2:
                if n1.x == n2.x:
                    if n2.y == n1.y + 1:
                        n1.neighbors.append(n2)
                elif n1.y == n2.y:
                    if n2.x == n1.x + 1:
                        n1.neighbors.append(n2)
                if len(n1.neighbors) >= 2:
                    break

def seed(nodes):
    for n in nodes:
        if 40 < n.x < 160 and 20 < n.y < 80:
            if random.randint(0, 1000) <= map_data["seed"]:
                n.el = random.choice(map_data["Choice"])
                n.temp = random.choice(map_data["Choice"])

def set_active(nodes):
    for n in nodes:
        n.active = True

def smooth_map(nodes):
    for n1 in nodes:
        n1.active = False
        for n2 in n1.neighbors:
            if n2.active and n1.el != n2.el:
                if random.randrange(0, 100) < 5:
                    a = (n1.el + n2.el) / 2
                    n1.el = a
                    n2.el = a
                elif random.randrange(0, 100) < 5:
                    a = (n1.temp + n2.temp) / 2
                    n1.temp = a
                    n2.temp = a

def raise_land(nodes):
    for n in nodes:
        if n.el > 0 and random.randrange(0, 100) < 1:
            n.el += 100

def lower_sea(nodes):
    for n in nodes:
        if n.el <= 0 and random.randrange(0, 100) < 1:
            n.el -= 100

def raise_temp(nodes):
    for n in nodes:
        if n.el > 0 and random.randrange(0, 100) < 1:
            n.temp += 10

# Dados do mapa
map_data = {
    "xy": [200, 100],
    "cLevel": 0,
    "nodes": [],
    "seed": 10,
    "Choice": [-100, 200]
}

# Geração dos nós
map_data["nodes"] = generate_nodes()
print("Generating Nodes")

# Obtenção dos vizinhos
print("Getting Neighbors")
get_neighbors(map_data["nodes"])

# Semente
print("Seeding")
seed(map_data["nodes"])

# Processamento do mapa
print("Processing...")
for i in range(100):
    set_active(map_data["nodes"])
    smooth_map(map_data["nodes"])
    raise_temp(map_data["nodes"])
print("1")
for i in range(15):
    set_active(map_data["nodes"])
    lower_sea(map_data["nodes"])
    raise_land(map_data["nodes"])
print("2")
for i in range(100):
    set_active(map_data["nodes"])
    smooth_map(map_data["nodes"])

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Renderização dos nós
    screen.fill(COLORS["blue"])
    for n in map_data["nodes"]:
        n.render()
    pygame.display.flip()

pygame.quit()
