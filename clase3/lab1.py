# Crea una clase “Persona”. Con atributos nombre y edad.
# Además, hay que crear un método “cumpleaños”, que
# aumente en 1 la edad de la persona cuando se invoque
# sobre un objeto creado con “Persona”.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cumpleanyos(self):
        self.edad += 1

p = Persona("Gus", 45)
print(f"mi nombre es {p.nombre} y mi edad : {p.edad}")

p.cumpleanyos()
print(f"mi nombre es {p.nombre} y mi edad : {p.edad}")

p.cumpleanyos()

print(f"mi nombre es {p.nombre} y mi edad : {p.edad}")

print(f"mi nombre es {p.nombre} y mi edad : {p.edad}")
print(p)
print(id(p))