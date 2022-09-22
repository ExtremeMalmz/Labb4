from product import Product

class Dator(Product):
    def __init__(self,productNumber: int,productName: str,productPrice: int,merInfo: str) -> None:
        self.merInfo = merInfo
        super().__init__(productNumber, productName, productPrice)

    def __str__(self) -> str:
        return f"Product number: {self.productNumber} - Product name: {self.productName} - Product price: {self.price} - Mer Info: {self.merInfo} "