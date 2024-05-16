## O Projeto

A simulação irá permitir que os usuários observem como essas criaturas evoluem ao longo do tempo, desenvolvendo diversas características, como tamanho, comportamento e morfologia. As características que surgem durante a simulação são influenciadas pelas interações entre as criaturas e com o ambiente.

O projeto oferece deve fornecer funcionalidades, incluindo:

Simulação em tempo real: A simulação pode ser executada em tempo real, permitindo que os usuários observem a evolução das criaturas em tempo real.
Visualização: A simulação fornece uma interface visual para acompanhar a evolução das criaturas e do ambiente.
Controle: Os usuários podem controlar diversos parâmetros da simulação, como a taxa de mutação e a taxa de seleção.
Análise: A simulação deve fornecer ferramentas para analisar os dados gerados pela simulação.
O projeto deve se assemelhar a evolução. A simulação pode ser utilizada para investigar diversas questões relacionadas à evolução, como o papel da mutação, da seleção natural e da interação e reprodução entre as criaturas.

* Ambiente 2D: Comece criando o ambiente 2D onde as criaturas viverão e interagirão. Você precisará definir as regras desse ambiente, como colisões, limites, obstáculos, fontes de alimentos, etc.

* Criaturas Iniciais: Crie um conjunto inicial de criaturas com características básicas. Elas podem ter atributos como velocidade, tamanho, visão, entre outros, que podem ser representados por números ou vetores.

* NEAT: Implemente NEAT para evoluir as redes neurais das criaturas. Isso envolve definir a estrutura da rede neural, incluindo o número de entradas (sensores), número de saídas (ações) e quaisquer parâmetros adicionais relevantes para a evolução.

* Interatividade: Desenvolva uma interface interativa usando Pygame para permitir que os usuários observem e interajam com a simulação. Isso pode incluir controles para ajustar parâmetros da simulação, como taxa de mutação e taxa de seleção.

* Visualização: Crie gráficos e animações para representar as criaturas, o ambiente e sua interação. Isso pode incluir representações visuais das redes neurais das criaturas e como elas respondem às mudanças no ambiente.

* Análise de Dados: Implemente ferramentas para coletar e analisar dados gerados pela simulação. Isso pode incluir estatísticas sobre a evolução das populações de criaturas ao longo do tempo, como taxa de sobrevivência, diversidade genética, entre outros.

* Tempo Real: Certifique-se de que a simulação possa ser executada em tempo real, permitindo que os usuários observem a evolução das criaturas enquanto ela acontece.

* Testes e Ajustes: Teste a simulação exaustivamente e faça ajustes conforme necessário para garantir que ela funcione conforme o esperado e ofereça uma experiência envolvente e educativa.


## TODO
* Adicionar comportamento de ataque mais avançado: Atualmente, o dot ataca outros dots se eles estiverem dentro do campo de visão. Você pode adicionar lógica para priorizar alvos com base em certas características, como dots com menos vida, dots mais próximos, etc.

* Adicionar evolução ao longo do tempo: Você pode implementar um sistema de evolução onde dots com comportamentos mais eficazes (como encontrar mais recursos, evitar predadores, reproduzir com sucesso) têm uma chance maior de passar seus genes para a próxima geração.

* Melhorar a visualização: Você pode adicionar elementos visuais para indicar o estado do dot, como barras de vida e energia, ícones de alerta quando um dot está sendo atacado ou quando detecta um recurso próximo, etc.