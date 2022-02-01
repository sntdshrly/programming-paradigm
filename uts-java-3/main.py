from typing import final


class SaturasiRendah(Exception):
    pass

class SaturasiTinggi(Exception):
    pass

def cek(saturasi: int):
    if (saturasi < 95):
        raise SaturasiRendah("Saturasi terlalu rendah!")
    elif(saturasi >= 95):
        raise SaturasiTinggi("Saturasi tinggi!")

def main():
    saturasi = int(input("Masukan saturasi darah anda: "))
    try:
        cek(saturasi)
    except SaturasiRendah as e:
        print("Warning! : " + str(e))
    except SaturasiTinggi as e:
        print(e)
    finally:
        print("pengecekan selesai!")

if __name__ == "__main__":
    main()
