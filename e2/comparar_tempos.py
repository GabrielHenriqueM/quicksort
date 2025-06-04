import random
import time
from quicksort_recursivo import quick_sort_decrescente
from quicksort_iterativo import quick_sort_decrescente_iterativo

def testar_quick_sort():
    tamanhos = [1000, 5000, 10000, 50000]
    resultados = []

    for tamanho in tamanhos:
        vetor_original = random.sample(range(1, 1000000), tamanho)
        
        vetor_recursivo = vetor_original.copy()
        vetor_iterativo = vetor_original.copy()

        inicio = time.time()
        quick_sort_decrescente(vetor_recursivo, 0, len(vetor_recursivo) - 1)
        fim = time.time()
        tempo_recursivo = fim - inicio

        inicio = time.time()
        quick_sort_decrescente_iterativo(vetor_iterativo)
        fim = time.time()
        tempo_iterativo = fim - inicio

        resultados.append((tamanho, tempo_recursivo, tempo_iterativo))

    print(f"{'Tamanho':>10} | {'Recursivo (s)':>15} | {'Iterativo (s)':>15}")
    for tamanho, rec, it in resultados:
        print(f"{tamanho:10} | {rec:15.6f} | {it:15.6f}")

if __name__ == "__main__":
    testar_quick_sort()
