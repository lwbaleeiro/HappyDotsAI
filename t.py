import numpy as np

class Carro:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco

# Suponha que tenhamos uma lista de objetos Carro
carros = [
    Carro("Fusca", 5000),
    Carro("Fusca_2", 5000),
    Carro("Gol", 8000),
    Carro("Civic", 15000),
    Carro("Corolla", 20000),
    Carro("BMW", 30000),
    Carro("Teste", 35000),
    Carro("Ferrari", 50000),
    Carro("Ferrari_2", 1000)
]

# Converter a lista de carros em um array NumPy para facilitar a manipulação
carros_array = np.array(carros)

# Usar numpy.partition para particionar a lista de carros de acordo com o preço
k = int(len(carros) * 0.5)  # Pegar metade dos carros mais baratos
indices_50_percentil = np.argpartition([carro.preco for carro in carros_array], 2)[:k]

# Pegar os carros correspondentes aos índices
carros_baratos = carros_array[indices_50_percentil]

# Imprimir os modelos e preços dos carros selecionados
print("Carros mais baratos:")
for carro in carros_baratos:
    print(carro.modelo, "- Preço:", carro.preco)