NIM=int(input("Masukan NIM : "))
nama=input("Masukan nama mahasiswa : ")
matkul=input("Mata kuliah : ")
nilai_absensi=int(input("Masukan nilai absensi : "))
nilai_tugas=int(input("Masukan nilai tugas : "))
nilai_uts=int(input("Masukan nilai uts : "))
nilai_uas=int(input("Masukan nilai uas : "))

nilai_absensi*=(20/100)
nilai_tugas*=(25/100)
nilai_uts*=(25/100)
nilai_uas*=(30/100)
nilai_akhir=nilai_absensi+nilai_tugas+nilai_uas+nilai_uts
print("\a")
print("------------------------------")
print("\t PROGRAM NILAI")
print("------------------------------")
print('\a')
print("NIM Mahasiswa  :",NIM)
print("Nama Mahasiswa :",nama)
print("Mata kuliah    :",matkul)


if nilai_akhir >81:
    print(f"Nilai Akhir    : {nilai_akhir} Anda lulus dengan Grade A")
elif nilai_akhir >75:
    print(f"Nilai Akhir    : {nilai_akhir} Anda lulus dengan Grade B")
elif nilai_akhir >60:
    print(f"Nilai Akhir    : {nilai_akhir} Anda lulus dengan Grade C")
elif nilai_akhir >41:
    print(f"Nilai Akhir    : {nilai_akhir} Anda Tidak lulus dengan Grade D")
else:
    print(f"Nilai Akhir    : {nilai_akhir} Anda Tidak lulus dengan Grade E")

