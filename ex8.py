# Contar Letras em uma Lista de Palavras (com map e reduce)

'''
Exercicio 8:
Crie uma Função que Receba uma Lista de Palavras
e Retorne a Soma Total de Letras em Todas as Palavras,
Utilizando map Para Contar as Letras e Reduce para Somar.

Exemplo de Entrada: ["casa", "python", "lambda"]
Exemplo de Saída: 16
'''
from functools import reduce

# --- Exercise 8 ---
print("--- Exercise 8 ---")
words_array = ["python", "food", "brodah", "pudding"]
sum_of_letters = reduce(lambda x, y: x + y, list(map(lambda word: len(word), words_array)))
print(f"The Sum of The Letters in The Words of {words_array} is: {sum_of_letters}")
print("------------------")
# --- Exercise 8 ---