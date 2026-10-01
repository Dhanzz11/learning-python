from getpass import getpass

def setting (password):
    kriteria1 = len(password) == 8
    kriteria2 = any(c.isupper() for c in password)
    kriteria3 = any(c.isdigit() for c in password)
    jumlah_Kriteria = sum([kriteria1, kriteria2, kriteria3])

    if jumlah_Kriteria == 3:
        print(f"Password sudah diganti")
        return True
    else:
        print("silahkan penuhi kriteria ini (password harus memiliki 8 karakter, huruf besar dan huruf kecil)")
        return False

def enkripsi(password, geser):
    hasil= ""
    for i in password:
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

def baca_akun(nama_file):
    daftar_akun = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                baris = baris.strip()
                if " || " in baris:
                    bagian = baris.split(" || ")
                    username = bagian[0].replace("username: ", "")
                    password = bagian[1].replace("passwordLogin: ", "")
                    daftar_akun.append({"username": username, "passwordLogin": password})
    except FileNotFoundError:
        pass
    return daftar_akun

def regris_akun(namafile):
    daftar = baca_akun(namafile)

    while True:
        username_baru = input("username akun: ")
        username_ada = False
        for p in daftar:
            if p["username"] == username_baru:
                username_ada = True

        if username_ada:
            print("username sudah dipakai")
        else:
            break

    while True:
        password_akun_baru = getpass("password akun baru: ")
        sembunyikan = enkripsi(password_akun_baru, 9)
        valid = setting(sembunyikan)
        if valid:
            break

    with open(namafile, "a") as file:
        file.write(f"username: {username_baru} || passwordLogin: {sembunyikan}\n")
    print("Akun berhasil dibuat!")

regris_akun("datapwe.txt")