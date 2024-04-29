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
    