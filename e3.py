# funcao errada
# def qsrt_errada(array, left, right):
#     # chamada da funcao partition para escolher o pivo
#     j = partition(array, left, right)
#     # condicao incorreta: pode ignorar vetor pequeno
#     if left < j - 1:
#         qsrt_errada(array, left, j - 1)
#     # condicao incorreta: pode ignorar vetor pequeno
#     if j + 1 < right:
#         qsrt_errada(array, j + 1, right)

# explicacao:
# o problema esta nas condicoes left < j - 1 e j + 1 < right
# quando o vetor tem 1 ou 2 elementos, essas condicoes impedem nova chamada da funcao
# um vetor com 2 elementos pode nao ser ordenado
# o algoritmo pode pular a ordenacao desse caso
# resultado: o vetor final pode ficar incorreto

# funcao corrigida
# def qsrt_correta(array, left, right):
#     # condicao correta para garantir a ordenacao completa
#     if left < right:
#         # chamada da funcao partition
#         j = partition(array, left, right)
#         # chamada recursiva para subvetor da esquerda
#         qsrt_correta(array, left, j - 1)
#         # chamada recursiva para subvetor da direita
#         qsrt_correta(array, j + 1, right)

# explicacao:
# usando left < right, garante-se que todos os subvetores serao tratados
# a funcao para apenas quando o subvetor tiver 1 ou 0 elementos
# dessa forma, todos os casos sao ordenados corretamente
