from getpass import getpass
######################################################################################
                                # encryptioan section

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
                                # setting section

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
                                # opsi 3 section

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

def bacadaftar_produk(produk):
    with open (produk , "r") as file:
       daftar = file.read()
       print(daftar)


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
            
######################################################################################
                                # cek stok section

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
            print(F"\n{p['Produk']} tersisa {p['Stok']} item, mohon dipesan stok tambahan")
        elif p['Stok'] <= 10:
            print(F"\n{p['Produk']} tersisa {p['Stok']} item, jaga-jaga pesan stok tambahan")
        else:
            print(F"\n{p['Produk']} masih {p['Stok']} item, aman ae\n")

######################################################################################
                                # database section

def tulisdatabase_toko(produk):
    for p in produk:
        with open ("database_produk.txt", "a") as file:
            file.write(f" log ==> Produk : {p['Produk']} -- Rp{p['harga']}|| Stok: {p['Stok']}\n")

######################################################################################
                                # menu section

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
            bacadaftar_produk("daftarProduk.txt")
        elif pilihan == "2":
            cek = bacastok("datastok.txt")
            cek_stok(cek)
        elif pilihan == "3":
            edit_produk(produk)
            tulisdatabase_toko(produk)
            tulisdatastok(produk)
            tulis_daftar(produk)
        elif pilihan == "4":
            print("==== SETTING ====")
            print("A. Ganti password")
            x = input(" ")
            if x == "A":
                password_Baru = getpass("password baru ")
                valid = setting(password_Baru)
                if valid:
                    hide = enkripsi(password_Baru, 9)
                    data_password(hide)
                    
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

def data_pw(datapw):
    with open(datapw, "r") as file:
        for isi in file:
            pw = isi.split(" : ")[0].replace("passwordLogin: ", "")
        return pw
    
def login(password):
    sembunyikan = enkripsi(password, 9)
    data = data_pw("datapw.txt")
    if sembunyikan == data:
        masuk = menu()
        return masuk
    else:
        print("Wer bist du, Eindringling??")
####################################################################################
                                # main section

def main():
    password = getpass("masukan password login: ")
    login(password)


main()