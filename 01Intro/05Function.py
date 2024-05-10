def soma(a, b):
    return a + b

print(soma(3, 7))

# Parâmetros nomeados: é explicito o nome durante a chamada da função
def dadosPessoais(nome, idade):
    print(nome + ", " + str(idade) + " anos")

dadosPessoais("João", 30) # usando ordem, não nomeação
dadosPessoais(idade=25, nome="John") # nomeado

# Parâmetro padrão
def saudacao(nome = "José", idade = 18):
    print("Olá, " + nome + "!")

saudacao()

# Funções Lambda:
'''
Funções lambda são funções anônimas de uma linha que podem ter
qualquer número de argumentos, mas apenas uma expressão. Elas são definidas
usando a palavra-chave lambda e são frequentemente usadas em situações onde 
uma função simples é necessária por um curto período de tempo.
'''
quadrado = lambda x, y: x ** y # x, y: é o nome do parâmetro
print("Quadrado:", quadrado(5, 3))

# Funções de Ordem Superior:
'''
Funções de ordem superior são aquelas que podem aceitar outras funções como
argumentos ou retorná-las como valores. Elas permitem uma programação mais
flexível e abstraída.
'''
def aplicarFuncao(lista, funcao):
    return [funcao(x) for x in lista]

resultado = aplicarFuncao([2, 3, 4, 5], lambda x: x ** 2)
print("Aplica função de ordem superior:", resultado)

# Função Documentada
def potencia(a = 2, b = 2):
    """Essa função retorna a potência"""
    return a ** b

print(potencia.__doc__)
print("potencia:", potencia(2, 3))


# Função Recursiva
'''
Recursão é um conceito em que uma função chama a si mesma diretamente 
ou indiretamente. É útil para resolver problemas que podem ser divididos
em subproblemas menores.
'''
def fatorial(n):
    if n == 0:
        return 1 # retorna 1 porque fatorial de 0 é 1
    else:
        return n * fatorial(n - 1)
    
print("Recursao. Fatorial:", fatorial(3)) # 3 x 2 x 1 = 6