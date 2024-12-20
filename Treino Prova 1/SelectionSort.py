import numpy as np

def selectionsort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min]:
                min = j
            lista[i], lista[min] = lista[min], lista[i]

lista = np.random.randint(1,1000,20)
print(lista)
selectionsort(lista)
print(lista)