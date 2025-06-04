def quick_sort_decrescente_iterativo(array):
    def partition(array, inicio, fim):
        pivo = array[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            if array[j] > pivo:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[fim] = array[fim], array[i + 1]
        return i + 1

    stack = [(0, len(array) - 1)]
    while stack:
        inicio, fim = stack.pop()
        if inicio < fim:
            pivo_index = partition(array, inicio, fim)
            stack.append((inicio, pivo_index - 1))
            stack.append((pivo_index + 1, fim))

if __name__ == "__main__":
    vetor = [5, 2, 9, 1, 5, 6]
    quick_sort_decrescente_iterativo(vetor)
    print(vetor)
