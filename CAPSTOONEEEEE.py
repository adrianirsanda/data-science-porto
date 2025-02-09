import os
import platform

def clear_terminal():

    system = platform.system().lower()

    if system == 'windows':
        os.system('cls')

    else:
        os.system('clear')

clear_terminal()

from tabulate import tabulate

ikan = {
    'Nama' : ['Oscar', 'Peacock Bass', 'Arwana Jardini', 'Payara', 'Vittatus', 'Goliath', 'Golden Dorado'], 
    'Ukuran' : [5, 5, 5, 5, 5, 5, 5], 
    'Origin' : ['Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta', 'Jakarta'], 
    'Stok' : [7, 7, 7, 7, 7, 7, 7], 
    'Harga' : [10, 10, 10, 10, 10, 10, 10]
    }

def readIkan ():
    while True:
        print()
        print('Menu Tampilkan Data Ikan')
        print()
        print('1. Tampilkan Semua Ikan')
        print('2. Tampilkan Ikan Berdasarkan Nama')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi1 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan: '))
        except ValueError:
            print()
            print('Input tidak valid, harap masukkan angka.')
            continue
        print()
        
        if opsi1 == 1:
            print('Daftar Semua Ikan:')
            print()
            print(tabulate(ikan, headers='keys', showindex='always', colalign=('center', 'center', 'center', 'center', 'center')))
            print()
            
        elif opsi1 == 2:
            print()
            print(tabulate(ikan, headers='keys', showindex='always'))
            print()
            nyariIkan = input('Masukkan Nama Ikan yang Ingin Dicari: ').title()
            
            if nyariIkan in ikan['Nama']:
                indexReadIkan = ikan['Nama'].index(nyariIkan)
                print()
                print(f'Data Ikan {nyariIkan}:')
                print(f"Nama: {ikan['Nama'][indexReadIkan]}")
                print(f"Ukuran: {ikan['Ukuran'][indexReadIkan]}")
                print(f"Origin: {ikan['Origin'][indexReadIkan]}")
                print(f"Stok: {ikan['Stok'][indexReadIkan]}")
                print(f"Harga: {ikan['Harga'][indexReadIkan]}")
                print()
            else:
                print()
                print(f'Ikan dengan nama {nyariIkan} tidak ditemukan.')
                print()
        
        elif opsi1 == 3:
            break
        
        else:
            print('Pilihan tidak valid.')
    
def nambahIkan ():
    while True:
        print()
        print('Menu Tambah Ikan')
        print()
        print('1. Tambah Ikan Baru')
        print('2. Tambah Stok Ikan')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi2 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan: '))
        except ValueError:
            print()
            print('Input tidak valid, harap masukkan angka.')
            continue
        print()
        
        if opsi2 == 1:
            tambahIkan = input('Masukan Nama Ikan Yang Ingin Ditambah: ').title()
            ukuranIkanBaru = int(input('Masukkan Ukuran Ikan: '))
            originIkanBaru = input('Masukkan Origin Ikan: ')
            stokIkanBaru = int(input('Masukkan Jumlah Stok Ikan: '))
            HargaIkanBaru = int(input('Masukkan Harga Ikan: '))
            ikan['Nama'].append(tambahIkan)
            ikan['Ukuran'].append(ukuranIkanBaru)
            ikan['Origin'].append(originIkanBaru)
            ikan['Stok'].append(stokIkanBaru)
            ikan['Harga'].append(HargaIkanBaru)
            print()
            print(f'Ikan {tambahIkan} Berhasil Ditambahkan!')
            print()
            print(tabulate(ikan, headers = 'keys', showindex = 'always', colalign=('center', 'center', 'center', 'center', 'center')))
        
        elif opsi2 == 2:
            print()
            print(tabulate(ikan, headers = 'keys', showindex = 'always', colalign=('center', 'center', 'center', 'center', 'center')))
            print()
            tambahStokIkan = input('Masukkan Nama Ikan yang Sudah Ada: ').title()
            if tambahStokIkan in ikan['Nama']:
                jumlahBaru = int(input('Masukkan jumlah stok ikan tambahan: '))
                indexTambahIkan = ikan['Nama'].index(tambahStokIkan)
                ikan['Stok'][indexTambahIkan] += jumlahBaru
                print()
                print(f'Stok Ikan {tambahStokIkan} Berhasil Ditambahkan!')
                print()
                print(tabulate(ikan, headers = 'keys', showindex = 'always', colalign=('center', 'center', 'center', 'center', 'center')))
            else:
                print()
                print(f'ikan {tambahStokIkan} tidak ditemukan')
        
        elif opsi2 == 3:
            break
        
        else:
            print('pilihan tidak valid.')
            
def deleteIkan ():
    while True:
        print()
        print('Menu Hapus Ikan')
        print()
        print('1. Hapus Ikan')
        print('2. Kembali ke Menu Utama')
        print()
        try:
            opsi3 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan: '))
        except ValueError:
            print()
            print('Input tidak valid, harap masukkan angka.')
            continue
        print()
        
        if opsi3 == 1:
            print(tabulate(ikan, headers='keys', showindex='always', colalign=('center', 'center', 'center', 'center', 'center')))
            print()
            hapusIkan = input('Masukkan Nama Ikan yang Ingin Dihapus: ').title()
            
            if hapusIkan in ikan['Nama']:
                indexHapusIkan = ikan['Nama'].index(hapusIkan)
                
                del ikan['Nama'][indexHapusIkan]
                del ikan['Ukuran'][indexHapusIkan]
                del ikan['Origin'][indexHapusIkan]
                del ikan['Stok'][indexHapusIkan]
                del ikan['Harga'][indexHapusIkan]
                
                print()
                print(f'Ikan {hapusIkan} Berhasil Dihapus!')
                print()
                print(tabulate(ikan, headers='keys', showindex='always', colalign=('center', 'center', 'center', 'center', 'center')))
            else:
                print()
                print(f'Ikan {hapusIkan} tidak ditemukan!')
        
        elif opsi3 == 2:
            break
        
        else:
            print('Pilihan tidak valid.')

keranjang = []
            
def updateIkan():
    while True:
        print()
        print('Menu Pembelian Ikan')
        print()
        print('1. Beli Ikan')
        print('2. Checkout')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi4 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan: '))
        except ValueError:
            print()
            print('Input tidak valid, harap masukkan angka.')
            continue
        print()
        
        if opsi4 == 1:
            print(tabulate(ikan, headers='keys', showindex='always'))
            print()
            
            beliIkan = input('Masukkan Nama Ikan yang Ingin Dibeli: ').title()
            print()
            
            if beliIkan in ikan['Nama']:
                indexBeliIkan = ikan['Nama'].index(beliIkan)
                
                print(f"Stok tersedia untuk {beliIkan}: {ikan['Stok'][indexBeliIkan]} ikan.")
                print()
                jumlahBeli = int(input('Masukkan jumlah ikan yang ingin dibeli: '))
                print()
                totalHarga = jumlahBeli * ikan['Harga'][indexBeliIkan]
                
                while True:

                    if jumlahBeli <= ikan['Stok'][indexBeliIkan]:
                        ikan['Stok'][indexBeliIkan] -= jumlahBeli
                        keranjang.append({'Nama': beliIkan, 'Jumlah': jumlahBeli, 'Total Harga': totalHarga})
                        print()
                        print(tabulate(keranjang, headers='keys', showindex='always'))
                        print()
                        print(f'{jumlahBeli} ikan {beliIkan} ditambahkan ke keranjang.')
                        print()
                        print(f'Total Harga Sebesar Rp. {totalHarga}')
                        break
                    else:
                        print()
                        print('Stok Ikan Tidak Cukup!')
                        break
            else:
                print(f'Ikan {beliIkan} tidak ditemukan!')
                print()
        elif opsi4 == 2:
            if keranjang:
                    print(tabulate(keranjang, headers='keys', showindex='always', colalign=('center', 'center', 'center', 'center', 'center')))
                    totalPembayaran = sum(item['Total Harga'] for item in keranjang)
                    print(f'Total Harga: {totalPembayaran}')
                    while True:
                        print()
                        uangBayar = int(input('Masukkan Jumlah Uang: '))
                        if uangBayar < totalPembayaran:
                            print(f'Transaksi Dibatalkan, uang kurang {totalPembayaran - uangBayar}')
                        elif uangBayar == totalPembayaran:
                            print('Transaksi Berhasil!')
                            print('Terima Kasih')
                            keranjang.clear()
                            break
                        else:
                            print(f'Transaksi Berhasil!, Uang Kembalian Anda Sebesar Rp.{uangBayar - totalPembayaran}')
                            print('Terima Kasih')
                            keranjang.clear()
                            break
            else:
                    print("Keranjang kosong, tidak bisa checkout.")
        elif opsi4 == 3:
            break
        
        else:
            print('Pilihan tidak valid.')
       
while True:
    print()
    print('===== welcome to adrian fish store =====')
    print()
    print('List Menu')
    print()
    print('1. Menampilkan Data ikan')
    print('2. Menambah Ikan')
    print('3. Menghapus Ikan')
    print('4. Membeli Ikan')
    print('5. Exit Program')
    print()

    try:
        menu = int(input("Masukkan Pilihan Menu Ingin Dijalankan: "))
    except ValueError:
        print()
        print('Input tidak valid, harap masukkan angka.')
        continue
    print()
    
    if menu == 1:
        readIkan ()

    elif menu == 2:
        nambahIkan ()

    elif menu == 3:
        deleteIkan ()

    elif menu == 4:
        updateIkan ()
        
    elif menu == 5:
        print('Terima Kasih!')
        print('Exit Program')
        break

    else:
        print()
        print("Pilihan menu tidak valid")
        continue