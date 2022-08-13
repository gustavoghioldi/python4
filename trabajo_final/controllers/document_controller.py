from models.item import Item
from models.document import Document
from repositories.document_repository import DocumentRepository
class DocumentController:
    @staticmethod
    def print_document(address: str, cuit:int, items: list):
        doc = Document(cuit, address, items)
        repo = DocumentRepository(doc)
        repo.create()