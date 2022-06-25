# Ejercicio 1: Guardar datos
# Cree un algoritmo para guarda cada una de las
# personas del diccionario personas en un txt.
# El nombre se tiene que guardar en minúsculas y
# cada persona debe quedar en un renglón con un
# guión del medio separando el nombre y la edad.
# Ejemplo dentro del personas.txt se tendría que ver:
# roberto-20
# romina-32
# personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

def add_line(k:str, v):
    with open("personas.txt", "a") as f:
            try:
                line = f"{k.lower()}-{int(v)}"
                print(f"log:{line}")
                f.write(f"{line}\n")
            except ValueError:
                print(f"{v} --> no es un entero")
            
# shift + / 
if __name__ == '__main__':
    personas = {"Juan":20,"Romina":32, "gustavo":"hola", "Tamara":25,"Melanie":19}
    for k in personas.keys():
        add_line(k, personas[k])
       
            