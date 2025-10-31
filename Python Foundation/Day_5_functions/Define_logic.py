
wow = input("masukkan angka : ")  # input awal

def greet(w):
    print("ini angka : ", w)      # fungsi fleksibel, bisa panggil kapan aja

greet(wow)                         # greet pertama pakai input awal
print(10)                           # angka baru, tapi wow tetap aman
greet(wow)    

#Jadi kalo w itu kan hanya simpen wow

#Logic 2

wowo = input("masukkan angka : ")  # input awal

def hai(p):

    """dari percobaan yang ada, diambil kesimpulan bahwa w ato p yang ditulis didalam
() cuma jadi parameter fungsi, jadi kalau hai(5) maka otomatis 5
akan dimasukkan ke dalam wowo dan diterima oleh parameter (p) dilanjutkan dengan format yang ditulis.

Tambahan : def ...(...) dia akan ambil dari variabel di atas dan bersifat lokal
makanya nilai diganti di fungsi gak akan merusak variabel global, kalo print bisa keluar juga variabel global."""

    print("ini angka : ", p)      # fungsi fleksibel, bisa panggil kapan aja

hai(5)
hai(wowo)


print(greet.__doc__) #docstring fungsi, mirip komentar bedanya bisa menjadi nilai dan disimpan dalam variabel, bisa sebagai message dari fungsi.



























