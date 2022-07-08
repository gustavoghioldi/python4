#unprogram python que ingrese por linea de comando un producto
# ese producto debe tener precio, nombre
# cada producto que vamos a crear se va a guardar en una linea en un archivo
# si llegamos: o para tarea, poder listar con otro archivo de python todos los productos en pantalla
# en el archivo
import sys
from modulos.product import DecimalPriceExec
from modulos.product import Product

if sys.argv[1:]:
    try:
        p = Product(sys.argv[1], sys.argv[2])
    except DecimalPriceExec:
        print("el segundo valor debe porder ser convertido a decimal")


    p.save()
else:
    p = Product()
    p.view()
    #p.save()