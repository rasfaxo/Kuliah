# linear search
def linear_search(data, cari):
    posisi = []

    for i in range(len(data)):
        if cari == data[i]:
            posisi.append(i+1)
    if len(posisi) > 0:
        print('data', cari, 'sebanyak', len(posisi),
              'ditemukan di posisi: ', posisi)
    else:
        print('data tidak ditemukan')


data = [1, 4, 5, 6, 8, 4, 9]
print('Data : ', data)
cari = int(input('Data yang ingin dicari : '))
linear_search(data, cari)

# binary search


def binary_search(data, cari):
    L = 0
    H = len(data)-1
    ketemu = False
    while L <= H and not ketemu:
        mid = int((L+H)/2)
        if cari == data[mid]:
            ketemu = True
            print('Data', cari, 'ditemukan di posisi', mid)
        elif cari < data[mid]:
            H = mid-1
        else:
            L = mid+1
    if not ketemu:
        print('Data tidak ditemukan')


data = [1, 2, 4, 7, 10, 14, 23, 35, 47]
print(f'Data : {data}')
cari = int(input('Data yang ingin dicari : '))
binary_search(data, cari)

# max min search


def straitmaxmin(a, n):
    max = min = a[0]
    p = 0
    for i in range(1, n):
        p = p+1
        print('Proses ke: ', p)
        if a[i] > max:
            max = a[i]
        else:
            p = p+1
            print('Proses ke: ', p)
            if a[i] < min:
                min = a[i]
    print('='*12)
    print(f'Max=', {max}, 'Min=', {min})


x = [3, 6, 9, 12]
straitmaxmin(x, 4)
