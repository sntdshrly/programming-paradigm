from Vehicle import Vehicle
from Wheel import Wheel
from Car import Car

def main():
    c1 = Car()
    c1.setWheels([])
    print("c1 harga: "+str(c1.getPrice()))

    c2 = Car()
    w = Wheel()
    w.price = 500
    ws = [w]
    c2.setWheels(ws)
    print("c2 harga: "+str(c2.getPrice()))

    c3 = Car()
    w2 = Wheel()
    w2.price = 700
    ws = [w, w2]
    c3.setWheels(ws)
    print("c3 harga: "+str(c3.getPrice()))

    c4 = Car()
    w3 = Wheel()
    w3.price = 900
    ws = [w, w2, w3]
    c4.setWheels(ws)
    print("c4 harga: "+str(c4.getPrice()))

if __name__ == "__main__":
    main()