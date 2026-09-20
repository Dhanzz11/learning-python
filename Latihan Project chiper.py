def baca_file(nama_file):
    with open (nama_file, "r") as file:
        isi_file = file.read()
        return isi_file

def tulis_file(nama_file, isi):
    with open ("fileHasil.txt", "w") as file:
        file.write (isi)

def enkripsi(teks, geser):
    hasil= ""
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
            huruf_baru = i
        hasil = hasil + huruf_baru
    return hasil

def dekripsi(teks, balikan):
    hasil =""
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
            huruf_baru = i
        hasil = hasil + huruf_baru
    return hasil

def main():
    while True:
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Saya tak percaya kamu, saya keluar")
        pilihan = input("Pilih mode tool: ")
        if pilihan == "1":
            nama_file = input("Nama File: ")
            teks= baca_file(nama_file)
            geser = 3
            hasil = enkripsi(teks, geser)
            tulis_file(nama_file, hasil)
            print(hasil)
        elif pilihan == "2":
            nama_file = input("Nama File: ")
            teks = baca_file(nama_file)
            geser = 3
            hasil = dekripsi(teks, geser)
            tulis_file(nama_file, hasil)
            print(hasil)
        elif pilihan == "3":
            print("Abcd dia yang buka, alr catch u later")
            break
        else:
            print("Ketik yang bener su")

main()