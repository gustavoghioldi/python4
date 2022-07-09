import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    #passwd=
    port=3306,
    db="test"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE if not exists products (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), price DECIMAL(6, 2))")

cursor.execute("INSERT INTO products VALUES (%s, %s, %s)", (None, "Mouse", 300))
conn.commit()
conn.close()