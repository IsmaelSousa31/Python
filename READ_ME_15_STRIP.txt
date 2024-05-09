Objetivo:
O objetivo deste código é remover espaços em branco extras do início e do final de cada substring após dividir uma string original em substrings com base em um delimitador específico.

Como funciona:

Inicialmente, é definida uma string chamada frase, que contém espaços em branco extras no início e no final, além de uma vírgula como delimitador.
A string frase é dividida em substrings com base na vírgula, resultando em uma lista de substrings chamada lista_frases_cruas.
É criada uma lista vazia chamada lista_frases para armazenar as substrings limpas.
Um loop for é utilizado para iterar sobre cada substring na lista lista_frases_cruas.
Dentro do loop, cada substring é processada utilizando o método strip() para remover os espaços em branco extras do início e do final.
As substrings limpas são adicionadas à lista lista_frases.
Por fim, são impressas duas versões da lista de substrings: uma sem o uso do método strip() e outra com o uso do método strip().
Este código é útil quando você precisa limpar espaços em branco extras do começo e do final de substrings após dividir uma string com base em um delimitador específico, como uma vírgula. Isso garante que as substrings resultantes estejam formatadas corretamente para processamento adicional.