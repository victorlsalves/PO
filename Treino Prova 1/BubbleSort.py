import numpy as np

def bubblesort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

lista = np.random.randint(10,1000,20)
print(lista)
bubblesort(lista)
print(lista)