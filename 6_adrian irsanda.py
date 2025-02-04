import os
import platform
from tabulate import tabulate

def clear_terminal():

    system = platform.system().lower()

    if system == 'windows':
        os.system('cls')

    else:
        os.system('clear')

clear_terminal()

# aa, bb, cc, dd, ee
# ff, gg, hh, jj, kk

# soal 1.
# film_saya = (input('masukkan 5 film kesukaan anda: ')).split(', ')

# film_teman = (input('masukkan 5 film kesukaan teman anda: ')).split(', ')

# film_saya_1 =  film_saya.split(',')
# film_teman_1 = film_teman.split(',')
# print(film_saya)
# print(film_teman)

# x = set(film_saya)
# y = set(film_teman)

# print((film_saya, x))
# print((film_teman, y))

# movie = x.intersection(y)
# kesukaan = (len(movie)) / (len(film_saya)) * 100
# print(f'kesukaan film kalian yang sama sebesar {kesukaan}%')

# soal 2.

welcome = print('selamat datang di pasar buah')
print()
tampilkan_menu = print('list menu \n 1. menampilkan data buah \n 2. menambahkan buah \n 3. menghapus buah \n 4. membeli buah \n 5. exit program')
print()
angka = int(input(f'masukkan angka menu yang ingin dijalankan: '))
print()

data = [['Nama', 'Stock', 'Harga'], ['Apel', 20, 10000], ['Jeruk', 15, 15000], ['Anggur', 25, 20000]]

keranjang_belanja = []

while angka in range(1,6):
    if angka == 1:
        print(tabulate(data, headers = 'firstrow', showindex = 'always'))
        print()
        tampilkan_menu = print('list menu \n 1. menampilkan data buah \n 2. mmenambahkan buah \n 3. menghapus buah \n 4. membeli buah \n 5. exit program')
        print()
        angka = int(input(f'masukkan angka menu yang ingin dijalankan: '))
    elif angka == 2:
        input_nama_buah = input(f'masukkan nama buah yang ingin ditambahkan: ')
        input_stok_buah = int(input(f'masukkan stok buah yang ingin ditambahkan: '))
        input_harga_buah = int(input(f'masukkan harga buah yang ingin ditambahkan: '))
        print()
        tambah_buah = [input_nama_buah, input_stok_buah, input_harga_buah]
        data.append(tambah_buah)
        print(tabulate(data, headers = 'firstrow', showindex = 'always'))
        print()
        tampilkan_menu = print('list menu \n 1. menampilkan data buah \n 2. menambahkan buah \n 3. menghapus buah \n 4. membeli buah \n 5. exit program')
        print()
        angka = int(input(f'masukkan angka menu yang ingin dijalankan: '))
    elif angka == 3:
        print()
        print(tabulate(data, headers = 'firstrow', showindex = 'always'))
        print()
        input_hapus_index_buah = int(input(f'masukkan index buah yang ingin dihapus: '))
        for i in range(len(data) - 1): 
                if i == input_hapus_index_buah:
                     del data[i + 1]
        print(tabulate(data, headers = 'firstrow', showindex = 'always'))
        print()
        angka = int(input(f'masukkan angka menu yang ingin dijalankan: '))
    elif angka == 4:
        print()
        print(tabulate(data, headers = 'firstrow', showindex = 'always'))
        print()
        input_beli_index_buah = int(input(f'masukkan index buah yang ingin dibeli: '))
        for x, y in enumerate(data):
            if x > 0:
                c = y[input_beli_index_buah + 1][0]
                break
        input_beli_jumlah_buah = int(input(f'masukkan jumlah buah yang ingin dibeli: '))
        if input_beli_jumlah_buah > data[input_beli_index_buah+1][1]:
            print(f'stok kurang, sisa {data[input_beli_index_buah+1][1]}')
        # elif input_beli_jumlah_buah <= data[input_beli_index_buah+1][1]:
        #     keranjang_belanja.append()
        else:
            x = input('mau beli yang lain? (ya/tidak): ').lower()
            if x == 'tidak':
                total_harga = input_beli_jumlah_buah * data[input_beli_index_buah+1][2]
                print(f'total harga: {total_harga}')
                uang_bayar = int(input("Masukkan jumlah uang: "))
                while uang_bayar == total_harga:
                    print('terimakasih')
                    break
                while uang_bayar < total_harga:
                    print(f'transaksi dibatalkan,uang kurang {total_harga-uang_bayar}')
                    uang_bayar = int(input("Masukkan jumlah uang: "))
                while uang_bayar > total_harga:
                    print(f'terima kasih, uang kembalian anda {uang_bayar-total_harga}')
                    break
            else:
                pass
    elif angka == 5:
        print('exit program')
        break
else:
    print()
    print('input tidak sesuai, silahkan input sesuai menu')
    print()
    print('list menu \n 1. menampilkan data buah \n 2. menambahkan buah \n 3. menghapus buah \n 4. membeli buah \n 5. exit program')
    print()
    angka = int(input(f'masukkan angka menu yang ingin dijalankan: '))