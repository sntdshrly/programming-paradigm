'''
sherly santiadi
2072025
ujian akhir semester paradigma pemrograman
'''

def kali(a, b):
    if b != 0:
        return a + kali(a, b-1)
    else:
        return 0

def pangkat(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * pangkat(a, b-1)

def pilih_fungsi(pilihan):
    if(pilihan == 1):
        return kali
    elif(pilihan == 2):
        return pangkat

def hitung(fungsi, a, b):
    if fungsi == kali:
        return kali(a,b)
    elif fungsi == pangkat:
        return pangkat(a,b)

def main():
    print(kali(7, 2))
    print(hitung(kali, 5, 3))
    print(hitung(pangkat, 5, 3))
    f = pilih_fungsi(1)
    print(f(7, 3))
    g = pilih_fungsi(2)
    print(g(5, 2))
    print(f(g(2,3), g(3,2)))


if __name__ == "__main__":
    main()