if __name__ == '__main__':
    with open("texto.txt", "w") as f:
        f.write("HOLA ARCHIVO!!!!!!\n")
        f.write("HOLA ARCHIVO2\n")
        f.write("HOLA ARCHIVO3!!!!!!")
    
    try:    
        with open("texto.txt", "r") as f:
            texto = f.read()
            print(texto)
            print(repr(texto))
            print(type(texto))
            
    except FileNotFoundError:
        print("no existe el archivo")
    
    #esta es legacy no es recomendable usar    
    f = open("texto.txt", "a")
    f2 = open("texto.txt", "a")
    f.write("otra linea")
    f2.write("otro archivo")
    f.close()
    f2.close()