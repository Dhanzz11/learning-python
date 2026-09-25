######################################################################################
                                # toko section

def tulisdatabase_toko(produk):
    daftar_produk = set()
    try:
        with open("database_produk.txt", "r") as file:
            for baris in file:
                nama = baris.split(" -- ")[0].replace("Produk: ", "")
                daftar_produk.add(nama)
    except FileNotFoundError:
        pass

    with open("database_produk.txt", "a") as file:
        for p in produk:
            if p["nama"] not in daftar_produk:
                file.write(f"nama: {p['nama']} harga: {p['harga']} stok: {p['stok']}\n")
                daftar_produk.add(p["nama"])

def bacadatabase_toko(produk):
    with open (produk , "r") as file:
        isi_produk = file.read()
        print (isi_produk)

def edit_produk(produk):
    nama = input("Produk tambahan: ")
    harga = int(input("harga: "))
    stok = int(input("banyak stok produk: "))
    produk_baru = {"nama": nama, "harga": harga, "stok": stok}
    produk.append(produk_baru)

def cek_stok(produk):
    for p in produk:
        if p["'stock"] < 10:
            print(F"{p['nama']} tersisa {p['stok']} item, mohon dipesan stok tambahan")
        elif p["'stock"]< 5:
            print(F"{p['nama']} tersisa {p['stok']} item, segera pesan stock tambahan")
        else:
            print(F"{p['nama']} masih {p['stok']} item, aman ae")

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
            bacadatabase_toko("database_produk.txt")
        elif pilihan == "2":
            pass
        elif pilihan == "3":
            edit_produk(produk)
            tulisdatabase_toko(produk)
            pass
        elif pilihan == "4":
            pass
        elif pilihan == "5":
            pass
        elif pilihan == "5":
           pass
        else:
            pass

####################################################################################
                                # setting section
def data_pw(enkrip):
    with open ("datapwmasuk.txt", "a") as file:
        file.write (f"pw: {enkrip}")











####################################################################################
                                # main section

menu()