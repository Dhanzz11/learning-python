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

def data_pw(datapw):
    with open(datapw, "r") as file:
        for isi in file:
            pw = isi.split(" : ")[0].replace("passwordLogin: ", "")
        return pw


password = input("masukan password: ")
data = data_pw("datapw.txt")
if data == password:
    hasil = menu()
    print(hasil)
else:
    print("ah mau apanya kau?")