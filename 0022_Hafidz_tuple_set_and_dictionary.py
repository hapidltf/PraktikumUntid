# # LIST 
# # menggunakan kurung siku 
# data_list = [10,2,4,3,2] 
# print(data_list)  

# # tuples 
# data_tuples = (7,8,10,11) 
# print(data_tuples) 
# print(data_tuples[1])  

# # sets (himpunan) 
# data_sets = {10, 4, 3, 2, 7, 6, 5}
# data_list = list(data_sets)
# print(data_list[1]) 

# # tidak bisa dilakukan 
# data_tuples[1] = "ucup" 
# data_tuples.append(1)  

# ## Dictionary  
# # # list → array, mengakses dengan menggunakan index  
# data_list = ["ucup","rendi","salsa"] 
# print(data_list[0])  

# # dictionary (dict) → associative array # identifier → key  
# data_dict = {
#     "key":"value",
#     "cp": "ucup", 
#     "rd": "rendi", 
#     "sl": "salsa", 
#     "nmbr": 100, 
#     "list": data_list } 

# print(data_dict["cp"]) 
# print(data_dict["nmbr"]) 
# print(data_dict["list"]) 



# ## --- Operasi Dictionary ---  
# data_dict = {"cup":"ucup surucup",
#             "pet":"opet saripet", 
#             "ndo":"nando surundo" }  
# # panjang dictionary 
# LENDICT = len(data_dict) 
# print(f"panjang dictionary: {LENDICT}")  

# # mengecek key exist atau tidak 
# KEY = "cup" 
# CHECKKEY = KEY in data_dict 
# print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")  

# # mengakses value (read) dengan get 
# print(data_dict["cup"]) 
# print(data_dict.get("cup")) 
# print(data_dict.get("kis","key tidak ditemukan"))# check key dengan message  

# # # mengupdate data 
# data_dict["cup"] = "ucup si ganteng" 
# print(data_dict) 
# data_dict["de"] = "ade si adek" 
# print(data_dict)  
# data_dict.update({"cup":"ucup surucup"}) 
# print(data_dict) 
# data_dict.update({"iwn":"iwan mang keren"}) 
# print(data_dict) 

# # akan di tambah jika tidak ada print(data_dict)  
# # # menghapus data 
# del data_dict["iwn"] 
# print(data_dict)    


# # --- Looping Dictionary ---  
# teman_teman = { "cup":"ucup surucup",  
#                 "tong":"sotong surotong",  
#                 "lur":"lur sedulur",
#                 "wel":"bung towel"  } 

# # looping first try (yang keluar hanya key)

# for teman in teman_teman: 
#     print(teman) 
# # operator untuk mengambil item 
# keys = teman_teman.keys() 
# print(keys) 

# for key in teman_teman.keys(): 
#     print(teman_teman.get(key)) 


# values = teman_teman.values() 
# print(values) 
    

# for value in teman_teman.values(): 
#     print(value) 
    
# items = teman_teman.items() 
# print(items) 
    
# for item in teman_teman.items(): 
#     print(item) 
    
# for key,value in teman_teman.items(): 
#     print(f"key = {key}, value = {value}") 



    # Latihan

# ## soal 1

# # a.membuat data tuple dengan isi nama, nim, dan prodi
# identitas = ("hapid", 2605060022, "S1 Teknologi Informasi") 

# # b. menampilkan data dengan memanggil index
# print(identitas[0])
# print(identitas[1])
# print(identitas[2])

# # c. mengubah data dalam tuple dan menjelaskan error nya
# # identitas[2] = "teknolgi informasi"

# # d. data sets
# nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5} #ketika data di print maka akan di urutkan dan nilai yang berjumlah lebih dari 1 akan di tampilkan 1 kali
# print(nilai_angka)



## soal 2

# a. membuat dictionary dengan key nama, nim dan prodi
data_mahasiswa = {
    "nim" : "24010",
    "nama" : "Budi Santoso",
    "prodi" : "S1 Teknologi Informasi"
}

# b. mengubah prodi menjadi santra mesin dan menambahkan angkatan
data_mahasiswa["prodi"] = "S1 Sastra Mesin"
data_mahasiswa.update({"angkatan" : "2026"})
print(data_mahasiswa)
print("\n")


# c. delete key nim pada dictionary
del data_mahasiswa["nim"]
print(data_mahasiswa)
print("\n")


# ## Soal 3

# a. membuat dict. keranjang yang berisi beberapa item
keranjang = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}

# b. menampilkan data di atas menggunakan perulangan
key = keranjang.keys()
belanja = keranjang.items()
harga = keranjang.values()

for key,harga in belanja:
    print(f"harga {key}: Rp.{harga}")

# c. menampilkan total belanja
total = 0
for harga1 in keranjang.values():
    total += harga1

print(f"Total Harga adalah : {total}")