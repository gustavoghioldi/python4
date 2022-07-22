from dolar_service import DolarService
from dolar_model import DolarModel
from dolar_repository import DolarRepository
from sqlite_connection import DBConnection


dr = DolarRepository()

for i in dr.read_all_quotations(DBConnection()):
    print(i.__dict__)
