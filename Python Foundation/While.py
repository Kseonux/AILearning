a =3
print (str(a),"orang")

a = 8
while a < 10:
    print (a)
    a += 1
else:
    print ("woy maling woy, selesai")

#else jalan jika false, selama while kondisi = true maka akan dijalankan dan dicek lagi dan dijalankan lagi. Dalam case ini loop berakhir setelah kondisi 10 dan diatasnya.

#jika pake fungsi biasa dibawah sebetulnya salah jika tanpa (str(a)). Salah karena 8 bukan string, sebetulnya bisa lebih simpel, tinggal pake petik aja 8nya cuma ya biar keren tapi ini boros jadi ga keren.
"""
a = 8
b = (str(a))
while b.isdigit():
    print (b)
else:
    print (str(a))
"""
#else jalan jika false, selama while kondisi = true maka akan dijalankan dan dicek lagi dan dijalankan lagi. Dalam caseku akan unlimited loop karena nilai akan terus benar.

a = True
b = False
c = 2.5 + 3 #2.5 adalah float, 3 adalah int, python otomatis mengonversi 3 int menjadi float makanya 5.5 adalah float
d = float(c) #gada gunanya
print(d)

























