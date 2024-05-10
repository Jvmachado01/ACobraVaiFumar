# Dictionary para mapear "chave": valor


# Criando um dicionário
meuDicionario = {"a":1, "b": 2, "c": 3}
print(meuDicionario) # {'a': 1, 'b': 2, 'c': 3}

# Acesso a valores
print(meuDicionario['b']) # 2

# Adição ou Atualização de Pares Chave-Valor
meuDicionario["d"] = 4 # Adicona uma novo par
meuDicionario["a"] = 0 # Atualiza o valor da chave "a"
print(meuDicionario) # {'a': 0, 'b': 2, 'c': 3, 'd': 4}

# Remoção de pares Chave-Valor
del meuDicionario["b"]
print(meuDicionario) # {'a': 0, 'c': 3, 'd': 4}

# Verificar a existência de chaves
print("a" in meuDicionario) # True
print("z" in meuDicionario) # False

# Obtenção de listas de chaves, Valores e Pares Chave-Valor
keys = meuDicionario.keys()
values = meuDicionario.values()
items = meuDicionario.items()
print("Chaves:", keys) # dict_keys(['a', 'c', 'd'])
print("Values:", values) # dict_values([0, 3, 4])
print("Items:", items) # dict_items([('a', 0), ('c', 3), ('d', 4)])

# Obtendo valores com get()
valor = meuDicionario.get("a")
print(valor) # 0

# Limpeza de um dicionário
meuDicionario.clear()
print(meuDicionario) # {}




