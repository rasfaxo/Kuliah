# template layar masuk
def layar_masuk():
    print('SEPATU IDAMAN'.center(51))
    print("="*51)
    print(" Kode\t Merek\t\tJenis\t\tHarga")
    print("="*51)
    print("|  1  |\tAdidas  |\tCasual      |\t600.000   |")
    print("|     |\tAdidas  |\tRunning     |\t700.000   |")
    print("|  2  |\tReebok  |\tCasual      |\t700.000   |")
    print("|     |\tReebok  |\tRunning     |\t500.000   | ")
    print("|  3  |\t Nike   |\tCasual      |\t900.000   |")
    print("|     |\t Nike   |\tRuninng     |\t1.500.000 |")
    print("|  4  |\tArdiles |\tCasual      |\t200.000   |")
    print("|     |\tArdiles |\tRunning     |\t250.000   |")
    print("="*51)
    print("\n")


# variabel publik
merk_sepatu = []
kode_sepatu = []
jenis_sepatu = []
harga_sepatu = []
opsi = []
opsi_sepatu = []
jumlah_beli = []
jumlah = []

# mengambil inputan


def get_input():
    i = 0
    while i < get_jumlah:
        print('-'*20)
        print('   pesanan ke -', i+1)
        print('-'*20)
        kode_sepatu.append(
            int(input("Masukan kode sepatu yang ingin dibeli 1-4 : ")))
        if kode_sepatu[i] == 1:
            print('-'*20)
            print('ADIDAS'.center(20))
            print('-'*20)
            opsi_sepatu.append(input("Running atau Casual : "))
            if opsi_sepatu[i] == "running" or opsi_sepatu[i] == "Running":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Adidas")
                jenis_sepatu.append("Adidas Running")
                harga_sepatu.append("700.000")
                jumlah.append(jumlah_beli[i]*700000)
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Adidas")
                jenis_sepatu.append("Adidas Casual")
                harga_sepatu.append("600.000")
                jumlah.append(jumlah_beli[i]*600000)
            else:
                merk_sepatu.append('Merek sepatu tidak diketahui')
                jenis_sepatu.append('jenis sepatu tidak diketahui')
                harga_sepatu.append("0")
                jumlah.append(jumlah_beli[i]*0)
        elif kode_sepatu[i] == 2:
            print('-'*20)
            print('REEBOK'.center(20))
            print('-'*20)
            opsi_sepatu.append(input("Running atau Casual : "))
            if opsi_sepatu[i] == "Running" or opsi_sepatu[i] == "running":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Rebook")
                jenis_sepatu.append("Reebok Running")
                harga_sepatu.append("500.000")
                jumlah.append(jumlah_beli[i]*500000)
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Rebook")
                jenis_sepatu.append("Reebok Casual ")
                harga_sepatu.append("700.000")
                jumlah.append(jumlah_beli[i]*700000)
            else:
                merk_sepatu.append('Merek sepatu tidak diketahui')
                jenis_sepatu.append('jenis sepatu tidak diketahui')
                harga_sepatu.append("0")
                jumlah.append(jumlah_beli[i]*0)
        elif kode_sepatu[i] == 3:
            print('-'*20)
            print('NIKE'.center(20))
            print('-'*20)
            opsi_sepatu.append(input("Running atau Casual : "))
            if opsi_sepatu[i] == "Running" or opsi_sepatu[i] == "running":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Nike")
                jenis_sepatu.append("Nike Running")
                harga_sepatu.append("1.500.000")
                jumlah.append(jumlah_beli[i]*1500000)
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Nike")
                jenis_sepatu.append("Nike Casual")
                harga_sepatu.append("900.000")
                jumlah.append(jumlah_beli[i]*900000)
            else:
                merk_sepatu.append("merek sepatu tidak diketahui")
                jenis_sepatu.append("Jenis sepatu tidak diketahui")
                harga_sepatu.append("0")
                jumlah.append(jumlah_beli[i]*0)
        elif kode_sepatu[i] == 4:
            print('-'*20)
            print('ARDILES'.center(20))
            print('-'*20)
            opsi_sepatu.append(input("Running atau Casual : "))
            if opsi_sepatu[i] == "Running" or opsi_sepatu[i] == "running":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Ardiles")
                jenis_sepatu.append("Ardiles Running")
                harga_sepatu.append("250.000")
                jumlah.append(jumlah_beli[i]*250000)
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Ardiles")
                jenis_sepatu.append("Ardiles Casual")
                harga_sepatu.append("200.000")
                jumlah.append(jumlah_beli[i]*200000)
            else:
                merk_sepatu.append("merek sepatu tidak diketahui")
                jenis_sepatu.append("Jenis sepatu tidak diketahui")
                harga_sepatu.append("0")
                jumlah.append(jumlah_beli[i]*0)
        else:
            print('\n')
            print('-'*30)
            print(" Kode yang anda masukan salah")
            print('-'*30)
            continue
        i += 1
# tempalte layar keluar


def template_keluar():
    print('-'*79)
    print(' Kode\t merk\t\tjenis\t\tharga\t\tbanyak\t\tjumlah')
    print('sepatu\tsepatu\t\tsepatu\t\tsatuan\t\t beli\t\tharga')
    print('-'*79)
# proses bayar


def proses_bayar():
    j = 0
    while j < get_jumlah:
        print(
            f'  {kode_sepatu[j]}\t{merk_sepatu[j]}\t     {jenis_sepatu[j]}\t{harga_sepatu[j]}\t          {jumlah_beli[j]}\t        {jumlah[j]}')
        j += 1
    print('-'*79)
# menghitung jumlah bayar


def jumlah_bayar(jumlah):
    z = 0
    x = jumlah
    jumlah_bayar = len(x)
    for i in range(jumlah_bayar):
        y = x[i]
        z += y
    return z
# menghitung pajak


def pajak():
    pajak = jumlah_bayar(jumlah)*10/100
    return pajak
# menghitung total bayar


def total_bayar():
    total = pajak() + jumlah_bayar(jumlah)
    return total


# cetak
layar_masuk()
get_jumlah = int(input("Masukan jumlah sepatu yang ingin di beli : "))
get_input()
template_keluar()
proses_bayar()
print(f'\t\t\t\t\t\t\t Jumlah bayar : Rp. {jumlah_bayar(jumlah)}')
print(f'\t\t\t\t\t\t\t Pajak 10%    : Rp. {int(pajak())}')
print(f'\t\t\t\t\t\t\t Total bayar  : Rp. {int(total_bayar())}')
ubay = int(input("\t\t\t\t\t\t\t uang bayar   : Rp."))
kembali = ubay-total_bayar()
print(f'\t\t\t\t\t\t\t Uang kembali : Rp. {int(kembali)}')
