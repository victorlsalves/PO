# -*- coding: utf-8 -*-
"""Atividade CountingSort

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pUOF3KBuYaNOI_SsNkeYbB_nTSDvbk9-

Gerando os números
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

lista1 = np.random.randint(0, 50000, 200000)
lista2 = np.random.randint(0, 50000, 300000)
lista3 = np.random.randint(0, 50000, 400000)
lista4 = np.random.randint(0, 50000, 500000)
lista5 = np.random.randint(0, 50000, 600000)
lista6 = np.random.randint(0, 50000, 700000)
lista7 = np.random.randint(0, 50000, 800000)
lista8 = np.random.randint(0, 50000, 900000)
lista9 = np.random.randint(0, 50000, 1000000)

"""Copiando em listas diferentes"""

lista1_counting = lista1.copy()
lista2_counting = lista2.copy()
lista3_counting = lista3.copy()
lista4_counting = lista4.copy()
lista5_counting = lista5.copy()
lista6_counting = lista6.copy()
lista7_counting = lista7.copy()
lista8_counting = lista8.copy()
lista9_counting = lista9.copy()

lista1_quick = lista1.copy()
lista2_quick = lista2.copy()
lista3_quick = lista3.copy()
lista4_quick = lista4.copy()
lista5_quick = lista5.copy()
lista6_quick = lista6.copy()
lista7_quick = lista7.copy()
lista8_quick = lista8.copy()
lista9_quick = lista9.copy()

"""Immplementando o CountingSort"""

def countingsort(lista):
    if lista.size == 0:
        return lista
    maximo = 0
    lista_conta = []
    for num in lista:
        if num > maximo:
            maximo = num
    lista_conta = [0] * (maximo + 1)
    for num in lista:
        lista_conta[num] += 1
    for i in range(1, maximo + 1):
        lista_conta[i] += lista_conta[i - 1]
    for i, num in reversed(list(enumerate(lista))):
        lista[lista_conta[num] - 1] = num
        lista_conta[num] -= 1
    return lista

"""Calculando o tempo"""

import time

start_time = time.time()
countingsort(lista1_counting)
end_time = time.time()
tempo1medio = end_time - start_time

start_time = time.time()
countingsort(lista2_counting)
end_time = time.time()
tempo2medio = end_time - start_time

start_time = time.time()
countingsort(lista3_counting)
end_time = time.time()
tempo3medio = end_time - start_time

start_time = time.time()
countingsort(lista4_counting)
end_time = time.time()
tempo4medio = end_time - start_time

start_time = time.time()
countingsort(lista5_counting)
end_time = time.time()
tempo5medio = end_time - start_time

start_time = time.time()
countingsort(lista6_counting)
end_time = time.time()
tempo6medio = end_time - start_time

start_time = time.time()
countingsort(lista7_counting)
end_time = time.time()
tempo7medio = end_time - start_time

start_time = time.time()
countingsort(lista8_counting)
end_time = time.time()
tempo8medio = end_time - start_time

start_time = time.time()
countingsort(lista9_counting)
end_time = time.time()
tempo9medio = end_time - start_time

"""Implementando e calculando o tempo do QuickSort"""

def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        pivo = particao(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)
    return lista

def particao(lista, inicio, fim):
    meio = (inicio + fim) // 2
    if lista[inicio] > lista[fim]:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
    if lista[inicio] > lista[meio]:
        lista[inicio], lista[meio] = lista[meio], lista[inicio]
    if lista[meio] > lista[fim]:
        lista[meio], lista[fim] = lista[fim], lista[meio]
    pivo = lista[meio]
    lista[meio], lista[fim - 1] = lista[fim - 1], lista[meio]

    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

start_time = time.time()
quicksort(lista1_quick)
end_time = time.time()
tempo1medioquick = end_time - start_time

start_time = time.time()
quicksort(lista2_quick)
end_time = time.time()
tempo2medioquick = end_time - start_time

start_time = time.time()
quicksort(lista3_quick)
end_time = time.time()
tempo3medioquick = end_time - start_time

start_time = time.time()
quicksort(lista4_quick)
end_time = time.time()
tempo4medioquick = end_time - start_time

start_time = time.time()
quicksort(lista5_quick)
end_time = time.time()
tempo5medioquick = end_time - start_time

start_time = time.time()
quicksort(lista6_quick)
end_time = time.time()
tempo6medioquick = end_time - start_time

start_time = time.time()
quicksort(lista7_quick)
end_time = time.time()
tempo7medioquick = end_time - start_time

start_time = time.time()
quicksort(lista8_quick)
end_time = time.time()
tempo8medioquick = end_time - start_time

start_time = time.time()
quicksort(lista9_quick)
end_time = time.time()
tempo9medioquick = end_time - start_time

"""Construindo o gráfico"""

tamanhos = [200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

tempos = [tempo1medio, tempo2medio, tempo3medio, tempo4medio, tempo5medio, tempo6medio, tempo7medio, tempo8medio, tempo9medio]
plt.plot(tempos, tamanhos, marker='o', label='CountingSort')

tempos = [tempo1medioquick, tempo2medioquick, tempo3medioquick, tempo4medioquick, tempo5medioquick, tempo6medioquick, tempo7medioquick, tempo8medioquick, tempo9medioquick]
plt.plot(tempos, tamanhos, marker='o', label='QuickSort')

plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho da Lista')
plt.title('Comparação de Tempo de Execução do Algoritmo CountingSort com Listas grandes')
plt.legend()
plt.show()