import random
from itertools import permutations

def embaralhar_lista(x: list, y: list):
    """Embaralha a lista adicionada, de modo que o próximo retorno seja sempre diferente do anterior.
    Se o número de embaralhamentos máximo for alcançado, a função para de retornar novos valores.
    Obs: Além da lista com os valores a serem reordenados, é necessário criar uma lista vazia antes de chamar a função e passar como segundo parâmetro.
    A função irá retornar a lista que guarda apenas os novos valores"""
    while True:
        random.shuffle (x)
        if x not in y:
            y.append (x.copy ())
            break
        elif x in y:
            pass
        if len (y) == len (list (map (", ".join, permutations (x)))):
            break
            print ("Permutações máximas")
    return y
