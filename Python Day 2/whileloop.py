#a = 0
#while a < 10:
#    a = a + 1
#    print (a)

#other whileloop

a = 1
s = 0

print("masukan angka untuk di tambahkan :")
print("masukan angka 0 untuk keluar")

while a != 0:
    print("Jumlah :", s)
    a = float(input("angka? "))
    s = s + a
print("Jumlah Total :", s)