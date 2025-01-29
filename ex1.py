# Dobrar elementos de uma lista (com map)

'''
Exercicio 1:
Escreva uma Função que, Utilizando map e uma Função 
lambda, Receba uma Lista de Números Inteiros e 
Retorne uma Nova Lista com Todos os Elementos Dobrados.
Exemplo de Entrada: [1, 2, Exemplo de Saída: [2, 4, 6, 8]
'''

# --- Exercise 1 ---
print("--- Exercise 1 ---")

array1 = [1, 2, 3, 4, 5]
double = list(map(lambda x: x*2, array1))

print(f"The Double of {array1} is {double}!")

print("------------------")
# --- Exercise 1 ---