# Dicionário de Números Pares e Ímpares

'''
Exercicio 6:
Escreva uma Função que Receba uma Lista de
Números Inteiros e Utilize lambda e filter Para
Dividir a Lista em Números Pares e Ímpares.
Retorne um Dicionário com duas chaves:
"pares" e "ímpares".

Exemplo de Entrada: [1, 2, 3, 4, 5, 6]
Exemplo de Saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]}
'''

# --- Exercise 6 ---
print("--- Exercise 6 ---")

num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dictio = {
    "Even": list(filter(lambda x: x % 2 == 0, num_array)),
    "Odd": list(filter(lambda x: x % 2 != 0, num_array))
}
print(dictio)

print("------------------")
# --- Exercise 6 ---