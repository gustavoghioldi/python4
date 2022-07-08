import os

print(os.listdir())
print(os.getcwd())
try:
    os.mkdir("hola")
except FileExistsError:
    print("el directorio hola ya existe")

print(os.path.exists("./holasssss"))
os.rmdir("hola")
try:
    os.remove("texto.txt")
except FileNotFoundError:
    print("no existe el archivo texto.txt")    