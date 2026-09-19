huruf = " "
geser = 3
hasil = ""
teks ="Hola amigo"

for i in teks:
    if i.isupper():
        posisi = ord(i) - 65
        posisi_geser = (posisi + geser) % 26
        huruf_baru = chr(posisi_geser + 65)
    elif i.islower():
        posisi = ord(i) - 97
        posisi_geser = (posisi + geser) % 26
        huruf_baru = chr(posisi_geser + 97)
    else:
        huruf_baru = huruf
    hasil = hasil + huruf_baru
print(hasil)
