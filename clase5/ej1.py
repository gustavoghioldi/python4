import datetime
import requests
import sqlite3


response = requests.get("https://criptoya.com/api/dolar")
print(response.json())
print(datetime.datetime.now())

conn = sqlite3.connect('database.sqlite3')
cursor = conn.cursor()
cursor.execute("INSERT INTO cotizacion VALUES (?, ?)", (response.json()['ccb'], str(datetime.datetime.now())))
conn.commit()
conn.close()