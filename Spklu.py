from StasiunEnergi import StasiunEnergi

class Spklu(StasiunEnergi):
    def __init__(self, jenis: str = "", jml: int = 0):
        self.jenis = jenis
        self.jml = jml
        self.satuan = "KWh"
        self.harga_normal = 2000
        self.harga_cepat = 3000

    def mengisi(self) -> str:
            return "Melakukan pengisian " + self.jenis + " sebanyak " \
                + str(self.jml) + " " + self.satuan

    def hitung_pembayaran(self) -> float:
        if self.jenis == "normal":
            return self.jml * self.harga_normal
        elif self.jenis == "cepat":
            return self.jml * self.harga_cepat
        else:
            return 0