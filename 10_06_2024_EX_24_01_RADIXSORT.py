#João
def counting_sort_for_radix(arr, exp1):
    n = len(arr) # Obtém o tamanho do array
    output = [0] * n # Cria um array de saída com o mesmo tamanho do array de entrada, preenchido com zeros
    count = [0] * 10 # Cria um array para contar as ocorrências de cada dígito, inicialmente preenchido com zeros

    #Joao Contagem de ocorrências dos dígitos
    for i in range(n):
        index = arr[i] // exp1 # Calcula o índice do dígito atual
        count[index % 10] += 1 # Incrementa o contador para o dígito atual

    #Joao Mudança de count[i] para a posição real deste dígito na saída
    for i in range(1, 10):
        count[i] += count[i - 1] # Atualiza o contador para indicar a posição correta do dígito na saída
        
    #jamile Construindo a saída
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1 # Calcula o índice do dígito atual
        output[count[index % 10] - 1] = arr[i] # Coloca o número na posição correta na saída
        count[index % 10] -= 1 # Decrementa o contador
        i -= 1

    #Jamile Copiando a saída para arr[], para que arr agora contenha números ordenados
    for i in range(len(arr)):
        arr[i] = output[i] # Copia os elementos ordenados de volta para o array original

#Jamile
def radix_sort(arr):
    max1 = max(arr) # Encontra o maior número no array
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp) # Chama a função de ordenação por dígito
        print(f"Após ordenar com exp={exp}: {arr}") # Exibe o estado do array após cada passo principal de ordenação
        exp *= 10 # Incrementa o expoente para mover para o próximo dígito

#Ismael
def main():
    # Entrada de valores pelo usuário
    numbers = [int(x) for x in input("Digite os números a serem ordenados, separados por espaços: ").split()]
    print("Array original:", numbers) # Exibe o array original fornecido pelo usuário
    radix_sort(numbers) # Chama a função de ordenação Radix Sort
    print("Array ordenado:", numbers) # Exibe o array ordenado

#Ismael
if __name__ == "__main__":
    main()
#Ajuda a organizar o código de forma que certas partes
#só sejam executadas quando o arquivo é usado como programa principal,
#e não quando é importado em outro lugar.
#Isso ajuda a evitar a execução de código indesejado ao importar o arquivo como um módulo.