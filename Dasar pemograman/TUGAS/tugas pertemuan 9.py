import os


def header():
    ''' Fungsi Header '''
    os.system('cls')
    print("{:^40}".format('KALKULATOR'))
    print("{:^40}".format("="*40))


def pengurangan(a, b):
    jumlah = a - b
    return jumlah


def pejumlahan(a, b):
    return a+b


def perkalian(a, b):
    return a*b


def pembagian(a, b):
    return a/b


ulang = 'y'
while ulang == "y" or ulang == "Y":
    header()
    command = input("masukan perintah : ")
    a = int(input("masukan bilangan pertama : "))
    b = int(input("masukan bilangan kedua :"))
    if command == "-":
        print(f"hasil: {pengurangan(a, b)}")
    elif command == "+":
        print(f"hasil : {pejumlahan(a,b)}")
    elif command == "*":
        print(f"hasil : {perkalian(a,b)}")
    elif command == "/":
        print(f"hasil : {pembagian(a,b)}")
    else:
        print("input salah")
        continue
    ulang = input("input ulang [y/n] : ")
    if ulang == "n" or ulang == "N":
        break
