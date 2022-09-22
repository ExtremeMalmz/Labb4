from product import Product

class Mic(Product):
    def __init__(self,productNumber: int,productName: str,productPrice: int,maxVolume: int, isMicBlack: bool) -> None:
        self.isMicBlack = isMicBlack 
        self.maxVolume = maxVolume
        super().__init__(productNumber, productName, productPrice)

    def __str__(self) -> str:
        return f"Product number: {self.productNumber} - Product name: {self.productName} - Product price: {self.price} - Max volume: {self.maxVolume} - Is the mic black: {self.isMicBlack} "