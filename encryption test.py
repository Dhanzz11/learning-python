def enkripsi(teks, geser):
    huruf = " "
    geser = 3
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

def dekripsi(teks, balikan):
    balikan = 3
    huruf = " "
    for i in teks:
        if i.isupper():
            posisi = ord(i) - 65
            posisi_geser = (posisi - balikan) % 26
            huruf_baru = chr(posisi_geser + 65)
        elif i.islower():
            posisi = ord(i) - 97
            posisi_geser = (posisi - balikan) % 26
            huruf_baru = chr(posisi_geser + 97)
        else:
            huruf_baru = huruf
        hasil = hasil + huruf_baru

        print(hasil)

def file_log(teks_a, teks_h):
    with open ("log.txt", "a") as file:
        file.write (f"teks asli: {teks_a}  hasil: {teks_h}")
    with open ("log.txt", "r") as file:
        isi_log = file.read()
        print(isi_log)

def main():