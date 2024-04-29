data=[[1,2,3], [4,5,6], [7,8,9], [0]]
print("baris pertama, kolom pertama adalah :",data[0][0],'\nbaris pertama, kolom kedua adalah   :',data[0][1])
print("baris pertama, kolom ketiga adalah  :",data[0][2],'\nbaris ketiga, kolom ketiga adalah   :',data[2][-1])
print("baris pertama, kolom ketiga adalah  :",data[3][-0])

#mengambil inputan
banyak_input=int(input("banyak input yang diinginkan : "))
#variable publik
nim=[]
nilai_uts=[]
nilai_uas=[]
total=[]
average=[]
#proses
i=0
while i < banyak_input:
    print('\n')
    print("\tdata ke-",i+1)
    print('-'*30)
    nim.append(int(input("masukan nim anda  : ")))
    nilai_uts.append(int(input("masukan Nilai UTS : ")))
    nilai_uas.append(int(input("masukan Nilai UAS : ")))
    i+=1
for i in range((banyak_input)):
    total.append((nilai_uas[i]+nilai_uts[i]))
    average.append((total[i] /2))

#cetak layar output
print('='*50)
print("   NIM\t    Nilai UTS\tNilai UAS\tTotal")
print('='*50)
for i in range (banyak_input):
    print('%i\t%i\t  %i\t\t%i   '% (nim[i],nilai_uts[i],nilai_uas[i],total[i]))
print('='*50)
print("                                rata=rata :",average[i])



alfabet = ['a','b','d','f','e','c','h','g','j','i']
#mengurutkan anggota list
alfabet.sort()
print(alfabet)
#mengurutkan anggota list dari belakang
alfabet.sort(reverse=True)
print(alfabet)
#menghapus anggota list
alfabet.remove('a')
print(alfabet)
#membalikan nilai list yang sudah dihapus
print(alfabet.pop(0))
#menghapus list yang diinginkan
del alfabet[2]
print(alfabet)
#menghapus semua anggota list
alfabet.clear()
print(alfabet)


my_tuple=(2,3,4,'a','b','c')
print('a' in my_tuple)

print('k' not in my_tuple)

list=[[1,2,3],[4,5,6],[7,8,9],[0]]
print("baris pertama, kolom pertama :"[0][0])
print()