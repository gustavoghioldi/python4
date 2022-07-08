class Vehiculo:
    def __init__(self, vel, model) -> None:
        self.velocidad = vel
        self.modelo = model

    def arrancar(self):
        print("arranque!")

class Terrestre(Vehiculo):
    def __init__(self, vel, modelo, ruedas):
        super().__init__(vel, modelo)
        self.ruedas = ruedas

    def arrancar(self):
        print ("Andando por tierra")
    def girar_ruedas(self):
        print ("estoy andando")

class Acuatico(Vehiculo):
    def arrancar(self):
        print( "Andando por Agua")
    def nadar(self):
        print("estoy en el agua")
class Aereo(Vehiculo):
    def arrancar(self):
        print("Andando Volando")
    def volar(self):
        print("estoy en el aire")    

class Anfibio(Terrestre, Acuatico):
    def arrancar(self):
        print(" voy por tierra o por agua")

auto = Terrestre(150, 2015, 4)

barco = Acuatico(25, 2008)

avion = Aereo(1000, 2017)


auto.arrancar() #polimorfismo
barco.arrancar()
avion.arrancar()
print("---------")
anf = Anfibio(30, 1998, 8)
anf.arrancar()
anf.girar_ruedas()
anf.nadar()

print(f"modelo:  {auto.modelo}, velocidad {auto.velocidad} y tengo {auto.ruedas} ruedas")