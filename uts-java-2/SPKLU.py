from StasiunEnergi import StasiunEnergi

class SPKLU(StasiunEnergi):
    def __init__(self, jenis: str, jml: int = 0):
        self.setjenis(jenis)# property agar jenis tidak aneh
        self.__jml: int = jml
        self.__satuan: str = "KWh"
        self.__harga_normal = 2000
        self.__harga_cepat = 3000

    def setjenis(self, jenis):
        if (jenis != "normal" and jenis != "cepat"):
            print("jenis tidak valid!")
        else:
            self.__jenis: str = jenis

    def mengisi(self) -> str:
        return self.__jenis + " " + str(self.__jml) + " " + self.__satuan
    
    def hitung_pembayaran(self) -> float:
        if (self.__jenis == "normal"):
            return self.__jml * self.__harga_normal
        else:
            return self.__jml * self.__harga_cepat
