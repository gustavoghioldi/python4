from dolar_service import DolarService
from sqlite_connection import DBConnection
from dolar_model import DolarModel

print(DolarService.getQuotation())

db_conn = DBConnection()
cursor = db_conn.get_cursor()
cursor.execute("CREATE TABLE if not exists quotation (oficial NUMBER, solidario NUMBER, blue NUMBER, ccb NUMBER, mep NUMBER, ccl NUMBER, time TEXT )")

#cursor.execute("INSERT INTO quotation VALUES (?, ?, ?, ? ,? , ?, ?)", (1, 2, 3, 4, 5, 6, "Date"))
db_conn.commit()
db_conn.destroy()

dm = DolarModel(1, 2, 3, 4, 5 ,6)
print(type(tuple(dm.get_list())))

