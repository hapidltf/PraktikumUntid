# import datetime  

# mahasiswa1 = {  
#     "nama":"Ucup Surucup",  
#     "nim" :"19022001",  
#     "sks_lulus":130,  
#     "beasiswa": False,  
#     "lahir":datetime.datetime(2001,4,10) # tahun, tanggal, bulan 
#     }   

# mahasiswa2 = {  
#     "nama":"Azan Magrib",  
#     "nim" :"19022002",  
#     "sks_lulus":140,  
#     "beasiswa":True,  
#     "lahir":datetime.datetime(2002,10,10) # tahun, tanggal, bulan 
#     }   

# mahasiswa3 = {  
#     "nama": "Slamet Dunia Akhirat", 
#     "nim" :"19022003",  
#     "sks_lulus":100,
#     "beasiswa":True,  
#     "lahir":datetime.datetime(1977,5,10) # tahun, tanggal, bulan 
#     }  

# data_mahasiswa = {  
#     "MAH001":mahasiswa1,  
#     "MAH002":mahasiswa2,  
#     "MAH003":mahasiswa3, }  

# # print(data_mahasiswa['MAH002']['nama']) 

# print(f"{"KEY":<6} {"Nama":<6} {"SKS":<3} {"Beasiswa":<9} {"Lahir":<10}") 
# print("-"*50)  # ... kode sebelumnya (import dan deklarasi dictionary) tetap sama ...

# print(f"{'KEY':<7} {'Nama':<20} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}") 
# print("-" * 60)


# for mahasiswa in data_mahasiswa:     
#     KEY = mahasiswa          
#     NAMA = data_mahasiswa[KEY]["nama"]     
#     NIM = data_mahasiswa[KEY]["nim"]     
#     SKS = data_mahasiswa[KEY]["sks_lulus"]     
#     BEASISWA = data_mahasiswa[KEY]["beasiswa"]     
#     LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")   

#     print(f"{KEY:<6} {NAMA:<20} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")


# import datetime 

# mahasiswa_template = {      
#     "nama":"nama",  
#     "nim":00000000,  
#     "sks_lulus":0,  
#     "lahir":datetime.datetime(1111,1,11) }  

# data_mahasiswa = {}  

# print(f"{"SELAMAT DATANG":^20}") 
# print(f"{"DATA MAHASISWA":^20}") 
# print("-"*20)  

# mahasiswa = dict.fromkeys(mahasiswa_template.keys()) 
# print(mahasiswa) 

# mahasiswa["nama"] = input("Nama Mahasiswa: ") 
# mahasiswa["nim"] = input("NIM Mahasiswa: ") 
# mahasiswa["sks_lulus"] = int(input("SKS Lulus")) 
# TAHUN_LAHIR = int(input("Tahun lahir (YYYY): ")) 
# BULAN_LAHIR = int(input("Bulan lahir (1-12): ")) 
# TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): ")) 
# mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)  

# print(mahasiswa) 


# import datetime 
# import os 
# import string 
# import random  

# # template dict mahasiswa 
# mahasiswa_template = {  
#     'nama':'nama',  
#     'nim':'00000000',  
#     'sks_lulus':0,  
#     'lahir':datetime.datetime(1111,1,11) }

# data_mahasiswa = {}  

# while True:  
#     # os.system("cls") # untuk windows  
#     os.system("clear")  
#     print(f"{'SELAMAT DATANG':^20}")  
#     print(f"{'DATA MAHASISWA':^20}")  
#     print("-"*20)   
#     mahasiswa = dict.fromkeys(mahasiswa_template.keys())  
#     mahasiswa['nama'] = input("Nama Mahasiswa: ")  
#     mahasiswa['nim'] = input("NIM Mahasiswa: ")  
#     mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))  
#     TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))  
#     BULAN_LAHIR = int(input("Bulan lahir (1-12): "))  
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))  
#     mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)   

#     KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))  
#     data_mahasiswa.update({KEY:mahasiswa})   
    
#     # dari program sebelumnya, hilangkan beasiswa  
#     print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")  
#     print('-'*60)   
    
#     for mahasiswa in data_mahasiswa:   
#         KEY = mahasiswa      
#         NAMA = data_mahasiswa[KEY]['nama']   
#         NIM = data_mahasiswa[KEY]['nim']   
#         SKS = data_mahasiswa[KEY]['sks_lulus']   
#         LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")      
#         print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")   
#         print("\n")  
        
#         is_done = input("Mau tambah lagi bro (y/n)? ") 

#         if is_done == "n":  
#             print("\nAkhir dari program, terima kasih") 
#             break  



# Latihan

import datetime
import os
import string
import random

perpus_template = {
    "judul" : 'judul',
    "penulis" : 'penulis',
    "tahun" : 0,
    "tglpinjam" : datetime.datetime(1111,1,11)
}

data_perpus = {}

while True:
    os.system("clear") 
    print("-"*30)  
    print(f"{'Selamat Datang Di Perpusatakaan':^30}")
    print(f"{'Masukkan Data Buku':^30}")
    print("-"*30)  

    buku = dict.fromkeys(perpus_template.keys())
    buku ['judul'] = input("Masukkan Judul Buku : ")
    buku ['penulis'] = input("Masukkan Penulis Buku : ")
    buku ['tahun'] = int(input("Masukkan Tahun Terbit : "))
    TAHUN_PINJAM = int(input("Tahun Pinjam (YYYY) : "))
    BULAN_PINJAM = int(input("Bulan Pinjam (1-12) : "))
    TANGGAL_PINJAM = int(input("Tanggal Pinjam (1-31) : "))
    buku ['tglpinjam'] = datetime.datetime(TAHUN_PINJAM,BULAN_PINJAM,TANGGAL_PINJAM)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    data_perpus.update({KEY:buku})

    print(f"\n{'KEY':<6} {'Judul':<17} {'Penulis':<10} {'Tahun':<10} {'Tanggal Pinjam':<10}")  
    print('-'*60)  

    for key in data_perpus:
        KEY = key
        JUDUL = data_perpus[KEY]['judul']
        PENULIS = data_perpus[KEY]['penulis']
        TAHUN = data_perpus[KEY]['tahun']
        TGL = data_perpus[KEY]['tglpinjam'].strftime("%x") 
        print(f"{KEY:<6} {JUDUL:<17} {PENULIS:<10} {TAHUN:^10} {TGL:^10}")   
        print("\n") 

    is_done = input("Apakah anda ingin menambahkan buku? (y/n) : ")

    if is_done == "n" : 
        print("\n Terimakasih!!!!!")
        break