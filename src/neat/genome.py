"""O genoma contém informações sobre a arquitetura da rede neural, 
incluindo os nós e as conexões entre eles. Cada conexão é representada por um gene de conexão, 
que contém informações sobre os nós de entrada e saída, o peso da conexão e um número de inovação único.
Além disso, cada nó tem um identificador único e uma função de ativação."""

"""A mutação é um aspecto essencial do algoritmo NEAT.
Permite a introdução de novas informações genéticas na população, 
permitindo a exploração de novos comportamentos."""

from neat.connection_gene import ConnectionGene
from neat.node import NodeType, Node

import random
import math

class Genome:
    def __init__(self, input_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.output_nodes = output_nodes
        self.nodes = {}  # Inicialização do dicionário para armazenar os nós do genoma
        self.connections = {}  # Inicialização do dicionário para armazenar as conexões do genoma

        # Inicializa os nós de entrada e saída com identificadores sequenciais
        for i in range(input_nodes):
            self.nodes[i] = Node(i, NodeType.INPUT)
        for i in range(input_nodes, input_nodes + output_nodes):
            self.nodes[i] = Node(i, NodeType.OUTPUT)

        # Inicializa as conexões entre os nós de entrada e saída
        innovation_number = 0
        for id_input in range(input_nodes):
            for id_output in range(input_nodes, input_nodes + output_nodes):
                # Verifica se os identificadores de nós estão dentro do intervalo esperado
                if id_input in self.nodes and id_output in self.nodes:
                    self.connections[innovation_number] = ConnectionGene(innovation_number, id_input, id_output, random.uniform(-1, 1), True)
                    innovation_number += 1
                else:
                    print("Identificador de nó inválido: ({}, {})".format(id_input, id_output))

    def create_random_genome(self, input_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.output_nodes = output_nodes

        # Adiciona nós de entrada
        for i in range(input_nodes):
            input_node = Node(i, NodeType.INPUT)
            input_node.set_layer(0)  # Define a camada como 0 (camada de entrada)
            self.nodes[i] = input_node

        # Adiciona nós de saída
        for i in range(output_nodes):
            output_node = Node(input_nodes + i, NodeType.OUTPUT)
            output_node.set_layer(1)  # Define a camada como 1 (camada de saída)
            self.nodes[input_nodes + i] = output_node

        # Adiciona algumas conexões aleatórias
        for input_node in range(input_nodes):
            for output_node in range(input_nodes, input_nodes + output_nodes):
                if random.random() < 0.5:  # Probabilidade de 50%
                    weight = random.uniform(-1, 1)
                    self.add_connection(input_node, output_node, weight)

    def add_connection(self, input_node, output_node, weight):
        connection = (input_node, output_node)
        self.connections[connection] = weight

    def add_node(self, node_id, node_type):
        self.nodes[node_id] = node_type

    def mutate(self, mutation_rate, new_node_rate, new_connection_rate):
            """Realiza mutações no genoma com base em taxas de mutação."""
            # Mutação de conexões
            for connection in self.connections.values():
                if random.random() < mutation_rate:
                    connection.mutate_weight()

            # Mutação de nós
            if random.random() < new_node_rate:
                self.add_new_node()

            # Mutação de novas conexões
            if random.random() < new_connection_rate:
                self.add_new_connection()

    def activation_function(self, x):
        # Função de ativação sigmóide
        return 1 / (1 + math.exp(-x))

    def feed_forward(self, inputs):

        """Nesta implementação, primeiro inicializamos os valores de entrada nos neurônios da camada de entrada
        com base nos valores de entrada fornecidos. Em seguida, propagamos esses valores através das conexões da rede,
        atualizando os valores dos neurônios de destino. Depois disso, aplicamos a função de ativação aos neurônios 
        das camadas ocultas e de saída. Por fim, obtemos as saídas da rede neural e as retornamos."""

        # Inicializa os valores de entrada nos neurônios da camada de entrada
        for i in range(len(self.nodes)):
            if self.nodes[i].node_type == NodeType.INPUT:  # Verifica se o nó é de entrada
                self.nodes[i].value = inputs[i]
            else:
                self.nodes[i].value = 0  # Inicializa o valor do neurônio para camadas ocultas e de saída

        # Propaga os sinais de entrada pelas conexões da rede
        for connection in self.connections.values():
            if connection.enabled:
                # Obtém os neurônios de origem e destino da conexão
                source_node = self.nodes[connection.input_node_id]
                target_node = self.nodes[connection.output_node_id]

                # Acumula o valor do neurônio de destino com o novo valor ponderado
                target_node.value += source_node.value * connection.weight

        # Ativação dos neurônios das camadas ocultas e de saída
        for node in self.nodes.values():
            if node.node_type != NodeType.INPUT:  # Ignora os neurônios da camada de entrada
                node.value = self.activation_function(node.value)

        # Obtém as saídas da rede neural
        outputs = []
        for node in self.nodes.values():
            if node.node_type == NodeType.OUTPUT:  # Verifica se o nó é de saída
                outputs.append(node.value)

        return outputs

    def add_new_connection(self):
        """Adiciona uma nova conexão ao genoma."""
        # Obtém todos os nós disponíveis para conexão
        available_nodes = list(self.nodes.values())

        # Remove nós de saída e nós desconectados
        available_nodes = [node for node in available_nodes if node.node_type != NodeType.OUTPUT and not self.__is_node_disconnected(node)]

        if len(available_nodes) < 2:
            return

        # Escolhe aleatoriamente dois nós para conectar
        in_node = random.choice(available_nodes)
        out_node = random.choice([node for node in available_nodes if node != in_node])

        # Verifica se a conexão já existe
        if self.__connection_exists(in_node.node_id, out_node.node_id):
            return

        # Adiciona a nova conexão
        new_connection = ConnectionGene(in_node.node_id, out_node.node_id, random.uniform(-1, 1), True, None)
        self.add_connection(new_connection)

    def __is_node_disconnected(self, node):
        """Verifica se um nó está desconectado."""
        for connection in self.connections.values():
            if connection.in_node_id == node.node_id or connection.out_node_id == node.node_id:
                return False
        return True

    def __connection_exists(self, in_node_id, out_node_id):
        """Verifica se uma conexão entre dois nós já existe."""
        for connection in self.connections.values():
            if connection.in_node_id == in_node_id and connection.out_node_id == out_node_id:
                return True
        return False