import numpy as np

def mergesort(lista):
    if len(lista) < 2:
        return lista
    meio = len(lista) // 2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

lista = np.random.randint(1,1000,20)
lista = lista.tolist()
print(lista)
print(mergesort(lista))