from product import Product

class Kamera(Product):
    def __init__(self,productNumber: int,productName: str,productPrice: int,lensInfo: str, previousOwner: str)-> None:
        self.lensInfo = lensInfo
        self.previousOwner = previousOwner
        super().__init__(productNumber, productName, productPrice)

    def __str__(self) -> str:
        return f"Product number: {self.productNumber} - Product name: {self.productName} - Product price: {self.price} - Lens Info: {self.lensInfo} - Previous Owner: {self.previousOwner} "