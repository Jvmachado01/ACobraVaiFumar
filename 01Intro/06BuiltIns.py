'''
Os built-ins são funções integradas que estão sempre disponíveis no Python, 
ou seja, elas não precisam ser importadas de nenhum módulo para serem usadas. 
'''
# print() exie mensagem na saída padrão
print("Quero café!")

# len() comprimento (número de itens) de um objeto como lista, tupla, string
nome = "Jack Daniels"
print("len:", len(nome))

# range() gera sequência de números. Muito usada em loops.
for i in range(5):
    print(i)

# sum() calcula a soma de elementos de iteráveis como lista ou tupla
numeros = [1, 2, 3]
print("soma:", sum(numeros))   


# max() máximo de uma lista
contagem = [3, 2, 5]
print("Máximo:", max(contagem))

# sorted() para ordenar
print("sorted:", sorted(contagem))

# zip() combina elementos de duas ou mais listas (ou outros iteráveis) em pares
nomes = ["John", "Paul", "Lemmy"]
idades = [35, 40, 30]

for nome, idade in zip(nomes, idades):
    print(nome, idade)

'''
Uma coisa importante a notar é que zip() retorna um iterador,
então se você quiser armazenar os resultados em uma lista, 
você precisa convertê-lo em uma lista:
'''
pares = list(zip(nomes, idades)) # retorna uma lista de tuplas
print(pares, type(pares))