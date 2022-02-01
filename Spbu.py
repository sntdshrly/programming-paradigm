from StasiunEnergi import StasiunEnergi

class Spbu(StasiunEnergi):
    def __init__(self, jenis: str = "", jml: int = 0):
        self.jenis = jenis
        self.jml= jml
        self.satuan = "liter"
        self.harga_pertalite = 8000
        self.harga_pertamax = 10000

    def mengisi(self) -> str:
            return "Melakukan pengisian " + self.jenis + " sebanyak " \
                + str(self.jml) + " " + self.satuan

    def hitung_pembayaran(self) -> float:
        if self.jenis == "pertalite":
            return self.jml * self.harga_pertalite
        elif self.jenis == "pertamax":
            return self.jml * self.harga_pertamax
        else:
            return 0
