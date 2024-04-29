print('-'*30)
print('KALKULATOR MATEMATIKA'.center(30))
print('-'*30)


def persegi_panjang():
    panjang=int(input('masukan nilai panjang : '))
    lebar=int(input('masukan nilai lebar    : '))
    luas=panjang*lebar
    print('-'*30)
    print('nilai panjang         : ',panjang)
    print('nilai lebar           : ',lebar)
    print('luas persegi panjang  : ',luas)
    print('rumus persegi panjang : panjang x lebar')

def pertambahan():
    A=int(input('Masukan nilai A : '))
    B=int(input('Masukan nilai B :'))
    nilai=A+B
    print('Nilai hasil : ',nilai)
    print('-'*30)


opsi=input('pilih opsi kalkulator ( A/B ) : ')
if opsi =='a' or opsi=='A':
    persegi_panjang()
else:
    pertambahan()