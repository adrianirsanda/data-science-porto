import os
import platform

def clear_terminal():

    system = platform.system().lower()

    if system == 'windows':
        os.system('cls')

    else:
        os.system('clear')

clear_terminal()

# soal 1

# angka = [41, 5, 1 , 3, 89, 32]

# max_value = angka[0]
# min_value = angka[0]

# for i in angka:
#     if i > max_value:
#         max_value = i
#     if i < min_value:
#         min_value = i

# print(f'maximum value: {max_value}')
# print(f'minimum value: {min_value}')

# soal 2

# container = []
# for i in range (8):
#     if i % 3 != 0:
#         container.append(i**2)
# print(container)

# soal 3

# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'.title()

# x = kalimat.split()

# aku = x.count('Aku')
# baru = x.count('Baru')
# makan = x.count('Makan')
# nasi = x.count('Nasi')
# terus = x.count('Terus')
# mau = x.count('Mau')
# mie = x.count('Mie')
# nanti = x.count('Nanti')
# malam = x.count('Malam')

# print(f'Jummlah kata 'Aku' ada {aku}')
# print(f'Jummlah kata 'Baru' ada {baru}')
# print(f'Jummlah kata 'Makan' ada {makan}')
# print(f'Jummlah kata 'Nasi' ada {nasi}')
# print(f'Jummlah kata 'Terus' ada {terus}')
# print(f'Jummlah kata 'Mau' ada {mau}')
# print(f'Jummlah kata 'Mie' ada {mie}')
# print(f'Jummlah kata 'Nanti' ada {nanti}')
# print(f'Jummlah kata 'Malam' ada {malam}')

# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# result = kalimat.title().split()
# print(result)
# unique = []
# for i in result:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# for y in unique:
#     print(f'jumlah kata {y} ada {result.count(y)}')

# ===================================================================================
# SET
# ditandai dengan kurung kurawal
# tidak boleh ada duplikat data
# boleh memiliki tipe data yang beragam
# hasil random sehingga tidak bisa di indexing
# biasanya dipakai untuk handling duplikat value

# a_set = {1, 2, 3, 4, 5, 100, 'a', 'aa', 5}
# print(a_set)

# a_list = list(a_set) # dibuat jadi set dulu sehingga urutannya menyesuaikan hasil set bukan hasil yang kita tulis
# print(a_list)

# ===================================================================================
# LOOPING IN SET
# a_set = {1, 2, 3, 4, 5, 100, 'a', 'aa', 5}
# for i in a_set:
#     print(i)

# ADD DATA PADA SET
# a_set = {1, 2, 3, 4, 5, 100, 'a', 'aa', 5}
# a_set.add(500)
# print(a_set)

# Menambahkan lebih dari 1 value

# a_set = {1, 2, 3, 4, 5, 100, 'a', 'aa', 5}
# a_set.update({'abe', 'ketua kelas'})
# print(a_set)

# DELETE DATA PADA SET

# a_set = {1, 2, 3, 4, 5, 100, 'a', 'aa', 5}
# a_set.remove(1000)
# print(a_set) # key error : 1000 karena tidak ada 1000 dalam set

# a_set = {1, 2, 3, 4, 5, 100, 'a', 'aa', 5}
# a_set.discard(1000)
# print(a_set)

# remove dan discard hanya bisa menghapus 1 value
# ketika menghapus value yang tidak ada di set, remove menghasilkan error
# ketika menghapus value yang tidak ada di set, discard tidak menghasilkan error

# method in set
# union, intersection, difference, symmetric difference

# ganjil = {1, 3, 5, 7, 9}
# prima = {2, 3, 5, 7, 11}

# # union --> full outer join
# print(ganjil.union(prima))

# # intersection --> irisan
# print(ganjil.intersection(prima))

# # difference --> yang tidak ada di set depan
# print(ganjil.difference(prima))

# # symmetric difference --> yang tidak ada persamaan antara 2 set
# print(ganjil.symmetric_difference(prima))

# DISJOINT, SUBSET, SUPERSET

ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6}
angka = {3, 5}

# disjoint
print(ganjil.isdisjoint(angka))

# subset
print(ganjil.issubset(angka))
print(angka.issubset(ganjil))

# superset
print(ganjil.issuperset(angka))