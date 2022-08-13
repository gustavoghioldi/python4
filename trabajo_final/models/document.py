class Document:
    def __init__(self, cuit: int, address:str, items: list):
        self.cuit = cuit
        self.address = address
        self.items = items