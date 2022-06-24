def div(n1:int, n2:int)->float:
    return n1/n2


if __name__ == '__main__':
    try:
        #print(div(1, 0))
        #int("HOLA")
        l = [1, 2, 3, 4]
        print(l[10])    
    except ZeroDivisionError:
        print("No puedo dividir por cero")
    except ValueError:
        print("Error en el valor")
    except IndexError:
        print("No tengo tantas opciones")     
    except Exception:
        print("exploto todo")
    
    
    print (" --- Fim del programa --- ")    
        
        