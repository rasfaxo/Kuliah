nama=input("Masukan nama : ")
no_hp=int(input("masukan No handphone : "))
jurusan=input("masukan jurusan (SBY/BL/LMP) : ")
jumlah_beli=int(input("masukan jumlah beli : "))

if jurusan == "SBY" :
    nama_jurusan="Surabaya"
    harga=300000
elif jurusan == "BL" :
    nama_jurusan="Bali"
    harga=350000
else:
    nama_jurusan="Lampung"
    harga=500000

if jumlah_beli >=3 :
    diskon=(jumlah_beli*harga)*0.1
else:
    diskon=0

total=(jumlah_beli*harga)-diskon
print("--------------------------------")
print("   PENJUALAN TIKET BUS XYZ ")
print("--------------------------------")
print("nama pembeli  : ",nama)
print("No.handphone  :",no_hp)
print("kode jurusan yang dipilih :",jurusan)
print("Nama kota jurusan :",nama_jurusan)
print("Harga         :",harga)
print("Jumlah beli   :",jumlah_beli)
print("--------------------------------")
print("Potongan yang didapat : "
,diskon)
print("Total bayar           :",total)
ubay=int(input("Masukan uang bayar : "))
total_harga=ubay-total
print("kembalian anda : ",total_harga)
