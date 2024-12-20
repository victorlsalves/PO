import numpy as np

def insertionsort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > pivo:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pivo

lista = np.random.randint(1, 1000, 20)
print(lista)
insertionsort(lista)
print(lista)