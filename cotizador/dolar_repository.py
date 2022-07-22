import datetime
from dolar_model import DolarModel
from sqlite_connection import DBConnection
class DolarRepository:
    
    @staticmethod
    def create(db_conn: DBConnection, dolar_model: DolarModel):
        cursor = db_conn.get_cursor()
        dolar_list = dolar_model.get_list()
        dolar_tuple = tuple(dolar_list)
        cursor.execute("INSERT INTO quotation VALUES (?,?,?,?,?,?,?)", dolar_tuple)
        db_conn.commit()
        db_conn.destroy()
    
    @staticmethod
    def read_all_quotations(db_conn:DBConnection)->list:
        cursor = db_conn.get_cursor()
        cursor.execute("SELECT * FROM quotation")
        all = cursor.fetchall()
        all_list = []
        for i in all:
            dm = DolarModel(
                    i[0],
                    i[1],
                    i[2],
                    i[3],
                    i[4],
                    i[5],
                    
                )
            dm.set_time(i[6])    
            all_list.append(
                dm
            ) 
        return all_list

    @staticmethod
    def read_one_quotation(db_conn:DBConnection)->list:
        pass