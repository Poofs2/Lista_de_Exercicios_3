# Somar os Números de Uma Lista (com reduce)

'''
Exercicio 3:
Cria uma Função que, Utilizando reduce e uma Função lambda, 
Receba uma Lista de Números Inteiros e Retorne a Soma Total
dos Números

Exemplo de Entrada: [1, 2, 3, 4]
Exemplo de Saída: 10
'''
from functools import reduce

# --- Exercise 3 ---
print("--- Exercise 3 ---")

array1 = [1, 2, 3, 4, 5]
summ = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(f"The Sum of {array1} = {summ}")

print("------------------")
# --- Exercise 3 ---