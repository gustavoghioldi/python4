import sqlite3

conn = sqlite3.connect("database.sqlite3")

cursor = conn.cursor()

cursor.execute("SELECT * FROM personas") # * trae todo
personas = cursor.fetchall()
print(personas)

cursor.execute("SELECT nombre FROM personas") # trae solo nombres
nom = cursor.fetchall()
print(nom)

cursor.execute("SELECT nombre FROM personas WHERE edad=45") # trae solo personas con edad de 45 
nom = cursor.fetchall()
print(nom)
print("--- *** --- ")
nom = cursor.fetchall()
print(nom)

cursor.execute("SELECT * FROM personas") # * trae todo
persona = cursor.fetchone() # vacia y retorn la primera posicion del cursor
print(persona)
persona = cursor.fetchone()
print(persona)
personas = cursor.fetchall()
print(personas)

conn.close()