from dolar_service import DolarService
from dolar_model import DolarModel
from dolar_repository import DolarRepository
from sqlite_connection import DBConnection

dw = DolarService.getQuotation()
dm = DolarModel(
    blue=dw['blue'],
    ccb=dw['ccb'],
    ccl=dw['ccl'],
    mep=dw['mep'],
    oficial=dw['oficial'],
    solidario=dw['solidario']
)

dr = DolarRepository()
dr.create(DBConnection(), dm)
