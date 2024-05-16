import pygame
import random
import math
import numpy as np

from neat.genome import Genome
from environment.resource import Resource

class Dot:
    def __init__(self, x, y, radius=6):

        # Posição inicial
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y

        # Atributos físicos
        self.radius = radius  # Tamanho inicial
        self.energy = 100  # Energia inicial
        self.life = 100  # Vida inicial
        self.is_alive = True
        self.color = (90, 252, 3)  # Cor inicial
        self.move_speed = 1.6
        self.distance_traveled = 0

        # Atributos comportamentais
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]  # Velocidade inicial
        self.genome = Genome(3,2) # A rede neural do NEAT
        self.passive = False  # Indica se o dot é passivo
        self.collide = False  # Flag para colisão
        self.field_of_view = math.pi / 2  # Campo de visão em graus 90*
        self.detection_radius_distance = 60
        self.fitness = 0

        # Atributos de reprodução
        self.reproduction_rate = 0.01  # Taxa de reprodução
        self.attack_power = 10  # Poder de ataque
        self.energy_cost_move = 0.1  # Custo de energia para se mover
        self.energy_cost_attack = 5  # Custo de energia para atacar
        self.energy_cost_reproduce = 30  # Custo de energia para se reproduzir

        # Tempo vivo
        self.lifetime = 0

        # Atributos de colisão
        self.rect = pygame.Rect(self.x - self.radius // 2, self.y - self.radius // 2, self.radius, self.radius)

    def __find_nearest_resource(self, resources):
        nearest_resource = None

        for resource in resources:
            distance = math.sqrt((self.x - resource.x) ** 2 + (self.y - resource.y) ** 2)
            if distance < self.detection_radius_distance and self.__is_resource_within_field_of_view(resource):
                nearest_resource = resource
        return nearest_resource                

    def __is_resource_within_field_of_view(self, resource):
        angle_to_resource = math.atan2(resource.y - self.y, resource.x - self.x)
        angle_difference = abs(angle_to_resource - self.__get_angle())
        return angle_difference < self.field_of_view / 2

    def __get_angle(self):
        return math.atan2(self.velocity[1], self.velocity[0])
    
    def __move_towards(self, resource):
        angle_to_resource = math.atan2(resource.y - self.y, resource.x - self.x)
        self.velocity = [self.move_speed * math.cos(angle_to_resource), self.move_speed * math.sin(angle_to_resource)]
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def check_resource_collision(self, resources):
        for resource in resources:
            circle_center = (self.x, self.y)
            closest_point_x = max(resource.rect.left, min(circle_center[0], resource.rect.right))
            closest_point_y = max(resource.rect.top, min(circle_center[1], resource.rect.bottom))
            distance = math.sqrt((circle_center[0] - closest_point_x)**2 + (circle_center[1] - closest_point_y)**2)
            if distance <= self.radius:
                self.energy += resource.energy_value
                resources.remove(resource)
   
    def check_collision(self, object):
        # Verifica colisão com outro dot
        self.collide = self.rect.colliderect(object.rect)
        return self.collide

    def reproduce(self):
        # Verifica se o dot pode se reproduzir com base na taxa de reprodução e energia disponível
        if self.is_alive and self.energy > self.energy_cost_reproduce:
            self.energy -= self.energy_cost_reproduce  # Reduz a energia necessária para a reprodução
            # Aqui você implementaria a lógica para criar um novo dot com base nas características do pai
            new_dot = Dot(self.x, self.y, self.radius)
            return new_dot
        else:
            return None

    def attack(self, target_dot):
        # Ataca outro dot
        if self.is_alive and target_dot.is_alive:  # Verifica se ambos os dots estão vivos
            distance = math.sqrt((self.x - target_dot.x) ** 2 + (self.y - target_dot.y) ** 2)
            if distance <= self.radius:  # Verifica se o alvo está dentro do alcance de ataque
                target_dot.life -= self.attack_power  # Reduz a vida do alvo
                self.energy -= self.energy_cost_attack  # Reduz a energia do dot

    def calculate_inputs(self, resources):
        # Inicializa as variáveis de distância e ângulo
        distance_to_nearest_resource = 0
        angle_to_nearest_resource = 0

        # Encontra o recurso mais próximo, se houver
        nearest_resource = self.__find_nearest_resource(resources)
        if nearest_resource:
            # Calcula a distância para o recurso mais próximo
            distance_to_nearest_resource = math.sqrt((self.x - nearest_resource.x) ** 2 + (self.y - nearest_resource.y) ** 2)
            # Calcula o ângulo para o recurso mais próximo em relação à direção atual do dot
            angle_to_nearest_resource = math.atan2(nearest_resource.y - self.y, nearest_resource.x - self.x)

        # Retorna as informações calculadas como entradas para a rede neural
        return distance_to_nearest_resource, angle_to_nearest_resource, self.energy

    def update(self, resources):
        self.is_alive = self.energy > 0

        # Calcula as entradas da rede neural
        inputs = self.calculate_inputs(resources)
        # Processa as entradas na rede neural (ainda a ser implementado)
        neural_outputs = self.genome.feed_forward(inputs)
        # Processa as saídas da rede neural e toma decisões com base nelas
        self.process_outputs(neural_outputs)
        self.move()

    def move(self):
        # Movimenta o dot de acordo com sua velocidade
        if self.is_alive:
            self.prev_x = self.x
            self.prev_y = self.y

            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.energy -= self.energy_cost_move

            distance = math.sqrt((self.x - self.prev_x ) ** 2 + (self.y - self.prev_y) ** 2)
            self.distance_traveled += distance

            self.lifetime += 1   

    def get_input_vector(self, target_position):
        # Calcula o vetor de entrada para a rede neural com base na posição do alvo
        target_vector = np.array([target_position[0] - self.x, target_position[1] - self.y])
        target_vector /= np.linalg.norm(target_vector) if np.linalg.norm(target_vector) != 0 else 1  # Normaliza o vetor
        return target_vector       
    
    def decide_attack(self, target_dot):
        # Decide se o dot deve atacar o alvo com base na saída da rede neural
        if self.genome is not None:
            input_vector = self.get_input_vector((target_dot.x, target_dot.y))
            output = self.genome.feed_forward(input_vector)
            if output[0] > 0:  # Se a saída da rede for maior que 0, o dot ataca
                self.attack(target_dot)

    def evaluate_fitness(self):
        # Pontuação baseada na quantidade de comida consumida
        # food_score = self.energy - desativado por enquanto

        # Pontuação baseada no tempo de vida do dot
        time_score = self.lifetime

        # Pontuação baseada na distância percorrida
        distance_score = self.distance_traveled

        # Pontuação total (fitness) do dot
        fitness = time_score + distance_score

        return fitness

    def draw(self, screen):
        # Desenha o dot na tela
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def process_outputs(self, neural_outputs):
        # Processa as saídas da rede neural e toma decisões com base nelas
        move_direction = neural_outputs[0]
        action_decision = neural_outputs[1]
        
        # Ajusta a direção de movimento do dot com base na saída da rede neural
        self.adjust_movement_direction(move_direction)
        
        # Determina se o dot deve atacar ou reproduzir com base na saída da rede neural
        self.decide_action(action_decision)

    def adjust_movement_direction(self, move_direction):
        # Ajusta a direção de movimento do dot com base na saída da rede neural
        # Por exemplo, se a saída for positiva, vira para a direita; se for negativa, vira para a esquerda
        if move_direction > 0:
            # Vira para a direita
            self.rotate_clockwise()
        elif move_direction < 0:
            # Vira para a esquerda
            self.rotate_counter_clockwise()

    def decide_action(self, action_decision):
        # Determina se o dot deve atacar ou reproduzir com base na saída da rede neural
        # Por exemplo, se a saída for positiva, ataca; se for negativa, reproduz
        # if action_decision > 0:
        #     # Ataca
        #     self.attack()
        # elif action_decision < 0:
        #     # Reproduz
        #     self.reproduce()
        pass
    
    def rotate_clockwise(self):
        # Rotaciona o dot no sentido horário
        self.velocity = [self.velocity[1], -self.velocity[0]]  # Rotaciona a velocidade no sentido horário

    def rotate_counter_clockwise(self):
        # Rotaciona o dot no sentido anti-horário
        self.velocity = [-self.velocity[1], self.velocity[0]]  # Rotaciona a velocidade no sentido anti-horário