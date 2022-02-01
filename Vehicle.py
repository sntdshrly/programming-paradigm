class Vehicle:
    def __init__(self):
        self.__basePrice: int = 10000

    @property
    def basePrice(self) -> int:
        return self.__basePrice
    
    @basePrice.setter
    def basePrice(self, price) -> None:
        self.__basePrice = price