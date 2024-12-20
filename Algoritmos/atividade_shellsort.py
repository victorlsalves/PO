# -*- coding: utf-8 -*-
"""Atividade ShellSort

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gk9k0J3nzqvIyou-7DGfDAgcfVxeAwyK

Gerando os números
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

lista1 = np.random.randint(0, 50000, 10000)
lista2 = np.random.randint(0, 50000, 20000)
lista3 = np.random.randint(0, 50000, 30000)
lista4 = np.random.randint(0, 50000, 40000)
lista5 = np.random.randint(0, 50000, 50000)

"""Copiando em listas para cada algoritmo"""

lista1_shell = lista1.copy()
lista2_shell = lista2.copy()
lista3_shell = lista3.copy()
lista4_shell = lista4.copy()
lista5_shell = lista5.copy()

lista1_bubble = lista1.copy()
lista2_bubble = lista2.copy()
lista3_bubble = lista3.copy()
lista4_bubble = lista4.copy()
lista5_bubble = lista5.copy()

"""Implementando o ShellSort"""

def shellsort(lista):
    gap = 1
    tamanho = len(lista)
    while gap > 0:
            for i in range(gap, tamanho):
                aux = lista[i]
                j = i
                while j >= gap and aux < lista[j - gap]:
                    lista[j] = lista[j - gap]
                    j = j - gap
                    lista[j] = aux
            gap = int(gap / 2.2) # reduzinho o intervalo
    return lista

"""Calculando o tempo"""

import time

start_time = time.time()
shellsort(lista1_shell)
end_time = time.time()
tempo1medio = end_time - start_time

start_time = time.time()
shellsort(lista2_shell)
end_time = time.time()
tempo2medio = end_time - start_time

start_time = time.time()
shellsort(lista3_shell)
end_time = time.time()
tempo3medio = end_time - start_time

start_time = time.time()
shellsort(lista4_shell)
end_time = time.time()
tempo4medio = end_time - start_time

start_time = time.time()
shellsort(lista5_shell)
end_time = time.time()
tempo5medio = end_time - start_time

"""Calculando o tempo do BubbleSort para as mesmas listas"""

def bubblesort(lista):
    for i in range(len(lista)-1):
      for j in range(len(lista)-1):

        if lista[j] > lista[j+1]:
          aux = lista[j]
          lista[j] = lista[j+1]
          lista[j+1] = aux

    return lista

start_time = time.time()
bubblesort(lista1_bubble)
end_time = time.time()
tempo1mediobubble = end_time - start_time

start_time = time.time()
bubblesort(lista2_bubble)
end_time = time.time()
tempo2mediobubble = end_time - start_time

start_time = time.time()
bubblesort(lista3_bubble)
end_time = time.time()
tempo3mediobubble = end_time - start_time

start_time = time.time()
bubblesort(lista4_bubble)
end_time = time.time()
tempo4mediobubble = end_time - start_time

start_time = time.time()
bubblesort(lista5_bubble)
end_time = time.time()
tempo5mediobubble = end_time - start_time

"""Comparando os tempos graficamente"""

tamanhos = [10000, 20000, 30000, 40000, 50000]

temposmedio = [tempo1medio, tempo2medio, tempo3medio, tempo4medio, tempo5medio]
plt.plot(temposmedio, tamanhos, marker='o', label='Caso Médio ShellSort')

temposmediobubble = [tempo1mediobubble, tempo2mediobubble, tempo3mediobubble, tempo4mediobubble, tempo5mediobubble]
plt.plot(temposmediobubble, tamanhos, marker='o', label='Caso Médio BubbleSort')

plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho da Lista')
plt.title('Comparação de Tempo de Execução dos Algoritmos')
plt.legend()
plt.show()