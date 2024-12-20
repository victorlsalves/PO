import numpy as np

def quicksort(lista):
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    menores = [i for i in lista[1:] if i <= pivo]
    maiores = [i for i in lista[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

lista = np.random.randint(1, 1000, 20)
lista = lista.tolist()
print(lista)
lista = quicksort(lista)
print(lista)