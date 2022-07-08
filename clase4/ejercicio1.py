import sqlite3

class Product:
    def __init__(self, _id: int = None, name:str = None, price: float = None) -> None:
        self._id = _id 
        self.name = name
        self.price = price
        
        self.conn = sqlite3.connect("products.sqlite")
        self.__create_table()

    def save(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products VALUES (?, ?,?)", (self._id, self.name, self.price))
        self.conn.commit()

    def load(self, _id):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id, name, price FROM products WHERE id='{_id}'")
        self._id, self.name, self.price = cursor.fetchone()

    def __create_table(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("CREATE TABLE products (id NUMERIC, name TEXT, price NUMERIC)")
        except sqlite3.OperationalError:
            pass


###### implementacio de producto ########
#producto = Product(1, "Teclado", 25)
#producto.save()
product = Product()
product.load(1)
print(product.__dict__)
print(f"producto: id = {product._id}, nombre = {product.name}")
product2 = Product(2, "Mouse", 22)
print(f"producto: id = {product2._id}, nombre = {product2.name}")
product2.save()