import sys

# print(sys.argv)
# print(type(sys.argv))
# print(sys.argv[1])
print(sys.argv[1:])
try:
    print (f"Hola : {sys.argv[1]}")
except IndexError:
    print("debe pasar un argumento con un nombre valido")

if sys.argv[1:]:
    for i in sys.argv[1:]:
        print(i)