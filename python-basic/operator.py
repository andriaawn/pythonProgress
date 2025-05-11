# operators is a special symbol that is used to perform operations on operands.


print(10 + 2) # addition operator
print(10 - 2) # subtraction operator
print(10 * 2) # multiplication operator
print(10 / 2) # division operator
print(10 % 2) # modulus operator, sisa hasil bagi dua bilangan contoh 10 % 2 = 0
print(10 ** 2) # exponent operator, pangkat dua bilangan contoh 10 ** 2 = 100
print(10 // 2) # floor division operator, pembagian bulat contoh 10 // 2 = 5
print(10 // 3) # floor division operator, pembagian bulat contoh 10 // 3 = 3


# assigment operator
# operator yang digunakan untuk memberikan nilai pada variabel

a = 10
b = 20 

a += 5 
print(a) # 15, a = a + 5
b -= 5 
print(b) # 15, b = b - 5
a *= 5
print(a) # 75, a = a * 5
b /= 5
print(b) # 3.0, b = b / 5
a %= 5

# etc ..

# python comparation operator
# operator yang digunakan untuk membandingkan dua nilai dan menghasilkan nilai boolean (True/False)

print(10 == 10) # True, sama dengan
print(10 != 10) # False, tidak sama dengan
print(10 > 10) # False, lebih besar dari
print(10 < 10) # False, lebih kecil dari
print(10 >= 10) # True, lebih besar sama dengan
print(10 <= 10) # True, lebih kecil sama dengan


# python logical operator
# operator yang digunakan untuk menggabungkan dua atau lebih kondisi
# dan menghasilkan nilai boolean (True/False)
# and, or, not
print(10 > 5 and 5 < 10) # True, kedua kondisi benar

# and, jika kedua kondisi benar maka hasilnya True
# or, jika salah satu kondisi benar maka hasilnya True
# not, membalikkan nilai boolean, jika True menjadi False dan sebaliknya

print(10 > 5 or 5 > 10) # True, salah satu kondisi benar
print(not (10 > 5)) # False, membalikkan nilai boolean
print(not (10 < 5)) # True, membalikkan nilai boolean

# logical operator bisa digunakan untuk menggabungkan beberapa kondisi
print(10 > 5 and 5 < 10 or 10 == 10) # True, salah satu kondisi benar
print(10 > 5 and 5 < 10 and 10 == 10) # True, semua kondisi benar
print(10 > 5 and 5 < 10 and 10 != 10) # False, salah satu kondisi salah
print(10 > 5 and 5 < 10 and 10 >= 10) # True, semua kondisi benar

# identity operator
# operator yang digunakan untuk membandingkan dua objek

# is, jika kedua objek sama maka hasilnya True
# is not, jika kedua objek tidak sama maka hasilnya True

print(10 is 10) # True, kedua objek sama
print(10 is not 10) # False, kedua objek sama
print(10 is 20) # False, kedua objek tidak sama


# membership operator
# operator yang digunakan untuk memeriksa apakah suatu nilai ada dalam suatu objek
# in, jika nilai ada dalam objek maka hasilnya True
# not in, jika nilai tidak ada dalam objek maka hasilnya True

print(10 in [10, 20, 30]) # True, 10 ada dalam list
print(10 not in [20, 30, 40]) # True, 10 tidak ada dalam list

print(10 in (10, 20, 30)) # True, 10 ada dalam tuple
print(10 not in (20, 30, 40)) # True, 10 tidak ada dalam tuple
print(10 in {10, 20, 30}) # True, 10 ada dalam set
print(10 not in {20, 30, 40}) # True, 10 tidak ada dalam set
print(10 in {10: 'a', 20: 'b', 30: 'c'}) # True, 10 ada dalam dictionary   
print(10 not in {20: 'a', 30: 'b', 40: 'c'}) # True, 10 tidak ada dalam dictionary

print(10 in '10 20 30') # True, 10 ada dalam string
print(10 not in '20 30 40') # True, 10 tidak ada dalam string


# bitwise operator
# operator yang digunakan untuk melakukan operasi bit pada bilangan bulat
# operator ini bekerja pada level bit, bukan pada level nilai

# AND, OR, XOR, NOT, LEFT SHIFT, RIGHT SHIFT

# presedence operator
# operator yang digunakan untuk menentukan urutan eksekusi operator dalam suatu ekspresi
# operator dengan presedence lebih tinggi akan dieksekusi terlebih dahulu
# operator dengan presedence lebih rendah akan dieksekusi kemudian
# operator dengan presedence yang sama akan dieksekusi dari kiri ke kanan

# example:
print(10 + 5 * 2) # 20, perkalian dieksekusi terlebih dahulu
print((10 + 5) * 2) # 30, kurung dieksekusi terlebih dahulu
print(10 + 5 - 2 * 3) # 15, perkalian dieksekusi terlebih dahulu

