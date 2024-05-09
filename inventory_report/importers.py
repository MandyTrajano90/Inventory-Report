from typing import Dict, Type, List
from abc import ABC, abstractmethod
import json
from csv import DictReader
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def import_data(self) -> List[Product]:
        with open(self.file_path) as file:
            data = json.load(file)
            products = []
            for product in data:
                products.append(Product(**product))
            return products


class CsvImporter(Importer):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def import_data(self) -> List[Product]:
        with open(self.file_path) as file:
            data = DictReader(file)
            products = []
            for product in data:
                products.append(Product(**product))
            return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
