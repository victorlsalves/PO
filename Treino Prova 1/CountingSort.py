import numpy as np

def countingsort(lista):
    if len(lista) == 0:
        return []
    maximo = max(lista)
    aux = [0] * (maximo + 1)
    for num in lista:
        aux[num] += 1
        lista_ordenada = []
        for i in range(len(aux)):
            lista_ordenada.extend([i] * aux[i])
    return lista_ordenada

lista = np.random.randint(1,1000,20)
print(lista)
print(countingsort(lista))