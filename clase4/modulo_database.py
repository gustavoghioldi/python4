import sqlite3
import pymysql

class Product:
    def __init__(self, name:str = None, price: float = None) -> None:
        self._id = None
        self.name = name
        self.price = price
        
        self.conn =conn = pymysql.connect(
            host="localhost",
            user="root",
            #passwd=
            port=3306,
            db="test"
            )
        self.__create_table()

    def save(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products VALUES (%s,%s,%s)", (self._id, self.name, self.price))
        self.conn.commit()

    def load(self, _id):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id, name, price FROM products WHERE id='{_id}'")
        product = cursor.fetchone()
        if product:
            self._id, self.name, self.price = product
        else:
            raise Exception(f"No existe producto con id_ = {_id}")

    def viewAll(self)->tuple:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id, name, price FROM products")
        return cursor.fetchall()

    def update(self):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE products SET name=%s, price=%s WHERE id=%s", (self.name, self.price, self._id) )
        self.conn.commit()

    def delete(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=%s", (self._id))
        self.conn.commit()

    def __create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE if not exists products (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), price DECIMAL(6, 2))")

        

