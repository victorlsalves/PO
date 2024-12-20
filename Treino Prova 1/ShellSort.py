import numpy as np

def shellsort(lista):
    gap = len(lista) // 2
    while gap > 0:
        for i in range(gap, len(lista)):
            aux = lista[i]
            j = i
            while j >= gap and lista[j - gap] > aux:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = aux
        gap //= 2
    return lista

lista = np.random.randint(1,1000,20)
print(lista)
print(shellsort(lista))