Objetivo: Dividir uma string em substrings com base em um caractere específico e retornar essas substrings em uma lista.
Este programa em Python ilustra como dividir uma string em substrings com base em um caractere específico, neste caso, a vírgula (','), e armazenar essas substrings em uma lista.

Como funciona o código:
A variável lista_de_compras contém a string que será dividida em substrings.
A função split(',') é aplicada à string lista_de_compras, onde a vírgula (',') é o caractere usado como delimitador para dividir a string em substrings.
O resultado da operação é armazenado na lista lista_com_virgula.
Em seguida, é criada uma lista vazia chamada lista para armazenar as substrings sem espaços em branco desnecessários.
Utilizando um loop for e a função strip() para remover espaços em branco desnecessários de cada substring, as substrings são adicionadas à lista lista.
Por fim, a lista resultante, contendo as substrings divididas, é impressa na tela.