#Perulangan for disebut counted loop (perulangan yang terhitung),
#perulangan while disebut uncounted loop (perulangan yang tak terhitung)

#perulangan for
ulang= 5
for i in range(ulang) :
    print(f"ulang ke-{i}")

print("=======================================")

nasi=('pecel ayam','nasi uduk','pecel lele')
for isi in nasi:
    print(isi)

#perulangan while

jawab='ya'
hitung=1
while(jawab== 'ya'):
    hitung+= 1
    jawab=input("ulang lagi tidak ?")
print(f"total perulangan{hitung}")


jawab='ya'
hitung=1
while(True):
    hitung+=1
    jawab=input("ulang lagi tidak ? ")
    if jawab == "tidak":
        break



#perulangan for dengan list
number=[1,2,3,4,5,6,7,8,9,0]
nomer=0
for nomer in number:
    nomer+=nomer
print("jumlah :",nomer)

#mengetahui urutan iterasi for dengan list
listkota=['jakarta','depok','citayam','margonda']
for i, kota in enumerate(listkota):
    print(i, kota)

#perulangan for dengan range
for i in range(5):
    print("saya suka",i)

#for dengan break dan continue
for i in (10, 20):
    if i==15:
        continue
    print(i)

#for dengan else
listkota=['jakarta','depok','citayam','margonda']
for kora in listkota:
    print(kota)
else:
    print("tidak ada nama kota")

#for dengan else break
listkota=['jakarta','depok','citayam','margonda']
kota_yang_dicari=input("masukan kota yang dicari : ")

for i, kota in listkota:
#ubah katanya menjadi lowercase agar menjadi insensitive
    if kota.lower() == listkota.lower():
        print("kota yang anda cari berada pada indeks",i)
        break
    else:
        print("kota yang anda cari tidak ada dalam list")


#perulangan while dengan list
listkota=['jakarta','depok','citayam','margonda']
i=0
while i<len(listkota):
    print(listkota[i])
    i+=1

#while dengan inputan
a=int(input("masukan bilangan ganjil lebih dari 50 : "))
while a % 2 !=1 or a<=50:
    a=int(input("salah,masukan lagi : "))
print("benar")

#while dengan continue
listkota=['jakarta','depok','citayam','margonda']
i=-1
while i < len(listkota):
    i+=1
    if i % 2 == 0 or i > 0:
        print("skip")
        continue
print(listkota[i])

#while dengan break
listkota=['jakarta','depok','citayam','margonda']
kota_yang_dicari=input("masukan kota yang dicari : ")
i=0
while i < len(listkota):
    if listkota[i].lower()==kota_yang_dicari.lower():
        print(print("kota yang dicari pada index",i))
        break
    print("bukan",listkota[i])
    i+=1

#while dengan else
listkota=['jakarta','depok','citayam','margonda']
kota_yang_dicari=input("masukan kota yang dicari : ")
i=0
while i < len(listkota):
    if listkota[i].lower()==kota_yang_dicari.lower():
        print(print("kota yang dicari pada index",i))
        break
    print("bukan",listkota[i])
    i+=1
else:
    print("maaf kota yang anda cari tidak ada dalam list")


#membuat program lagu anak ayam
a =int(input("masukan angka : ")) 
print("tek kotek kotek kotek, anak ayam turun berkotek")
if a>=2:
    while a>1:
        print(f"anak ayam turunlah {a} mati 1 tinggallah", a-1)
        a-=1
if a<=1:
    print(f"anak ayam turun {a} mati 1 tinggal induknya")

#membuat program gambar segitiga
n=int(input("masukan angka : "))

for i in range(0, n):
    for j in range(0, n):
        print(' ', end='')
    n-=1
    for a in range(0, i+1):
        print('*', end=' ')
    print('\r')

print('\n')

n=int(input("masukan angka : "))

for i in range(0, n):
    for j in range(0, n):
        print(' ', end='')
    n-=1
    for a in range(0, i+1):
        print('$', end=' ')
    print('\r')
    