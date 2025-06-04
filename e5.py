# vetor: 55 44 22 11 66 33

# sequencia de chamadas:

# quicksort(array, 1, 6)
#     quicksort(array, 1, 4)
#         quicksort(array, 1, 0)
#         quicksort(array, 2, 4)
#             quicksort(array, 2, 2)
#             quicksort(array, 4, 4)
#     quicksort(array, 6, 6)

# explicacao:
# primeiro a funcao particiona o vetor usando 33 como pivo
# os menores ou iguais a 33 vao para a esquerda
# depois a funcao recursivamente ordena a parte da esquerda (1 a 4)
# subdivide ate subvetores de 1 elemento
# depois ordena a parte da direita (6 a 6)
# a recursao termina quando o subvetor tem 0 ou 1 elemento
