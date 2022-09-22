#Eric Malmström IA-Labb 3
from product import Product
from dator import Dator
from kamera import Kamera
from mic import Mic

class Inventory():
    def __init__(self)-> None:
        '''
        constructor for Inventory class
        '''
        self.listOfProducts = []

    def addItemToInventory(self, productNumber:int, productName:str, price:int)-> None:
        '''
        adds item to listOfProducts
        '''
        
        #object skapas här
        storeProduct = Product(productNumber, productName, price)
        self.listOfProducts.append(storeProduct)

        '''
        product1 = Product(123,'Ericstation',100)
        self.listOfProducts.append(product1)

        product2 = Product(123,'asda',100)
        self.listOfProducts.append(product2)
        '''

    def addADator(self)-> None:
        productNumber = input("Vad är produktens nummer (int)")
        productName = input("Vad är produktens namn (str)")
        productPrice = input("Vad är produktens pris (int)")
        merInfo = input("Mer info (str): ")

        dator = Dator(productNumber,productName,productPrice,merInfo)
        self.listOfProducts.append(dator)

    def addAKamera(self)-> None:
        productNumber = input("Vad är produktens nummer (int)")
        productName = input("Vad är produktens namn (str)")
        productPrice = input("Vad är produktens pris (int)")
        lensInfo = input("lens info (str): ")
        previousOwner = input("Previous owner: ")

        kamera = Kamera(productNumber,productName,productPrice,lensInfo, previousOwner)
        self.listOfProducts.append(kamera)

    def addAMic(self)-> None:
        productNumber = input("Vad är produktens nummer (int)")
        productName = input("Vad är produktens namn (str)")
        productPrice = input("Vad är produktens pris (int)")
        maxVolume = input("Vad är max volym på mic-en (int)")
        isMicBlack = input("Är den svart (bool)") 

        mic = Mic(productNumber,productName,productPrice,maxVolume,isMicBlack)
        self.listOfProducts.append(mic)
        
    def __str__(self)-> str:
        return  '\n'.join(str(storeProduct) for storeProduct in self.listOfProducts)

