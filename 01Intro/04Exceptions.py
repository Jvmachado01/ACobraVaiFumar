"""
                          BaseException
                               |
                           Exception
       ________________________|_______________________
      |                        |                       |
  ArithmeticError          LookupError          AssertionError
      |                        |                       |
ZeroDivisionError         IndexError               AttributeError
  OverflowError             KeyError                    |
FloatingPointError             |                        |
                           EOFError                 RuntimeError
                             IOError                    |
                              |                      NameError
                         ValueError                     |
                             OSError                    |
                                                      ...

===> Ver hierarquia de Exception na doc oficial para melhores tratamentos.

"""

# Exceções que geralmente precisam ser tratadas:

# FileNotFoundError
try: 
    with open("Arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado")

# ValueError

try: 
    arquivo = None
    arquivo = open("arquivo_nomes.txt", "r")
    nomes = arquivo.read()
    print(nomes)
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Inpunt/Output error")
finally:
    if arquivo:
        print("O arquivo foi fechado")
        arquivo.close()    

print("Fim do programa")

