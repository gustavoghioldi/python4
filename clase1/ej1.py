# Dada 2 listas con números enteros, crear una tercera con los
# números que pertenecen a ambas. Pero con la salvedad que
# en esta tercera no debe tener elementos repetidos.

def is_in( n1:int, li: list)->int:
    """
    nos devuelve un numero si esta en la lista o False si no esta
    """
    # if n1 in li:
    #     return n1
    # else:
    #     return False
    return n1 if n1 in li else False

if __name__ == '__main__':
    primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
    segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
    tercera = []
    for i in primera:
        if is_in(i , segunda):
            if not(is_in(i, tercera)):
                tercera.append(i)
    print(tercera)