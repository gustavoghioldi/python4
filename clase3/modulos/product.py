class DecimalPriceExec(Exception):
    pass

class Product:
    def __init__(self, name=None, price=0) -> None:
        try:
            float(price)
        except ValueError:
            raise DecimalPriceExec    
        self.__name = name
        self.__price = price

    def save(self):
        if self.__name == None:
            raise Exception("NO se puede grabar ")
        with open("productos.txt", "a") as f:
            f.write(f"{self.__name} -- {self.__price}\n")

    def view(self):
        with open("productos.txt") as f:
            print(f.read())

    