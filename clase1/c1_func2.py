def sumar(n1, *args)->int:
    total = 0
    for i in args:
        total += i
    return f"{n1} {total}"

def super_function(name, doc,*args, otros="NADA",**kwargs):
    print(otros)
    print(name)
    print(doc)
    print(args)
    print(kwargs)
    
if __name__ == '__main__':
    # print(sumar("respuesta es: ", 100, 1, 10))
    # print(sumar("the response is: ", 1, 1, 10))
    super_function("Gustavo", "35625362", 1, 2,6, 7, 90, otros="OTROS DOCUMENTOS", a=5, b=33, n="hola")