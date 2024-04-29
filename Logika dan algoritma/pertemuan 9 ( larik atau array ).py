# array dimensi satu
nilai_tugas = ([60, 70, 80, 90])
print(f"nilai tugas :\n {nilai_tugas} ")
#output : [60, 70, 80, 90]
print(nilai_tugas[0])
print(nilai_tugas[1])
print(nilai_tugas[2])
print(nilai_tugas[3])
# output : 60,70,80,90
print("===============================")
nilai_tugas = [10, 20, 30, 40]
print(nilai_tugas[-3])
#output : 20
print("================================")

nilai_tugas = [10, 20, 30, 40]
print("nilai elemen ke 2 dan 3:", nilai_tugas[1:3])
# output : 20,30
print("===================================")

nilai_tugas = [10, 20, 30, 40]
print(nilai_tugas[0:])
#output : [10,20,30,40]
print("=====================================")

nilai_tugas = [10, 20, 30, 40]
print(nilai_tugas[len(nilai_tugas)-3:])
# output : 20,30,40
print("======================================")
nilai_tugas = ([60, 70, 80, 90])
for i in nilai_tugas:
    print(i, end=" ")

# mengubah elemen
nilai_tugas = [60, 70, 80, 90]
nilai_tugas[0] = 65
print(nilai_tugas)
# output : 65,70,80,90

# array berdimensi dua
list = [["teknik", "kedokteran", "MIPA"], [1, 2, 3]]
print(list)
print("======================================")

arr = [["teknik", "kedokteran", "MIPA"], [1, 2, 3]]
print(arr)
print("elemen pada baris ke 1: ", arr[0][0:])
print("elemen pada baris ke 2: ", arr[1][0:])
print("="*45)

# deklarasi
penjualan = [[90, 100, 30, 45], [45, 27, 60],
             [20, 110, 45, 30], [98, 95, 75, 40]]
# isi
for i in penjualan:
    for j in i:
        print(j, end=" ")
print()
print("="*45)
