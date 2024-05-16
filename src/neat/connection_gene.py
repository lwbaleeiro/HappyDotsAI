
"""Os genes de conexão representam as conexões entre os nós da rede neural. Cada gene de conexão tem um peso associado, que determina a força da conexão."""
import random

class ConnectionGene:
    def __init__(self, innovation_number, input_node_id, output_node_id, weight, enabled=True):
        self.innovation_number = innovation_number  # Número de inovação único do gene de conexão
        self.input_node_id = input_node_id  # ID do nó de entrada
        self.output_node_id = output_node_id  # ID do nó de saída
        self.weight = weight  # Peso da conexão
        self.enabled = enabled  # Flag para indicar se a conexão está habilitada

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def mutate_weight(self):
        """Mutates the weight of the connection."""
        self.weight += random.uniform(-0.1, 0.1)
