def sumar(num1: int = 1, num2: int =1 )->int:
    rta = num1 + num2
    return rta
    
# su = sumar(1, 3)
# print(f"respuesta --> {su}")
# print(f"respuesta --> {sumar(12, 2)}")
# print(f"respuesta --> {sumar(1, 234)}")
t = ("Gustavo", "Ariel", "Juan", )
def saludar(names: tuple, fu, n1=1)->None:
    """ Esta es una funcion que saluda
    Args:
        names (tuple): _description_
        fu (_type_): _description_
        n1 (int, optional): _description_. Defaults to 1.
    """
    for i in names:
        print(f"hola: {i}")
        print(fu(n1, len(i)))

if __name__ == '__main__':
    saludar(t, sumar)