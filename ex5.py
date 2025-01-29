# Elevar Números ao Quadrado e Ordenar (com map e sorted)

'''
Exercicio 5:
Crie uma Função que Eleve ao Quadrado Todos os Números de Uma Lista
Utilizanddo map, e Depois Retorne a Lista Ordenada

Exemplo de Entrada: [3, 1, 4, 2]
Exemplo de Saída: [1, 4, 9, 16]
'''

# --- Exercise 5 ---
print("--- Exercise 5 ---")
array1 = [1, 4, 5, 3, 2]
sqr_root = list(map(lambda x: x ** 2, array1))
print(f"The Square Root of {sorted(array1)} is: {sorted(sqr_root)}")

print("------------------")
# --- Exercise 5 ---