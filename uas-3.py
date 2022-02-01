'''
sherly santiadi
2072025
ujian akhir semester paradigma pemrograman
'''

def list_rekursif(angka):
    if(angka != -1):
        if(check(angka)):
            print(angka + 2, end=" ")
        else:
            print(angka * 2, end=" ")
        return list_rekursif(angka-1)


def check(angka):
    return (angka % 2 == 0 and angka != 0)


def main():
    list_rekursif(11)
    print()
    list_rekursif(10)

if __name__ == "__main__":
    main()