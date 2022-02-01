from Spbu import Spbu
from Spklu import Spklu

def main():
    spbu1 = Spbu("pertalite",10)
    print(spbu1.mengisi())
    print("Pembayaran: "+str(spbu1.hitung_pembayaran()))

    spbu2 = Spbu("pertamax",20)
    print(spbu2.mengisi())
    print("Pembayaran: "+str(spbu2.hitung_pembayaran()))

    spklu1 = Spklu("normal",20)
    print(spklu1.mengisi())
    print("Pembayaran: "+str(spklu1.hitung_pembayaran()))

    spklu2 = Spklu("cepat",30)
    print(spklu2.mengisi())
    print("Pembayaran: "+str(spklu2.hitung_pembayaran()))

if __name__ == "__main__":
    main()
