import sqlite3

conn = sqlite3.connect("database.sqlite3")

cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE personas (nombre TEXT, edad Numeric)")
except sqlite3.OperationalError:
    print("la tabla ya existe")

personas = (
    ("Juan", 44), 
    ("Pepe", 45)
    )

for n, e in personas:
    #repasar Unpackage
    cursor.execute("INSERT INTO personas VALUES (?, ?)", (n, e)) # este es el metodo seguro
    #cursor.execute(f"INSERT INTO personas VALUES ('{n}', {e})") # esto es inseguro en algunas versiones
    #"INSERT INTO personas VALUES {}, {}".format(n , e) <-- inseguro
conn.commit()
conn.close()