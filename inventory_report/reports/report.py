from abc import abstractmethod
from typing import Protocol
from inventory_report.inventory import Inventory


class Report(Protocol):
    @abstractmethod
    def add_inventory(self, inventory: Inventory) -> None:
        raise NotImplementedError

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError
