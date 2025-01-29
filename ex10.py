# Média Ponderada com Dicionário e reduce

'''
Exercicio 10:
Crie uma Função que Receba um Dicionário onde
as Chaves são Nomes de Alunos e os Valores são Listas
de Notas (Com Pesos na Última Posição). A Função
deve Calcular a Média Ponderada de Cada Aluno Usando reduce
e Retornar um Novo Dicionário com os Resultados.

Exemplo de Entrada:
{
    "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
    "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}

Exemplo de Saída:
{
    "João": 8.0,
    "Ana": 6.0
}
'''
from functools import reduce

# --- Exercise 10 ---
print("--- Exercise 10 ---")
# Média Ponderada: (a[0] * peso + a[1] * peso + a[2] * peso) / len[a] * peso

dictio_init = {
    "Pedro": [8, 6, 10, 2],
    "Maria": [4, 6, 8, 3],
    "Carlos": [5, 4, 9, 3]
}

new_dict = {key: None for key in dictio_init}
keys = list(new_dict.keys())
# print(dictio_init[keys[0]]) # <- Example on How to Call the Values
value = list(dictio_init.values())

for key in range(len(value)):
    val = value[key]
    apply_wgt = list(map(lambda x: x * val[-1], val))
    reduced = reduce(lambda x, y: x + y, val[:-1])
    medium = reduced / (len(val) - 1)
    new_dict[keys[key]] = medium

print(f"Old Dict:\n {dictio_init}")
print(f"New Dict:\n{new_dict}")
    
    
    
print("------------------")
# --- Exercise 10 ---