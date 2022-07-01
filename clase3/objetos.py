class Person: # aca declaro la clase (molde de un objeto)
    def __init__(self, age, nombre, dni):
        print("Nacio una nueva persona")
        self.age = age
        self.name = nombre
        self.dni = dni

    def saludar(self, am_pm):
        if am_pm == "AM":
            return f"Buen dia soy {self.name}"    
        if am_pm == "PM":
            return f"Buenas tardes soy {self.name}"
        else:
            return f"HOLA soy {self.name}"
                
p1 = Person(12, "Juan", 23232323) # aca creo el objecto
p2 = Person(45, "Pedro", 23232222)

print(id(p1))
print(id(p2))
# p3 = Person()
# print(id(p3))
p1.age = 33
for i in [p1, p2]:
    print(f"mi nombre es {i.name}, mi edad {i.age} y mi dni {i.dni}")
    print(i.saludar(None))
print(p1.saludar("AM"))
print(p2.saludar("PM"))    