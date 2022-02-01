class Wheel:
    def __init__(self):
        self.__price: int = 1000

    @property
    def price(self) -> int:
        return self.__price
    
    @price.setter
    def price(self, price) -> None:
        self.__price = price
        