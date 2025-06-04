def quick_sort_decrescente(array, inicio, fim):
    if inicio < fim:
        def partition(array, inicio, fim):
            pivo = array[fim]
            i = inicio - 1
            for j in range(inicio, fim):
                if array[j] > pivo:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[fim] = array[fim], array[i + 1]
            return i + 1
        
        pivo_index = partition(array, inicio, fim)
        quick_sort_decrescente(array, inicio, pivo_index - 1)
        quick_sort_decrescente(array, pivo_index + 1, fim)

if __name__ == "__main__":
    vetor = [5, 2, 9, 1, 5, 6]
    quick_sort_decrescente(vetor, 0, len(vetor) - 1)
    print(vetor)
