# # operasi aritmatika

# a = 10
# b = 5

# # penjumlahan
# hasil = a + b
# print("a + b = ", hasil)

# # pengurangan
# hasil = a - b
# print("a - b = ", hasil)

# # perkalian
# hasil = a * b
# print("a * b = ", hasil)

# #   pembagian
# hasil = a / b
# print("a / b = ", hasil)

# # modulus
# hasil = a % b
# print("a % b = ", hasil)

# # eksponen
# hasil = a ** b
# print("a ** b = ", hasil)

# # floor division
# hasil = a // b
# print("a // b = ", hasil)


# # program konversi celcius ke satuan lain 
# print("\n PROGRAM KONVERSI TEMPERATUR \n") 
# celcius = float(input( "Masukan suhu dalam celcius : ")) 
# print( "suhu adalah", celcius,  "Celcius")

# # reamur
# reamur = (4/5) * celcius
# print( "Suhu dalam reamur adalah ", reamur,  "Reamur")

# # fahrenheit 
# fahrenheit = ((9/5) * celcius) + 32 
# print( "Suhu dalam fahrenheit adalah ", fahrenheit,  "Fahrenheit") 

# # kelvin 
# kelvin = celcius + 273 
# print( "Suhu dalam kelvin adalah ", kelvin,  "Kelvin") 

# # operasi komperasi 
#  # setiap hasil dari operasi komperasi adalah boolean   
# # >,<,>=,<=,==,!=,is,is not 

# a = 4 
# b = 2 

# # lebih besar dari > 
# print("=============== lebih besar dari (>)")
# hasil = a > 3
# print(a, "> ",b, "= ",hasil) 
# hasil = b > 3 
# print(b, "> ",3, "= ",hasil)
# hasil = b > 2 
# print(b, ">",2, "= ",hasil)

# # kurang dari < print(“=============== kurang dari (<)”) 
# hasil = a < 3 
# print(a, "< ",b, "= ",hasil) 
# hasil = b < 3 
# print(b, "< ",3, "= ",hasil) 
# hasil = b < 2 
# print(b, "< ",2, "= ",hasil)

# # lebih dari sama dengan >= print(“=============== lebih dari sama dengan (>=)”)
# hasil = a >= 3 
# print(a, ">= ",b, "= ",hasil)
# hasil = b >= 3 
# print(b, ">= ",3, "= ",hasil) 
# hasil = b >= 2 
# print(b, ">= ",2, "= ",hasil) 

# # kurang dari sama dengan <= print(“=============== kurang dari sama dengan (<=)”)
# hasil = a <= 3 
# print(a, "<= ",b, "= ",hasil) 
# hasil = b <= 3 
# print(b, "<= ",3, "= ",hasil) 
# hasil = b <= 2 
# print(b, "<= ",2, "= ",hasil) 

# # sama dengan (==) print(“=============== sama dengan (==)”) 
# hasil = a == 4 
# print(a, "== 4", "= ", hasil) 
# hasil = b == 4 
# print(b, "== 4", "= ", hasil)

# # tidak sama dengan (!=) print(“=============== sama dengan (!=)”) 
# hasil = a != 4 
# print(a, "!= 4", "= ", hasil) 
# hasil = b != 4 
# print(b, "!= 4", "= ", hasil)

# # ‘is " sebagai komparasi obj identity (bukan literal) 
# x = 5 # ini adalah assignment membuat object
# y = 5
# hasil = x is y 
# print("x is y = ",hasil)
# # ‘is not " sebagai komparasi obj identity (bukan literal) 
# x = 5 # ini adalah assignment membuat object 
# y = 6 
# hasil = x is not y 
# print("x is not y = ",hasil)  


# Tugas 
# menghitung sebuah volume luas dan keliling dari bangunan

# Input panjang, lebar dan tinggi
print("\n")
print("----Menghitung Volume Luas dan Keliling Bangunan----")
print("\n")

# A
p = float(input("Panjang: "))
l = float(input("Lebar: "))
t = float(input("Tinggi: "))

volume = p * l * t                   # rumus volume
luas = 2 * (p * l + p * t + l * t)   # rumus luas
keliling = 4 * (p + l + t)           # rumus keliling

print("\n")
print("Volume = ", volume)
print("Luas = ", luas)           # menampilkan hasil inputan
print("Keliling = ", keliling)

print("\n")

# B
# mengecek apakah luas bangun tersebut > 50
hasil = luas > 50
print("luas bangun tersebut lebih besar dari 50", hasil)

print("\n")

# C
# mengecek apakah volume bangun tersebut = 480
hasil = volume == 480
print("volume bangun tersebut lebih besar dari 480", hasil)