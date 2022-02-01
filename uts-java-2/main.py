from SPBU import SPBU
from SPKLU import SPKLU

def main():
    # spbu pertamax
    pertamax = SPBU("pertamax", 10)
    print(pertamax.mengisi())
    print(pertamax.hitung_pembayaran())

    # pertalite
    pertalite = SPBU("pertalite", 10)
    print(pertalite.mengisi())
    print(pertalite.hitung_pembayaran())

    # invalid
    invalid1 = SPBU("test", 10)
    invalid2 = SPKLU("test", 10)

    #spklu normal
    normal = SPKLU("normal", 10)
    print(normal.mengisi())
    print(normal.hitung_pembayaran())

    # cepat
    cepat = SPKLU("cepat", 10)
    print(cepat.mengisi())
    print(cepat.hitung_pembayaran())

if __name__ == "__main__":
    main()
