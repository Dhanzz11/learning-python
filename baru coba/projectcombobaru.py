######################################################################################
                                # produk section

def setting (password):
    kriteria1 = len(password) == 8
    kriteria2 = any(c.isupper() for c in password)
    kriteria3 = any(c.isdigit() for c in password)
    jumlah_Kriteria = sum([kriteria1, kriteria2, kriteria3])

    if jumlah_Kriteria == 3:
        return "Password sudah diganti"
    else:
        return "silahkan penuhi kriteria ini (password harus memiliki 8 karakter, huruf besar dan huruf kecil)"

def data_password(password):
    with open ("datapw.txt", "w") as file:
        file.write(f"Password: {password}")

def tulis_daftar(produk):
    daftar_produk = set()
    try:
        with open("daftarProduk.txt", "r") as file:
            for baris in file:
                nama = baris.split(" -- ")[0].replace("Produk: ", "")
                daftar_produk.add(nama)
    except FileNotFoundError:
        pass
    
    with open("daftarProduk.txt", "a") as file:
        for p in produk:
            if p["Produk"] not in daftar_produk:
                file.write(f"Produk : {p['nama']} -- Rp{p['harga']}\n")
                daftar_produk.add(p["Produk"])

def tulisdatabase_toko(produk):
    for p in produk:
        with open ("database_produk.txt", "a") as file:
            file.write(f"Produk : {p['nama']} -- Rp{p['harga']}|| Stok: {p['stok']}\n")

def bacadatabase_toko(produk):
    with open (produk, "r") as file:
        isi = file.read()
        print(isi)

def bacadaftar_produk(produk):
    with open ("database_produk.txt" , "r") as file:
       daftar = file.read()
       return eval(daftar)

def edit_produk(produk):
    nama = input("Produk tambahan: ")
    harga = int(input("harga: "))
    stok = int(input("banyak stok produk: "))
    produk_baru = {"Produk" : nama, "harga" : harga, "Stok" : stok}
    produk.append(produk_baru)

def cek_stok(produk):
    for p in produk:
        if p['stok'] < 10:
            print(F"{p['Produk']} tersisa {p['Stok']} item, mohon dipesan stok tambahan")
        elif p['stok']< 5:
            print(F"{p['Produk']} tersisa {p['Stok']} item, segera pesan stock tambahan")
        else:
            print(F"{p['Produk']} masih {p['Stok']} item, aman ae")

def menu():
    produk = []

    while True:
        print("==== MENU ====")
        print("1. lihat daftar produk")
        print("2. cek stok produk")
        print("3. edit isi produk")
        print("4. setting")
        print("5. log out\n")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            bacadaftar_produk(produk)
        elif pilihan == "2":
            cek = bacadaftar_produk(produk)
            cek_stok(cek)
        elif pilihan == "3":
            edit_produk(produk)
            bacadaftar_produk(produk)
            tulis_daftar(produk)
        elif pilihan == "4":
            print("==== SETTING ====")
            print("A. Ganti password")
            x = input(" ")
            if x == "A":
                password = input("password baru ")
                setting(password)
        elif pilihan == "5":
            print("log Out?")
            opsi = input("y/n ")
            if opsi == "y":
                break
            elif opsi == "n":
                pass
            else:
                print("????")
        else:
            print("invalid input")

####################################################################################
                                # setting section

####################################################################################
                                # main section

menu()