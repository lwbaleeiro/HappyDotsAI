from creatures.population_dots import PopulationDots
# from neat.neural_network import NeuralNetwork
from neat.genome import Genome

import numpy as np

def test_crossover_genomes():
    # Genomas de exemplo dos pais
    parent1_genome = [1, 2, 3, 4, 5]
    parent2_genome = [6, 7, 8, 9, 10]

    # Realizar o cruzamento dos genomas
    child_genome = population.crossover_genomes(parent1_genome, parent2_genome)
    
    # Exibir os resultados
    print("Parent 1 genome:", parent1_genome)
    print("Parent 2 genome:", parent2_genome)
    print("Child genome:", child_genome)

def test_addition_gene_mutation():

    # Criar uma população de dots com genomas aleatórios
    initial_population = 5  # Criar uma população inicial de 5 dots
    population = PopulationDots(initial_population)

    # Exibir os genomas antes da mutação
    print("Genomas antes da mutação de adição de gene:")
    for dot in population.dots:
        print(dot.genome)

    # Aplicar mutação de adição de gene
    mutated_population = [population.mutate_gene_addition(dot.genome) for dot in population.dots]

    # Exibir os genomas após a mutação
    print("\nGenomas após a mutação de adição de gene:")
    for genome in mutated_population:
        print(genome)

def test_remove_gene_mutation():
    # Criar uma população de dots
    population = PopulationDots(10)
    [population.mutate_gene_addition(dot.genome) for dot in population.dots]
    [population.mutate_gene_removal(dot.genome) for dot in population.dots]
    # Verificar se alguns dots tiveram genes removidos
    for dot in population.dots:
        print("Genome after remove gene mutation:", dot.genome)

def test_feed_forward():
    # Defina alguns valores de entrada
    inputs = [0.5, 0.3, 0.7]

    # Chame a função feed_forward com os valores de entrada
    outputs = genome.feed_forward(inputs)

    # Imprima as saídas obtidas
    print("Saídas da rede neural:", outputs)   

if __name__ == "__main__":

    # Population tests
    population = PopulationDots()
    test_crossover_genomes()
    test_addition_gene_mutation()
    test_remove_gene_mutation()

    # NN tests
    genome = Genome(3, 2)
    test_feed_forward()