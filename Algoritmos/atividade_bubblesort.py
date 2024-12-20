# -*- coding: utf-8 -*-
"""Atividade BubbleSort

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L572bVimPhVqtWf--ROhW0oS2R-YteeW

##Fazendo as listas e o algoritmo
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

lista1 = np.random.randint(10000, 50000, 1000)
lista2 = np.random.randint(10000, 50000, 2000)
lista3 = np.random.randint(10000, 50000, 4000)
lista4 = np.random.randint(10000, 50000, 6000)
lista5 = np.random.randint(10000, 50000, 8000)
lista6 = np.random.randint(10000, 50000, 10000)

def bubblesort(lista):
    for i in range(len(lista)-1):
      for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
          aux = lista[j]
          lista[j] = lista[j+1]
          lista[j+1] = aux
    return lista

"""##Calculando o tempo"""

import time

start_time = time.time()
bubblesort(lista1)
end_time = time.time()
tempo1medio = end_time - start_time

start_time = time.time()
bubblesort(lista1)
end_time = time.time()
tempo1melhor = end_time - start_time

lista1piorcaso = lista1[::-1]
start_time = time.time()
bubblesort(lista1piorcaso)
end_time = time.time()
tempo1pior = end_time - start_time

start_time = time.time()
bubblesort(lista2)
end_time = time.time()
tempo2medio = end_time - start_time

start_time = time.time()
bubblesort(lista2)
end_time = time.time()
tempo2melhor = end_time - start_time

lista2piorcaso = lista2[::-1]
start_time = time.time()
bubblesort(lista2piorcaso)
end_time = time.time()
tempo2pior = end_time - start_time

start_time = time.time()
bubblesort(lista3)
end_time = time.time()
tempo3medio = end_time - start_time

start_time = time.time()
bubblesort(lista3)
end_time = time.time()
tempo3melhor = end_time - start_time

lista3piorcaso = lista3[::-1]
start_time = time.time()
bubblesort(lista3piorcaso)
end_time = time.time()
tempo3pior = end_time - start_time

start_time = time.time()
bubblesort(lista4)
end_time = time.time()
tempo4medio = end_time - start_time

start_time = time.time()
bubblesort(lista4)
end_time = time.time()
tempo4melhor = end_time - start_time

lista4piorcaso = lista4[::-1]
start_time = time.time()
bubblesort(lista4piorcaso)
end_time = time.time()
tempo4pior = end_time - start_time

start_time = time.time()
bubblesort(lista5)
end_time = time.time()
tempo5medio = end_time - start_time

start_time = time.time()
bubblesort(lista5)
end_time = time.time()
tempo5melhor = end_time - start_time

lista5piorcaso = lista5[::-1]
start_time = time.time()
bubblesort(lista5piorcaso)
end_time = time.time()
tempo5pior = end_time - start_time

start_time = time.time()
bubblesort(lista6)
end_time = time.time()
tempo6medio = end_time - start_time

start_time = time.time()
bubblesort(lista6)
end_time = time.time()
tempo6melhor = end_time - start_time

lista6piorcaso = lista6[::-1]
start_time = time.time()
bubblesort(lista6piorcaso)
end_time = time.time()
tempo6pior = end_time - start_time

"""##Construindo os gráficos"""

tamanhos = [1000, 2000, 4000, 6000, 8000, 10000]
temposmedio = [tempo1medio, tempo2medio, tempo3medio, tempo4medio, tempo5medio, tempo6medio]
temposmelhor = [tempo1melhor, tempo2melhor, tempo3melhor, tempo4melhor, tempo5melhor, tempo6melhor]
tempospior = [tempo1pior, tempo2pior, tempo3pior, tempo4pior, tempo5pior, tempo6pior]
plt.plot(temposmedio, tamanhos, marker='o', label='Caso Médio')
plt.plot(temposmelhor, tamanhos, marker='o', label='Melhor Caso')
plt.plot(tempospior, tamanhos, marker='o', label='Pior Caso')
plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho da Lista')
plt.title('Gráfico do tempo de execução do algoritmo BubbleSort pelo tamanho de cada Lista')
plt.legend()
plt.show()