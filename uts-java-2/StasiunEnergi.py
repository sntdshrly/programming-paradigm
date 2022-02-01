from abc import ABC, abstractmethod

class StasiunEnergi(ABC):
    def mengisi(self) -> str:
        return "Melakukan pengisian..."

    @abstractmethod
    def hitung_pembayaran(self) -> float:
        pass
