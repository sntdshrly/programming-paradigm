from Vehicle import Vehicle
from Wheel import Wheel

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.__wheels = []
    
    def getPrice(self) -> int:
        wheel_price = 0
        for p in self.__wheels:
            wheel_price = wheel_price + p.price
        return super().basePrice + wheel_price
    
    def setWheels(self, wheels):
        # Kalau jumlah objek roda >= 3 maka wheels tidak perlu ditambahkan apa-apa
        if len(wheels) >= 3:
            self.__wheels = wheels
        
        # Kalau jumlah objek roda = 0 maka wheels akan ditambahkan sebanyak 4 wheel
        elif len(wheels) == 0:
            for c in range(4):
                w = Wheel() # sudah rp.1000
                self.__wheels.append(w)

        # Kalau jumlah objek roda = 1 maka wheels akan ditambahkan sebanyak 2 wheel
        elif len(wheels) == 1:
            self.__wheels = wheels # untuk meng-append yang diinput user
            for c in range(2):
                w = Wheel()
                w.price = wheels[0].price #karna cuman 1 buah roda jadi tidak cari rata-rata
                self.__wheels.append(w)

        # Kalau jumlah objek roda = 2 maka wheels akan ditambahkan sebanyak 1 wheel
        elif len(wheels) == 2:
            self.__wheels = wheels # untuk meng-append yang diinput user
            w = Wheel()
            w.price = (wheels[0].price + wheels[1].price)/2 #rata-rata wheels keduanya
            self.__wheels.append(w)