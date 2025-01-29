# Filtrar Números Pares de uma Lista (com filter)

'''
Exercicio 2:
Escreva uma Função que, Utiizando filter
e uma Função lambda, Receba uma Lista
de Números Inteiros e Retorne Apenas
os Números Pares

Exemplo de Entrada: [1, 2, 3, 4, 5]
Exemplo de Saía: [2, 4]

'''

# --- Exercise 2 ---
print("--- Exercise 2 ---")
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, array1))
print(f"Even Numbers in {array1}: {even}")


print("------------------")
# --- Exercise 2 ---