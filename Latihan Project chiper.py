def baca_file(nama_file):
    with open (nama_file, "r") as file:
        isi_file = file.read()
        return isi_file

def tulis_file(nama_file, isi):
    with open (nama_file, "w") as file:
        file.write (isi)

def tulis_dekrip(nama_file, isi):
    with open ("HasilKembali.txt", "a") as file:
        file.write(f"Nama file: {nama_file} isi: {isi}\n")
    with open ("HasilKembali.txt", "r") as file:
        file.read()

def log_tool(nama_file, aksi, isi):
    with open ("LogTool.txt", "a") as file:
        file.write(f"Nama File: {nama_file} || mode: {aksi} || hasil: {isi}\n")

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
    riwayat_file = []
    while True:
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Saya tak percaya kamu, saya keluar")
        pilihan = input("Pilih mode tool: ")
        if pilihan == "1":
            nama_file = input("Nama File: ")
            teks= baca_file(nama_file)
            nama_hasil_enkripsi = "hasil " + nama_file
            geser = 3
            hasil = enkripsi(teks, geser)
            tulis_file(nama_hasil_enkripsi, hasil)
            print(hasil)
            log_tool(nama_file, "ENKRIPSI", hasil)
            riwayat_file.append({"nama_file": nama_hasil_enkripsi, "aksi": "ENKRIPSI"})
        elif pilihan == "2":
            print("A. Dekripsi teks baru")
            print("B. Dekripsi teks enkripsi")
            pilih = input("Pilih Mode: ")
            if pilih == "A":
                nama_file = input("Nama File: ")
                teks = baca_file(nama_file)
                balikan = 3
                hasil = dekripsi(teks, balikan)
                tulis_dekrip("HasilKembali.txt", hasil)
                print(hasil)
                log_tool(nama_file, "ENKRIPSI", hasil)
            elif pilih == "B":
                for nomor, r in enumerate(riwayat_file, start=1):
                    print(f"{nomor}. {r['nama_file']} ({r['aksi']})")
                nomor_pilih = int(input("Pilih nomor file: "))
                nama_file = riwayat_file[nomor_pilih - 1]["nama_file"]
                balikan = 3
                teks = baca_file(nama_file)
                hasil = dekripsi(teks, balikan)
                tulis_dekrip("HasilKembali.txt", hasil)
                print(hasil)
                log_tool(nama_file, "ENKRIPSI", hasil)
            else:
                print("Ketik yang betul puq")
        elif pilihan == "3":
            print("Abcd dia yang buka, alr catch u later")
            break
        else:
            print("Ketik yang bener su")

main()