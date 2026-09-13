# # operasi logika atau boolean 

# # not, or, and, xor  

# print("===NOT===") 

# a = True 
# b = not a

# print("data a =",a)
# print("------------ NOT") 
# print("data b =",b)  

# # OR (jika salah satu true, maka hasilnya adalah true)
# print("===OR===") 
# a = False 
# b = False 
# c = a or b 
# print(a,"OR",b,"=",c) 

# a = False 
# b = True 
# c = a or b 
# print(a,"OR",b,"=",c) 

# a = True 
# b = False 
# c = a or b 
# print(a,"OR",b,"=",c) 

# a = True 
# b = True 
# c = a or b 
# print(a,"OR",b,"=",c)

# # AND (jika dua buah nilai true, maka hasil true) 
# print("===AND===")
# a = False 
# b = False 
# c = a and b 
# print(a,"AND",b,"=",c) 

# a = False 
# b = True 
# c = a and b 
# print(a,"AND",b,"=",c)

# a = True 
# b = False 
# c = a and b 
# print(a,"AND",b,"=",c) 

# a = True 
# b = True 
# c = a and b 
# print(a,"AND",b,"=",c) 

# # XOR (akan true jika salah satu true, sisanya false)
# print("===XOR===") 
# a = False 
# b = False 
# c = a ^ b 
# print(a,"XOR",b,"=",c) 

# a = False 
# b = True 
# c = a ^ b 
# print(a,"XOR",b,"=",c) 

# a = True 
# b = False 
# c = a ^ b 
# print(a,"XOR",b,"=",c) 

# a = True 
# b = True 
# c = a ^ b 
# print(a,"XOR",b,"=",c)


# Program Kategori Umur

umur = int(input("Masukan Umur: "))

if umur <=12 and umur >= 0:
    print ("Umur anda" , umur, "Tahun masuk dalam kategori Anak-anak")
elif umur <= 17 and umur >= 13:
    print ("Umur anda" , umur, "Tahun masuk dalam kategori Remaja")
elif umur <= 59 and umur >= 18:
    print ("Umur anda" , umur, "Tahun masuk dalam kategori Dewasa")
elif umur >= 60 :
    print ("Umur anda" , umur, "Tahun masuk dalam kategori Lansia")
else:
    print ("Inputan yang anda masukkan salah")