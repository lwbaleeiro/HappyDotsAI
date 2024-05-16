import random
from creatures.dot import Dot
from neat.node import Node, NodeType

GENE_MUTATION_RATE = 0.5
ADD_GENE_MUTATION_RATE = 0.4
REMOVE_GENE_MUTATION_RATE = 0.2

class PopulationDots():
    def __init__(self, size = 100):
        self.size = size
        self.dots = []

        # Criar a população inicial
        for _ in range(size):
            x = random.uniform(0, 1200)
            y = random.uniform(0, 900)
            dot = Dot(x, y)
            self.dots.append(dot)

    def calculate_total_fitness(self):
        total_fitness = 0
        for dot in self.dots:
            total_fitness += dot.fitness
        return total_fitness

    def evaluate_fitness(self):
        # Avaliar o fitness de cada dot na população
        for dot in self.dots:
            dot.fitness = self.calculate_fitness(dot)

    def calculate_fitness(self, dot):
        # Calcular o fitness de um dot
        # Aqui você pode usar critérios como tempo de vida, distância percorrida, etc.
        # Quanto maior o fitness, melhor o dot se saiu na simulação
        return dot.lifetime + dot.distance_travelled

    def select_parents(self):
        total_fitness = self.calculate_total_fitness()
        parents = []
        for dot in self.dots:
            # Calcula a probabilidade de ser escolhido como pai
            probability = dot.fitness / total_fitness
            # Adiciona o dot à lista de pais com base na sua probabilidade
            if random.random() < probability:
                parents.append(dot)
        # Retorna a lista de pais selecionados
        return parents

    def reproduce(self, selected_parents):
        new_generation = []
        for parent1, parent2 in selected_parents:
            # Cruzar os genomas dos pais para gerar os genomas dos filhos
            child_genome = self.crossover_genomes(parent1.genome, parent2.genome)

            # Criar um novo dot com o genoma do filho e adicionar à nova geração
            child_dot = Dot(0, 0, self.dot_radius)
            child_dot.brain.genome = child_genome
            new_generation.append(child_dot)
        return new_generation

    def crossover_genomes(self, parent1_genome, parent2_genome):
        """
        Performs crossover between two parent genomes to produce a child genome.
        """
        # Determine the crossover point
        crossover_point = random.randint(0, len(parent1_genome) - 1)
        
        # Create the child genome by combining parent genes
        child_genome = parent1_genome[:crossover_point] + parent2_genome[crossover_point:]
        
        return child_genome
    
    def mutate_gene_change(self, genome):
        if genome and random.random() < GENE_MUTATION_RATE:
            # Seleciona aleatoriamente um índice no genoma
            index = random.randint(0, len(genome) - 1)
            # Gera um novo valor aleatório para substituir o gene atual
            new_value = random.randint(1, 100)  # Aqui você pode ajustar o intervalo conforme necessário
            # Substitui o valor no índice selecionado pelo novo valor
            genome[index] = new_value     
            return genome
        
        return None
    
    def mutate_gene_addition(self, genome):
        """Mutação de adição de gene: adiciona um novo nó ao genoma."""
        # Escolhe uma conexão existente para adicionar um nó
        connection_key = random.choice(list(genome.connections.keys()))
        connection = genome.connections[connection_key]

        # Desabilita a conexão escolhida
        connection.enabled = False

        # Adiciona um novo nó e duas novas conexões
        new_node_id = len(genome.nodes)
        genome.nodes[new_node_id] = Node(new_node_id, NodeType.HIDDEN)  # Adiciona o novo nó como oculto

        # Adiciona as duas novas conexões conectando os nós originais ao novo nó
        genome.add_connection(connection.input_node_id, new_node_id, 1.0)  # Conexão com peso 1.0
        genome.add_connection(new_node_id, connection.output_node_id, connection.weight)  # Mantém o peso original da conexão

        return genome

    def mutate_gene_removal(self, genome):
        # Verifica se o genoma não está vazio
        if genome and random.random() < REMOVE_GENE_MUTATION_RATE:
            # Converte o genoma para uma lista de conexões
            connection_list = list(genome.connections.keys())
            # Verifica se há pelo menos dois genes (necessário para manter a viabilidade)
            if len(connection_list) >= 2:
                # Escolhe uma conexão aleatória para remover
                connection_key = random.choice(connection_list)
                # Remove a conexão do genoma
                del genome.connections[connection_key]

    def mutate(self):
        # Implementar a lógica de mutação do genoma aqui
        for dot in self.dots:
            self.mutate_gene_change(dot.genome)
            self.mutate_gene_addition(dot.genome)
            self.mutate_gene_removal(dot.genome)
    
    def evolve(self):
        # Evoluir a população para a próxima geração
        self.evaluate_fitness()
        self.select_parents()
        self.reproduce()
        self.mutate()

    def draw(self, screen):
        for dot in self.dots:
            dot.draw(screen)

    def update(self, resources):
         for dot in self.dots:
            dot.update(resources)       

    def check_resource_collision(self, resources):
        if resources is not None:
            for dot in self.dots:
                dot.check_resource_collision(resources)

    def check_collision(self, other_objects):
        if other_objects is not None:
            for dot in self.dots:
                for object in other_objects:
                    dot.check_collision(object)  
        