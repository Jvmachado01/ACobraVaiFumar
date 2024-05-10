# Embora tuples sejam imutáveis, há algumaso operações que podemos fazer.

# Desempacotamento de Tuples
coordinates = (3, 5)
x, y = coordinates
print("x:", x, "y:", y)

# Acesso a Elementos
numerosTuple = (10, 20, 30, 40, 50)
print(numerosTuple[0], numerosTuple[-1])

# Concatenar Tuples
frutasCitricasTuple = ("amora", "abacate")
frutasMuitaAguaTuple = ("melancia", "melão")
todasAsFrutasTuple = frutasCitricasTuple + frutasMuitaAguaTuple
print(todasAsFrutasTuple)

# Multiplicação de Tuple para multiplicar elementos
verdurasTuple = ("alface", "rúcula")
verdurasTupleMultiplicacao = verdurasTuple  * 2
print(verdurasTupleMultiplicacao) 

# Indexação e contagem de Elementos
legumes = ("abobrinha", "batata", "beterraba", "cenoura", "batata")
legumesIndex = legumes.index("batata")
legumesCount = legumes.count("batata")
print("Index:", legumesIndex, "Count:", legumesCount) # Index: 1 Count: 2

# comparação de tuples
print(verdurasTuple > legumes) # True
