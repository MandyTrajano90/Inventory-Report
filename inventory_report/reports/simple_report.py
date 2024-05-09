from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self):
        self.inventory_list = []

    def add_inventory(self, inventory: Inventory):
        self.inventory_list.append(inventory)

    def _get_manufacturing_date(self) -> str:
        return min(
            product.manufacturing_date for inventory in self.inventory_list
            for product in inventory.data
            )

    def _get_expiration_date(self) -> str:
        return min(
            product.expiration_date for inventory in self.inventory_list
            for product in inventory.data
            )

    def _get_biggest_company(self) -> str:
        companies = [
            product.company_name for inventory in self.inventory_list
            for product in inventory.data]
        return max(companies, key=companies.count)

    def generate(self) -> str:
        if not self.inventory_list:
            return "Inventory is empty"

        oldest_manufact = self._get_manufacturing_date()
        biggest_company = self._get_biggest_company()
        expiration_date = self._get_expiration_date()

        result = (
            f"Oldest manufacturing date: {oldest_manufact}\n"
            f"Closest expiration date: {expiration_date}\n"
            f"Company with the largest inventory: {biggest_company}\n"
        )

        return result
