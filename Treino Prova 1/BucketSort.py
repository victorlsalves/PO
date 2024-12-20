import numpy as np

def bucketsort(lista):
    if len(lista) == 0:
        return []
    maximo = max(lista)
    minimo = min(lista)
    baldes = len(lista)
    lista_baldes = [[] for _ in range(baldes)]
    for num in lista:
        index = int((num - minimo) / (maximo - minimo + 1) * (baldes - 1))
        lista_baldes[index].append(num)

    lista_ordenada = []
    for baldes in lista_baldes:
        lista_ordenada(sorted(baldes))
    return lista_ordenada

lista = np.random.randint(1,1000,20)
print(lista)
print(bucketsort(lista))