#calculadora
def calc (a , b):
    return ((a + b), (a -b), (a*b), (a/b))

def question():
    cond = True
    while cond:
        try:
            a = int(input("primer numero: "))
            b = int(input("segundo numero: "))
            rta = calc(a, b)
            print(f"suma = {rta[0]}")
            print("resta = {}".format(rta[1]))
            print("mult = " + str(rta[2]))
            print(f"dev = {rta[3]}")
            cond = False
        except ValueError:
            print("solo se pueden ingresar numeros")
        except ZeroDivisionError:
            print("el segundo numero no debe ser cero")

if __name__ == '__main__':
    question()
    