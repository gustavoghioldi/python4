# Se tiene una lista de personas como la siguiente:
# Se desea crear una función que ponga mayúscula
# solo en la primera letra, tanto del nombre como del
# apellido, y que devuelva la lista con esta
# modificación. 


 #["juan salvo","henry courtney","elizabeth bennet","marge simpson"]
def name_upper(noms:list)->list:
     aux = []
     for n in noms:
        nom , ape = n.split()
        aux.append(f"{nom.capitalize()} {ape.capitalize()}")
     return aux   
if __name__ == '__main__':
    noms  = ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]
    print(name_upper(noms))