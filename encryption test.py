def enkripsi(teks, geser):
    huruf =""
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
            huruf_baru = huruf
        hasil = hasil + huruf_baru
    return hasil

def dekripsi(teks, balikan):
    hasil =""
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
    return hasil

def file_log(teks_a, teks_h, mode):
    with open ("log.txt", "a") as file:
        file.write (f"teks asli: {teks_a}  hasil: {teks_h} mode: {mode}\n")

def lihat_riwayat():
    with open("log.txt", "r") as file:
        isi_log = file.read()
        return isi_log

def main():
    while True:
        print("=== CAESAR CIPHER TOOL ===")
        print("1. Enkripsi teks")
        print("2. Dekripsi teks")
        print("3. Lihat riwayat")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            teks = input("Masukan teks yang ingin disamarkan: ")
            geser = 3
            hasil = enkripsi(teks, geser)
            file_log(teks, hasil, "ENKRIPSI")
            print(hasil)
        elif pilihan == "2":
            teks = input("Masukan teks yang ingin dikembalikan: ")
            balikan = 3
            hasil = dekripsi(teks, balikan)
            file_log(teks, hasil, "DEKRIPSI")
            print(hasil)
        elif pilihan == "3":
            riwayat =lihat_riwayat()
            print(riwayat)
        elif pilihan == "4":
            print("Okeh bsokyu\n")
            break
        else:
            print("Pilihan apo dio, mana ada\n")

main()