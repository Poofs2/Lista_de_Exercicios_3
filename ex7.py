# Agrupar Números em Categorias (com dicionários e lambdas)

'''
Exercicio 7:
Escreva uma Função que Receba uma Lista de Números Inteiros e
Utilize map e filter Para Criar um Dicionário que Agrupe os Números
em Três Categorias:

- "Positivos" (Números Maiores que 0)
- "Negativos" (Números Menores que 0)
- "Zeros" (Números iguais a 0)

Exemplo de Entrada: [1, -2, 0, 3, -5, 0]
Exemplo de Saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}
'''

# --- Exercise 7 ---
print("--- Exercise 7 ---")

num_array = [0, 1, 5, -3, -2, 4, 9, 0, 10, -1]
dictio = {
    "Positives": sorted(list(filter(lambda x: x > 0, num_array))),
    "Negatives": sorted(list(filter(lambda x: x < 0, num_array))),
    "Zeros": sorted(list(filter(lambda x: x == 0, num_array)))
}
print(dictio)

print("------------------")
# --- Exercise 7 ---