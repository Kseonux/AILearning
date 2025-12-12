#dict mirip set tandanya{}
#order tapi no duplicates, bisa diubah

kelas = {"meja": "kayu",
         "kursi":"besi",
         "pencase": "pen"}

# kelas.update({"komputer": "files"})
# kelas.pop("meja")
# kelas.popitem()

key = kelas.keys()
for ky in kelas.keys():
    print (ky)

valuee = kelas.values()
for val in valuee:
    print(val)

itemm = kelas.items()
for key, value in itemm:
    print(f"{key}:  {value}")









print(kelas)







































