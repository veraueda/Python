def remove_repetidos(lista):
    lista.sort()
    x = 1
    while x < len(lista):
        if lista[x] == lista[x-1]:
            del lista[x-1]
        else:
            x = x + 1
    return lista
