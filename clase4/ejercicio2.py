
from modulo_database import Product

##### implementacio de producto ########
#### CREATE ####
producto = Product("Teclado", 25)
producto.save()

#### READ ######
product = Product()
product.load(30)
print(product.__dict__)

#### UPDATE ####
product.name = "Prueba3"
product.update()

### DELETE ####
# product.delete()

print(product.viewAll())


