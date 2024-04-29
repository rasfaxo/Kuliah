
import os


def header():
    ''' Fungsi Header '''
    os.system('cls')
    print("{:^40}".format('Program Menyapa Seseorang'))
    print("{:^40}".format("="*40))


def sapa(nama):
    """Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter"""
    print("Hi, "+nama+", apa kabar ?")


def input_nama():
    """Fungsi ini untuk memasukkan nama"""
    nama = input("Masukkan nama: ")
    return nama


# Pemanggilan Fungsi
ulang = "y"
while ulang == "y" or ulang == "Y":
    header()
    nama = input_nama()
    sapa(nama)
    ulang = input("Input ulang [Y/N] : ")
    if ulang == "n" or ulang == "N":
        break
print("Program selesai, terima kasih")
