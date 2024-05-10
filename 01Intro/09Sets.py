# Sets (conjuntos) úteis para lidar com coleções de elementos únicos

# Criação de conjunto
conjuntoNumeros = {1, 2, 3, 4, 5}
print(conjuntoNumeros)

# Adição de elementos
conjuntoNumeros.add(6)
conjuntoNumeros.add(7)
print(conjuntoNumeros) # {1, 2, 3, 4, 5, 6, 7}

# Remoção de elementos
conjuntoNumeros.remove(7)
print(conjuntoNumeros) # {1, 2, 3, 4, 5, 6}

# Verifica a existência de elementos:
print((2 in conjuntoNumeros), (10 in conjuntoNumeros))





# OPERAÇÕES DE CONJUNTOS

# Union
letras1 = {"A", "B", "C"}
letras2 = {"C", "D", "E"}
unionLetras = letras1.union(letras2) # {'E', 'B', 'D', 'C', 'A'}
print(sorted(unionLetras)) # ['A', 'B', 'C', 'D', 'E']

# Intersection
intersectionLetras = letras1.intersection(letras2)
print(intersectionLetras) # {'C'}

# Diference que retorna elementos presente no primeiro conjutno e ausentes no segundo
diferenceLetras = letras1.difference(letras2)
print(diferenceLetras) # {'A', 'B'}

# Diference Symmetric que retorna todos os elementos exclusivos de cada conjunto
symmetricDiferenca = letras1.symmetric_difference(letras2)
print(symmetricDiferenca) # {'A', 'D', 'E', 'B'}










# SET COMPREHENSION (compreensão de conjutnos) - cria conjunto com uma linha de código
'''
{expressão for item in iterável if condição}
expressão: O valor a ser incluído no conjunto.
item: A variável que representa cada item no iterável.
iterável: O objeto iterável (por exemplo, lista, tupla, conjunto)
    que você está percorrendo.
condição (opcional): Uma condição que determina se o item deve ser
     incluído no conjunto.
'''
# Conjunto de quadrados de numeros de 1 a 5
quadrados = {x ** 2 for x in range(1, 6)}
print("quadrados:", quadrados) # quadrados: {1, 4, 9, 16, 25}

# Usando uma condição para filtrar os itens a ser incluídos no conjunto
# Conjunto de quadrados de números pares de 1 a 10
quadradosPares = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print("Quadrado pares:", quadradosPares) # {64, 100, 4, 36, 16}









# Clear() para limpeza de conjuntos deixando-o vazio.
numerosConjutos = {1, 2, 3, 4, 5, 6}
print("Conjunto origial:", numerosConjutos)
numerosConjutos.clear()
print("Conjunto após a limpeza", numerosConjutos)
