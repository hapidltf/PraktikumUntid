# nama = "Hafidz" #string menyimpan karakter
# umur = 18       #int  menyimpan bilangan bulat
# BB = 50.0       #float menyimpan desimal

# print("Nama: ", nama)
# print("Umur: ", umur)     # print digunakan untuk menampilkan data
# print("Berat Badan: ", BB)

# angka_string = "123";  # string
# angka_float = 123.89; # float
# angka_integer = 54;    # int


# strtoint = int(angka_string);           # konversi string menjadi integer
# floattoint = int(angka_float);            # konversi float menjadi integer
# inttofloat = float(angka_integer);            # konversi integer menjadi float
# inttostr = str(angka_integer);            # konversi integer menjadi string

# print("String menjadi Int: ", strtoint, "type = ", type(strtoint));
# print("Float menjadi int: ", floattoint, "type = ", type(floattoint));   # hasil konversi
# print("Int menjadi Float: ", inttofloat, "type = ", type(inttofloat));
# print("int menjadi String: ", inttostr, "type = ", type(inttostr));


nama = input("Masukan Nama: ");
usia = input("Masukan Usia: ");     # input digunakan untuk menginput data
Tb = input("Masukan Tinggi Badan: ");

print("\n-- Data Yang Telah di Inputkan --");
print(f"Nama: ", nama);
print(f"Usia: ", usia );        #f digunakan untuk mengubah string tersebut menjadi 
print(f"Tinggi Badan: ", Tb);   #template yang dapat diisi dengan nilai variabel yang diberikan.