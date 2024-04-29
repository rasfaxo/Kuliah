print("-"*30)
print("PENJUALAN TIKET BUS XYZ".center(30))
print("-"*30)
nama=input("Nama pembeli          : ")
nohp=int(input("No. handphone         : "))
jurusan=input("Jurusan [SBY/BL/LMP]  : ")
jumlah_beli=int(input("Jumlah beli           : "))
if jurusan=="SBY" or jurusan=="sby":
    nama_kota="Surabaya"
    harga=300000
elif jurusan=="BL" or jurusan=="bl":
    nama_kota="Bali"
    harga=350000
else:
    nama_kota="Lampung"
    harga=500000

if jumlah_beli >=3:
    potongan=(jumlah_beli*harga)*0.1
else:
    potongan=0
total_harga=(jumlah_beli*harga)-potongan
print("nama kota jurusan     :",nama_kota)
print("harga                 :",harga)
print("-"*30)
print("Potongan yang didapat :",potongan)
print("Total bayar           :",total_harga)
ubay=int(input("masukan uang bayar    : "))
total=ubay-total_harga
print("Kembalian             :",total)
    

print('\n')

nis=int(input("Nis mahasiswa : "))
nama=input("Nama mahasiswa : ")
jurusan=input("Jurusan [SI/SIA] : ")

if jurusan == "SI" or jurusan == "si":
    nama_jurusan="Sistem informasi"
    harga=2400000
elif jurusan == "SIA" or jurusan == "sia":
    nama_jurusan="Sistem informasi akutansi"
    harga=2000000
else:
    print("anda salah memasukan kode")
    harga=0
print("----------------------------------------------------")
print("         PENDAFTARAN MAHASISWA BARU")
print("----------------------------------------------------")
print("Nis Mahasiwa              :",nis)
print("Nama Mahasiswa            :",nama)
print("kode jurusan yang dipilih :",jurusan)
print("Nama program studi        :",nama_jurusan)
print("Harga                     :",harga)

print('\n')

#nested if
kode_baju=input("Masukan kode baju [SP/AD] : ")
ukuran=input("Masukan ukuran baju [S/M] : ")
if kode_baju=="SP" or kode_baju=="sp":
    merk="SuperDry"
    if ukuran=="S" or ukuran=="s":
        jenis="Small"
        harga=450000
    elif ukuran=="M" or ukuran=="m":
        jenis="Medium"
        harga=500000
    else:
        jenis="anda salah memasukan kode"
        harga=0
        
elif kode_baju=="AD" or kode_baju=="ad":
    merk="adidas"
    if ukuran=="S" or ukuran=="s":
        jenis="Small"
        harga=500000
    elif ukuran=="M" or ukuran=="m":
        jenis="Medium"
        harga=550000
    else:
        jenis="anda salah memasukan kode"
        harga=0
        
else:
    merk="anda salah memasukan kode"
    harga=0
    

print("-"*40)
print("merk baju  :",merk)
print("harga baju :",harga)