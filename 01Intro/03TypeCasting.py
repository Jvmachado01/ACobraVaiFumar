# Quando um valor não puder ser convertido, uma exceção será gerada.

# int() para inteiro
valorString = "10901"
valorInt = int(valorString)
print(type(valorInt))

# float() para float
numInteiro = 10
numIntParaFloat = float(numInteiro)
print(type(numIntParaFloat))

# str() para String
idadeInt = 25
idadeIntParaString = str(idadeInt)
print(type(idadeIntParaString))

# bool() 
numeroFalse = 0
numeroBool = bool(numeroFalse)
print(type(numeroBool))

# list() converte um iterável para list
valorString = "Eu quero cafe"
valorLista = list(valorString)
print(valorLista, type(valorLista))

# tuple() converte um iterável para tuple
vogaisString = "AEIOU"
vogaisTupla = tuple(vogaisString)
print(vogaisTupla, type(vogaisTupla))

# dict() iterável de pares chave-valor para dicionário
valorLista = [("a", 1), ("b", 2), ("b", 3)] # lista de tuplas
valorDicionario = dict(valorLista)
print(valorDicionario, type(valorDicionario))

# set() converte iterável para conjunto
listaFrutas = ["maça", "limão", "laranja", "uva"]
conjuntoFrutas = set(listaFrutas)
print(conjuntoFrutas, type(conjuntoFrutas))