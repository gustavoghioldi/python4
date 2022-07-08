from modulos.mi_modulo import saludo, suma
from modulos.persona import Persona

from psutil import boot_time
from tabulate import tabulate

saludo()
print(suma(1, 4))

p = Persona("Gustavo")

print(p.name)

print(boot_time())

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(table))