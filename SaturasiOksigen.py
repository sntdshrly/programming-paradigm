class SaturasiRendah(Exception):
    pass

class SaturasiTinggi(Exception):
    pass

class SaturasiOksigen:
    def test_saturasi(self, saturasi: int) -> None:
        if (saturasi < 95):
            raise SaturasiRendah("saturasi rendah: " + str(saturasi))
        else:
            raise SaturasiTinggi("saturasi rendah: " + str(saturasi))

def main():
    so = SaturasiOksigen()
    list_saturasi = [85, 97, 93, 98]
    print("Menguji saturasi Oksigen dalam darah: " + str(list_saturasi))

    for c in list_saturasi:
        try:
            so.test_saturasi(c)
        except SaturasiRendah as ex:
            print("Exception: "+ ex.__str__())
        except SaturasiTinggi as ex:
            print("Exception: "+ ex.__str__())

if __name__ == "__main__":
    main()
