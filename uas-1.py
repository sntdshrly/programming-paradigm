'''
sherly santiadi
2072025
ujian akhir semester paradigma pemrograman
'''

def add(n1,n2):
    return n1 + n2
 
def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2 

def main():
    n1 = int(input("nilai 1: "))
    n2 = int(input("nilai 2: "))
    operasi = str(input("operasi (+, -, *, /): "))
    if operasi == "+":
        print("hasil: ", add(n1, n2))
    elif operasi == "-":
        print("hasil: ", sub(n1, n2))
    if operasi == "*":
        print("hasil: ", multiply(n1, n2))
    if operasi == "/":
        print("hasil: ", divide(n1, n2))

if __name__ == "__main__":
    main()