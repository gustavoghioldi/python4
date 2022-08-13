from models.document import Document
import datetime
class DocumentRepository:
    def __init__(self, document: Document) -> None:
        self.doc = document

    def create(self):
        now = datetime.datetime.now()
        str_now = now.strftime("%y%m%d%H%M%S")
        file_name = f'{str_now}_{self.doc.cuit}.txt'
        with open(file_name, 'w') as f:
            f.write(f"PEDIDO\n")
            f.write(f"======\n\n")
            f.write(f"cuit: {self.doc.cuit}\n")
            f.write(f"address: {self.doc.address}\n\n")
            f.write(f"Articulos:\n")
            f.write(f"=========\n\n")
            for i in self.doc.items:
                f.write(f'{i.q} - {i.art}\n')
