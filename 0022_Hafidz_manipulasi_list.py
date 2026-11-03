# ## --- LIST --- # 
# # Kumpulan data numbers 
# data_angka = [1,5,2,3] 
# print(data_angka) 
# # Kumpulan data_string 
# data_string = ["ucup","adit","siti"] 
# print(data_string) 
# # Kumpulan data boolean 
# data_boolean = [True, False, True, True] 
# print(data_boolean) 

# ## cara alternatif membuat list 
# # Kumpulan campuran 
# data_campuran = [1,"bakwan",2,"cireng","ucup",True,"adit",False] 
# print(data_campuran) 
# data_range = range(0,10,2) 

# # membuat list dengan for loop, list comprehension 
# list_for = [i **2 for i in range(0,10)] 
# print(list_for) 

# # membuat list pake for pake if 
# list_for_if = [i for i in range(0,10) if i !=5]
# print(list_for_if)

# list_for_if = [i for i in range(0, 10) if i % 2 == 0]
# print(list_for_if)

# list_for_if = [i for i in range(0,10) if i %2 != 0]
# print(list_for_if)

# ## --- Operasi LIST --- # 
# # index 0(-3) 1(-2) 2(-1) 
# data = ["Ucup","Adit","Dudung"] 
        
# # mengambil data dari list 
# data_0 = data[0] 
# print(f"data pertama (index 0) = {data_0}") 

# data_terakhir = data[-1] 
# print(f"data terakhir adalah = {data_terakhir}") 

# # mengambil info jumlah data dalam list 
# panjang_data = len(data) 
# print(f"panjang data = {panjang_data}") 

# # manipulasi data list 
# # # menambahkan item pada list sesuai posisi 
# print(f"data sebelum ditambah = \n{data}") 

# #data.insert(posisi,item)
# # menambah di akhir list 
# data.insert(1,"Asep") 
# print(f"data sesudah ditambah= \n{data}") 

# data.append("Ririn") 
# print(f"data ditambah lagi = \n{data}") 

# # menambahkan list dengan list 
# data_baru = ["Luffy","Zoro","Nami"] 
# data.extend(data_baru) 
# print(f"data gabungan = \n{data}") 

# # merubah data
# # kita ubah data 2 menjadi jarwo 
# data[2] = "jarwo" 
# print(f"data rubah = \n{data}")

# # menghapus data 
# data.remove("Ucup")
# print(f"data hapus = \n{data}")

# # menghapus data paling belakang 
# data.pop() 
# print(f"data akhir = \n{data}") 



# ## --- Operasi LIST --- 
# # # index 0(-3) 1(-2) 2(-1) 
# data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0] 
# print(f"data angka = \n{data_angka}") 

# # count data 
# jumlah_data_4 = data_angka.count(4) 
# jumlah_data_3 = data_angka.count(3) 
# print(f"jumlah angka 4 = {jumlah_data_4}") 
# print(f"jumlah angka 3 = {jumlah_data_3}")  

# # ambil posisi data 
# data = ["Rendi","Iqbal","Gana","Khairil"] 
# print(f"data = {data}") 
# index_Iqbal = data.index("Iqbal") 
# index_Gana = data.index("Gana")  
# print(f"index si Iqbal = {index_Iqbal}") 
# print(f"index si Gana = {index_Gana}")  

# # mengurutkan list 
# print(f"data angka sebelum sort = \n{data_angka}") 
# data_angka.sort() 
# print(f"data angka sort = \n{data_angka}")  
# print(f"data = {data}") 
# data.sort() 
# print(f"data sort = {data}") 

# # balik listnya 
# data_angka.reverse() 
# data.reverse() 
# print(f"data di reverse \n{data_angka}") 
# print(f"data di reverse \n{data}")

## --- Nested LIST ---
# data_0 = [1,2] 
# data_1 = [3,4] 
# data_list_biasa = [1,2,3,4] 
# print(f"list biasa = {data_list_biasa}") 
# list_2D = [data_0, data_1, 6,7] 
# print(f"list 2D = {list_2D}") 

# # contoh penggunaan 
# peserta_0 = ["Rendi", 25, "Laki-laki"] 
# peserta_1 = ["Joni", 10, "Laki-laki"] 
# peserta_2 = ["Eka", 50, "Wanita"]

# list_peserta = [peserta_0, peserta_1, peserta_2] 
# print(f"peserta = {list_peserta}")


# for peserta in list_peserta: 
#     print(f"nama\t : {peserta[0]}") 
#     print(f"umur\t : {peserta[1]}") 
#     print(f"Gender\t : {peserta[2]}\n") 


# Latihan

# # Soal no 1

# kendaraan = ["motor", "mobil", "sepeda", "bus"]
# # a. menambahkan truk di akhir list
# kendaraan.append("truk") 
# print("\n")
# print(f"Menambahkan data truk = \n{kendaraan}") 
# print("\n")
# # b. menyisipkan becak pada index ke 1
# kendaraan.insert(1, "becak")
# print("\n")
# print(f"Menambahkan data becak = \n{kendaraan}") 
# print("\n")
# # c. menghapus data yang berada di belakang
# kendaraan.pop()
# print("\n")
# print(f"Mendelete data terakhir = \n{kendaraan}") 
# print("\n")
# # d. mengubah sepeda menjadi skuter
# kendaraan[3] = "skuter"
# print(f"mengubah menjadi skuter = \n{kendaraan}") 
# print("\n")
# # e. menampilkan informasi jumlah total data tersebut
# panjangdata = len(kendaraan)
# print(f"jumlah data dalam list = {panjangdata}") 
# print("\n")



# # Soal no 2

# angka = [75, 80, 90, 75, 85, 100, 65]
# print(f"angka = {angka}") 
# # a. mencari tahu 100 ada di index berapa
# index = angka.index(100)
# print("\n")
# print(f"100 berada di index = {index}") 
# print("\n")
# # b. mengitung jumlah siswa dengan nilai 75
# count75 = angka.count(75)
# print(f"jumlah nilai 75 = {count75}") 
# print("\n")
# # c. mengurutkan skor dari terkecil kebersar
# angka.sort()
# print(f"mengurtkan dari kecil ke besar = {angka}") 
# print("\n")
# # d. kebalikan dari besar ke kecil
# angka.reverse()
# print(f"mengurtkan dari besar ke kecil = {angka}") 
# print("\n")



# # Soal no 3

# menu_utama = ["Nasi Goreng", "Mie Ayam"] 
# menu_tambahan = ["Kerupuk", "Es Teh"] 

# main_menu = [menu_utama,menu_tambahan]
# print("\n")
# print(f"Menu yang tersedia: {main_menu}")
# print("\n")



# Soal no 4

buku = ["Buku", 5000]
pensil = ["Pensil", 2000]
penggaris = ["Penggaris", 3000]

data_barang = [buku, pensil, penggaris] 

# a. menampilkan data harga pensil dari nested list
print("\n")
print(f"Nama barang: {pensil[0]}")
print(f"Harga: {pensil[1]}")
print("\n")

# b. menggunakan looping untuk menampikan semua data
print("\n")

print("List data barang")
for item in data_barang:
    print(f"Nama barang : {item[0]}")
    print(f"Harga barang : Rp.{item[1]}")
    print("\n")