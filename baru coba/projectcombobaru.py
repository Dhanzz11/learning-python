from getpass import getpass
######################################################################################
                                # {S} encryptioan section

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

######################################################################################
                                # 04 setting section

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
    
def data_password(password):
    with open ("datapw.txt", "w") as file:
        file.write(f"passwordLogin: {password}")

######################################################################################
                                # 01 daftar section

def bacadaftar_produk(produk):
    with open (produk , "r") as file:
       daftar = file.read()
       print(daftar)

######################################################################################
                                # c1 opsi 3.A section

def edit_produk(produk):
    nama = input("Produk tambahan: ")
    harga = int(input("harga: "))
    stok = int(input("banyak stok produk: "))
    produk_baru = {"Produk" : nama, "harga" : harga, "Stok" : stok}
    produk.append(produk_baru)

def tulis_daftar(produk):
    daftar_produk = set()
    try:
        with open("daftarProduk.txt", "r") as file:
            for baris in file:
                nama = baris.split(" -- ")[0].replace("Produk : ", "")
                daftar_produk.add(nama)
    except FileNotFoundError:
        pass
    
    with open("daftarProduk.txt", "a") as file:
        for p in produk:
            if p["Produk"] not in daftar_produk:
                file.write(f"Produk : {p['Produk']} -- Rp{p['harga']}\n")
                daftar_produk.add(p['Produk'])


def tulisdatastok(produk):
    daftar_produk = set()
    try:
        with open("datastok.txt", "r") as file:
            for baris in file:
                nama = baris.split(" -- ")[0].replace("Produk : ", "")
                daftar_produk.add(nama)
    except FileNotFoundError:
        pass
    
    with open("datastok.txt", "a") as file:
        for p in produk:
            if p["Produk"] not in daftar_produk:
                file.write(f"Produk : {p['Produk']} -- Rp{p['harga']} || Stok : {p['Stok']}\n")
                daftar_produk.add(p['Produk'])
            
#######################################################################################
                                # 02 cek stok section

def bacastok(nama_file):
    daftar_stok = []
    with open(nama_file, "r") as file:
        for baris in file:
            baris = baris.strip()
            nama = baris.split(" -- ")[0].replace("Produk : ", "")
            sisa = baris.split(" -- ")[1] 
            harga = int(sisa.split("|| Stok : ")[0].replace("Rp", ""))
            stok = int(sisa.split("|| Stok : ")[1])
            
            produk_baru = {"Produk": nama, "harga": harga, "Stok": stok}
            daftar_stok.append(produk_baru)
    return daftar_stok
    
def cek_stok(produk):
    for p in produk:
        if p['Stok'] <= 5:
            print(F"{p['Produk']} tersisa {p['Stok']} item, mohon dipesan stok tambahan")
        elif p['Stok'] <= 10:
            print(F"{p['Produk']} tersisa {p['Stok']} item, jaga-jaga pesan stok tambahan")
        else:
            print(F"{p['Produk']} masih {p['Stok']} item, aman ae")

######################################################################################
                                # -- database section

def tulisdatabase_toko(produk):
    for p in produk:
        with open ("database_produk.txt", "a") as file:
            file.write(f" barang baru ==> Produk : {p['Produk']} -- Rp{p['harga']}|| Stok: {p['Stok']}\n")

def log_perubahan(nama_produk, field, nilai_lama, nilai_baru):
    with open("database_produk.txt", "a") as file:
        file.write(f"{nama_produk}: {field} diubah dari {nilai_lama} jadi {nilai_baru}\n")

######################################################################################
                                # c2 opsi 3.B section

def cari_produk(produk, nama_cari):
    for p in produk:
        if p["Produk"] == nama_cari:
            return p
    return None

def edit_stok(produk):
    nama_cari = input("Nama produk yang mau diedit: ")
    p = cari_produk(produk, nama_cari)
    
    if p is None:
        print("Produk tidak ditemukan!")
        return
    
    stok_lama = p["Stok"]
    stok_baru = int(input("Stok baru: "))
    p["Stok"] = stok_baru
    
    try:
        daftar_stok = set()
        with open("datastok.txt", "r") as file:
                for baris in file:
                    baris = baris.strip()
                    nama = baris.split(" -- ")[0].replace("Produk : ", "")
                    sisa = baris.split(" -- ")[1] 
                    harga = int(sisa.split("|| Stok : ")[0].replace("Rp", ""))
                    stok = int(sisa.split("|| Stok : ")[1])
                    daftar_stok.add(stok)
    except FileNotFoundError:
        pass

    with open("datastok.txt", "w") as file:
        for p  in produk:
            if p["Stok"] not in produk:
                file.write(f"Produk : {p['Produk']} -- Rp{p['harga']} || Stok : {p['Stok']}\n")
                daftar_stok.add(p['Stok'])

    log_perubahan(nama_cari, "Stok", stok_lama, stok_baru)


######################################################################################
                                # c3 opsi 3.C section

def edit_harga(produk):
    nama_cari = input("Nama produk yang mau diedit: ")
    p = cari_produk(produk, nama_cari)
    
    if p is None:
        print("Produk tidak ditemukan!")
        return
    
    harga_lama = p["harga"]
    harga_baru = int(input("harga baru: "))
    p["harga"] = harga_baru
    
    try:
        daftar_harga = set()
        daftar_harga2 = set()
        with open("datastok.txt", "r") as file:
                for baris in file:
                    baris = baris.strip()
                    nama = baris.split(" -- ")[0].replace("Produk : ", "")
                    sisa = baris.split(" -- ")[1] 
                    harga = int(sisa.split("|| Stok : ")[0].replace("Rp", ""))
                    stok = int(sisa.split("|| Stok : ")[1])
                    daftar_harga.add(harga)
    except FileNotFoundError:
        pass

    with open("datastok.txt", "w") as file:
        for p  in produk:
            if p["harga"] not in produk:
                file.write(f"Produk : {p['Produk']} -- Rp{p['harga']} || Stok : {p['Stok']}\n")
                daftar_harga.add(p['harga'])

    with open ("daftarProduk.txt", "w") as file:
        for p in produk:
            if p["harga"] not in produk:
                file.write(f"Produk : {p['Produk']} -- Rp{p['harga']}\n")
                daftar_harga2.add(p['harga'])

    log_perubahan(nama_cari, "harga", harga_lama, harga_baru)

######################################################################################
                                # menu section

def menu():
    produk = []

    while True:
        print("\n==== MENU ====")
        print("1. lihat daftar produk")
        print("2. cek stok produk")
        print("3. edit isi produk")
        print("4. setting")
        print("5. log out\n")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            bacadaftar_produk("daftarProduk.txt")
        elif pilihan == "2":
            cek = bacastok("datastok.txt")
            cek_stok(cek)
        elif pilihan == "3":
            option = input( "A. Tambah Produk"
                            "\nB. Edit Stok"
                            "\nC. Edit Harga"
                            "\n ")
            if option == "A":
                edit_produk(produk)
                tulisdatastok(produk)
                tulis_daftar(produk)
                tulisdatabase_toko(produk)
            elif option == "B":
                data = bacastok("datastok.txt")
                edit_stok(data)
            elif option == "C":
                dh = bacastok("datastok.txt")
                edit_harga(dh)

        elif pilihan == "4":
            print("==== SETTING ====")
            print("A. Ganti password\n"
                  "B. Ganti Akun")
            x = input("\n ")
            if x == "A":
                #password_Baru = getpass("password baru ")
                #valid = setting(password_Baru)
                #if valid:
                    #hide = enkripsi(password_Baru, 9)
                    #data_password(hide)
                print("sedang maintanace")
                pass
            elif x == "B":
                print("sedang maintanace")
                pass
                    
        elif pilihan == "5":
            print("log Out?")
            opsi = input("y/n ")
            if opsi == "y":
                break
            elif opsi == "n":
                pass
            else:
                print("????\n")
        else:
            print("invalid input")

####################################################################################
                                # login section

def cari_akun(daftar, unc):
    for x in daftar:
        if x["username"] == unc:
            return x
    return None

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
        valid = setting(password_akun_baru)
        if valid:
            break

    with open(namafile, "a") as file:
        file.write(f"username: {username_baru} || passwordLogin: {sembunyikan}\n")
    print("Akun berhasil dibuat!")
    
##################################l##################################################
                                # main section

def main():
    while True:
        un = input("Masukan username: ")
        daftar = baca_akun("datapwe.txt")
        akunfind = cari_akun(daftar, un)
        
        if akunfind is None:
            print("Username tidak ditemukan, silahkan buat akun.")
            regris_akun("datapw.txt")
        else:
            pw = getpass("Masukan password: ")
            sembunyikan = enkripsi(pw, 9)

            if sembunyikan == akunfind["passwordLogin"]:
                print("Login berhasil!")
                menu()
                break
            else:
                print("Password salah!")
                
main()