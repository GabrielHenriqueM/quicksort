# funcao incorreta
# def sep(array, left, right):
#     j = right
#     for i in range(right - 1, left - 1, -1):
#         if array[i] > array[right]:
#             array[i], array[right] = array[right], array[i]
#             j = i
#     return j

# explicacao:
# a funcao tenta particionar o vetor usando array[right] como pivo
# problema:
# a troca entre array[i] e array[right] move o pivo de lugar varias vezes
# isso bagunca a divisao entre elementos menores e maiores que o pivo
# o pivo nao fica na posicao final correta
# o vetor pode nao ser ordenado corretamente

# implementacao correta
# def partition(array, left, right):
#     pivo = array[right]
#     i = left - 1
#     for j in range(left, right):
#         if array[j] <= pivo:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[right] = array[right], array[i + 1]
#     return i + 1

# explicacao:
# percorre o vetor da esquerda ate right - 1
# para cada elemento menor ou igual ao pivo, faz a troca para frente
# no final troca o pivo com array[i + 1]
# garante que todos menores ou iguais ao pivo fiquem antes
# garante que todos maiores fiquem depois
# o pivo fica na posicao correta
