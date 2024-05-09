from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="1",
        product_name="Borracha",
        company_name="Papelaria Solar",
        manufacturing_date="2021-07-04",
        expiration_date="2029-02-09",
        serial_number="FR48",
        storage_instructions="Ao abrigo de luz solar"
    )
    assert product.__str__() == (
        f"The product {product.id} - {product.product_name} with serial number {product.serial_number} manufactured on {product.manufacturing_date} by the company {product.company_name} valid until {product.expiration_date} must be stored according to the following instructions: {product.storage_instructions}."
    )
