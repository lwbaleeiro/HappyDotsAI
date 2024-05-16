## 1. Entender o algoritmo NEAT:
O NEAT (NeuroEvolution of Augmenting Topologies) é um algoritmo de neuroevolução que combina algoritmos genéticos com métodos de evolução de redes neurais. Ele foi projetado para evoluir redes neurais artificiais complexas, incluindo sua estrutura e pesos.

Principais conceitos:

Genótipo e Fenótipo: O genótipo representa a codificação genética de uma rede neural (como uma lista de genes), enquanto o fenótipo é a própria rede neural (sua arquitetura e conexões).
Especiação: Agrupamento de indivíduos em espécies com base na similaridade de seus genótipos.
Reprodução sexual: Cruzamento de genes de indivíduos para criar descendentes.
Mutação: Alteração aleatória de genes para introduzir diversidade na população.
Seleção: Processo de escolha dos indivíduos mais aptos para a próxima geração.

## 2. Definir a representação do genótipo:

No NEAT, o genótipo é representado por uma estrutura de dados que codifica a arquitetura e as conexões da rede neural. Isso geralmente é feito usando um grafo direcionado acíclico (DAG), onde os nós representam neurônios e as arestas representam conexões entre neurônios.

Componentes principais do genótipo:

Nós (nodes): Representam os neurônios da rede, incluindo nós de entrada, saída e ocultos.
Conexões (connections): Representam as conexões entre os neurônios, com pesos que determinam a força da conexão.
Passos para definir o genótipo:

Identificar os tipos de nós: Entrada, saída e ocultos, com identificadores únicos para cada tipo.
Criar os genes de conexão: Cada gene de conexão possui uma identificação única, bem como informações sobre o neurônio de entrada, o neurônio de saída e o peso da conexão.
Definir a estrutura de dados para armazenar o genótipo: Isso pode ser feito usando classes ou estruturas de dados em linguagens de programação orientadas a objetos.