# Nomes com Mais de 5 Letras (com filter)

'''
Exercicio 4:
Escreva uma Função que Receba uma Lista de Nomes e, Utilizando
filter, Retorne Apenas os Nomes com Mais de 5 Letras

Exemplo de Entrada: ["Ana", "Lucas", "Fernanda", "João"]
Exemplo de Saída: ["Lucas", "Fernanda"]
'''

# --- Exercise 4 ---
print("--- Exercise 4 ---")

name_array = ["Mario", "Luigi", "Carl", "Patrick", "Lynn", "Pedro", "Ana"]
name_filter = list(filter(lambda x: len(x) >= 5, name_array))
print(f"The Names With Less or Equal to 5 Letters are: {name_filter}")

print("------------------")
# --- Exercise 4 ---