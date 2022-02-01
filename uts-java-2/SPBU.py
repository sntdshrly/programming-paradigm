from StasiunEnergi import StasiunEnergi

class SPBU(StasiunEnergi):
    def __init__(self, jenis: str, jml: int = 0):
        self.setjenis(jenis)  # property agar jenis tidak aneh
        self.__jml: int = jml
        self.__satuan: str = "liter"
        self.__harga_pertalite = 8000
        self.__harga_pertamax = 10000

    def setjenis(self, jenis: str):
        if (jenis != "pertalite" and jenis != "pertamax"):
            print("jenis tidak valid!")
        else:
            self.__jenis: str = jenis

    def mengisi(self) -> str:
        return self.__jenis + " " + str(self.__jml) + " " + self.__satuan

    def hitung_pembayaran(self) -> float:
        if self.__jenis == "pertalite":
            return self.__jml * self.__harga_pertalite
        else:
            return self.__jml * self.__harga_pertamax
