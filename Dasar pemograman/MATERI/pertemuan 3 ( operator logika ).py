#OPERATOR ARITMATIKA
a=int(input("masukan nilai a : "))
b=int(input("masukan nilai b : "))
print('\n');
print("nilai A :",a)
print("nilai B :",b)
print('\n');

print("A + B :",a+b)
print("A - B :",a-b)
print("A X B :",a*b)
print("A : B :",a/b)
print("A ** B :",a**b)
print("A // B :",a//b)
print("A % B :",a%b)
print('\n');

#OPERATOR PERBANDINGAN
x=5
y=3
print("nilai X :",x)
print("nilai Y :",y)
print('\n');
print("Hasil operator perbandingan")
print("===========================")
#menghasilkan TRUE karena 5 lebih besar dari 3
print(x,">",y," hasilnya",x>y)
#menghasilkan FALSE karena 5 lebih besar dari 3
print(x,"<",y," hasilnya",x<y)
#sama dengan
print(x,"==",y," hasilnya",x==y)
#tidak sama dengan
print(x,"!=",y," hasilnya",x!=y)
#lebih besar sama dengan
print(x,">=",y," hasilnya",x>=y)
#lebih kecil sama dengan
print(x,"<=",y," hasilnya",x<=y)
print('\n');

#ini artinya memberikan nilai 5 pada variabel x
x=5
print("x = 5 hasilya",x)
#ini artinya sama dengan x=x+3 (perjumlahan)
x=5
x+=3
print("x+=3 hasilnya",x)
#ini artinya sama dengan x=x-3 (pengurangan)
x=5
x-=3
print("x-=3 hasilnya",x)
#ini artinya sama dengan x=x*3
x=5
x*=3
print("x*=3 hasilnya",x)
#ini artinya x=x/3
x=5
x/=3
print("x/=3 hasilnya",x)
#ini artinya x=x**3
x=5
x**=3
print("x**=3 hasilnya",x)
#ini artiya x=x%3
x=5
x%=3
print("x%=3 hasilnya",x)
print('\n');

#OPERATOR LOGIKA

#input data
x=3
#cetak nilai
print("nilai X :",x)

#hasil operator logika
hasil= x<5 and x<10
print("x<5 and x<10 adalah :",hasil)
#menghasilkan TRUE karena 2 pernyataan menghasilkan nilai TRUE
hasil= x>5 or x<10
print("x>5 or x<10 adalah :",hasil)
#menghasilkan TRUE karena salah satu pernyataan menghasilkan nilai TRUE
hasil=not(x>5 or x<10)
print("not x>5 or x<10 adalah :",hasil)
print('\n');

#OPERATOR IDENTITAS

#buat list untuk isi objeknya
x=["pepaya","pisang"]
y=["pepaya","pisang"]
z=x
#hasil operator identitas
print("hasil x is z adalah :",x is z)
#menghasilkan TRUE karena objek z sama dengan x
print("hasil x is y adalah :",x is y)
#menghasilkan FALSE karena objek x tidak sama dengan y,meskipun isinya sama
print("hasil x is not y adalah :",x is not y)
#menghasilkan TRUE karena objeknya x tidak sama dengan y
print('\n');

#OPERATOR KEANGGOTAAN
x=["pepaya","pisang"]

#hasil operator keanggotaan
print("pisang"in x)
#menghasilkan TRUE karena pisang berada dalam list
print("anggur"not in x)
#menghasilkan TRUE karena anggur tidak berada dalam list
print('\n');

#OPERATOR BITWISE
x=10
y=12
print('x berisi angka',x,'desimal atau',bin(x),'biner')
print('y berisi angka',y,'desimal atau',bin(y),'biner')

#hasil operator bitwise
print('x & y :',x & y)
print('x | y :',x | y)
print('x ^ y :',x ^ y)
print('x << 1 :',x << 1)
print('x >> 1 :',x >> 1)

#PROGRAM TOKO MAINAN
print("TOKO MAINAN ANAK".center(40))
print("*"*40)
nama=input("Masukan nama pembeli : ")
kode=int(input("Masukan kode mainan : "))
harga=int(input("Masukan harga : "))
jumlah=int(input("Masukan jumlah beli : "))
total=harga*jumlah
print("="*60)
print("nama pembeli =",nama)
print("kode mainan  =",kode)
print("harga        =",harga)
print("jumlah beli  =",jumlah)
print("Total        =",total)


