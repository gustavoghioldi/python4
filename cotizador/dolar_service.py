import requests

class DolarService:
    
    @staticmethod
    def  getQuotation():
        r = requests.get("https://criptoya.com/api/dolar")
        return r.json()