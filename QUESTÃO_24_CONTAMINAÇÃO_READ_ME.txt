Objetivo:
O objetivo deste código é calcular o número de pessoas contaminadas em um surto epidêmico com base em um modelo exponencial, onde o crescimento é proporcional ao número atual de pessoas contaminadas.

Como funciona:

O programa define uma função chamada modelo_exponencial que recebe três parâmetros: C0 (número inicial de pessoas contaminadas), B (número de pessoas que cada doente contamina por semana) e t (tempo em semanas decorrido desde o primeiro caso).
Dentro da função, é utilizada a função exponencial da biblioteca math para calcular o número de pessoas contaminadas (C) com base na fórmula C = C0 * math.exp(B * t).
Em seguida, o programa define uma função principal chamada main, que solicita ao usuário que insira os valores de C0, B e t.
Verifica-se se os valores inseridos são válidos (ou seja, se são números positivos) e, em caso de erro, uma mensagem apropriada é exibida.
Se os valores inseridos forem válidos, a função modelo_exponencial é chamada com esses valores e o resultado é exibido na tela, indicando o número aproximado de pessoas contaminadas após um determinado período de tempo.
Este código é útil para modelar o crescimento de casos em um surto epidêmico e pode ser usado para prever a propagação de doenças infecciosas com base em parâmetros específicos, como o número inicial de casos e a taxa de contágio. Ele fornece uma estimativa do número de casos em um determinado momento no tempo, ajudando a entender a evolução da epidemia e a tomar decisões informadas sobre medidas de controle e prevenção.