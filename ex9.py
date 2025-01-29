# Filtrar Tuplas com Média Maior que 5

'''
Exercicio 9:
Escreva uma Função que Receba uma Lista de Tuplas, Onde
Cada Tupla Contém Números Inteiros. Utilize map e filter
para Filtrar as Tuplas Cuja Média dos Valores
Seja Maior que 5

Exemplo de Entrada: [(2, 8), (4, 5, 6), (1, 2)]
Exemplo de Saída: [(2, 8), (4, 5, 6)]
'''
from functools import reduce

# --- Exercise 9 ---
print("--- Exercise 9 ---")
tuple_array = [(5, 8), (4, 7, 10), (3, 4), (9, 10)]

# Eu Tentei Fazer com "map" também, Mas Não Consegui Implementar de Modo que Funcione
medium = list(filter(lambda tuples: (sum(tuples) / len(tuples)) >= 5, tuple_array))
print(medium)

        
print("------------------")
# --- Exercise 9 ---