import sqlite3

class DBConnection:
    def __init__(self) -> None:
        self.__conn = sqlite3.connect("database.sqlite3")

    def get_cursor(self):
        return self.__conn.cursor()

    def commit(self):
        self.__conn.commit()
        
    def destroy(self):
        self.__conn.close()