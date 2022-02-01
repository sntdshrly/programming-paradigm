'''
sherly santiadi
2072025
ujian akhir semester paradigma pemrograman
'''

import csv

class Person:
    def __init__(self, nama, umur, gender):
        self.nama = nama
        self.umur = umur
        self.gender = gender

def main():
    data = [Person("Josi", 28, "Male"), Person("Jefferson", 22, "Male"), Person(
        "Diana", 22, "Female"), Person("Maria", 32, "Female"), Person("Andreas", 42, "Male")]

    with open("data.csv", 'w', newline='') as source:
            writer = csv.writer(source)
            for item in data:
                writer.writerow([item.nama, item.umur, item.gender])

if __name__ == '__main__':
    main()
