

# append() para adicionar um elmeento no final da lista
frutasList = ["maça", "uva"]
frutasList.append("melancia")
print(frutasList)

# exdended() adiciona elementos de outra lista ao final da lista atual
frutasCitricas = ["laranja", "limão"]
frutasList.extend(frutasCitricas)
print(frutasList)

# insert() para inserir um elemento em uma posição específica da lista
frutasList.insert(1, "abacate")
print(frutasList)

# remove() remove o primeiro elemento com o valor especificado
frutasList.remove("abacate")
print(frutasList)

# pop() para remover e retornar o elemento em uma posição (último como padrão)
poppedElement = frutasList.pop()
print(frutasList)
print("Popped element:", poppedElement)

# index() para retornar o índice do primeiro elemento com o valor especificado
print("índice do elemento:", frutasList.index("uva"))

# outros: count(), sort(), rever(), para mais, vide documentação.