def tambah_produk(produk):
    nama = input("Produk tambahan: ")
    harga = int(input("harga: "))
    stok = int(input("banyak stok produk: "))

    produk_baru = {"nama": {nama}, "harga": {harga}, "stok": {stok}}

    produk.append(produk_baru)


def tampilkan_produk(produk):
    produk = [
        {"nama": "Ekor Furry", "harga": 20000, "stok": 6}
    ]

def cek_stok_rendah(nama, stok):
    if stok < 5:
        return f"{nama} tersisa {stok} item, segera pesan stok tambahan"
    else:
        return f"{nama} stoknya aman"


def simpan_ke_file(nama, harga, stok):
    with open("stock.txt", "a") as file:
        file.write(f"nama: {nama} harga: {harga} stok: {stok} ")
    with open("stok.txt", "r") as file:
        data_produk = file.read()
        print(data_produk)
    

def main():
    produk = []
    
    while True:
        print("=== MENU INVENTARIS ===")
        print("1. Tambah produk")
        print("2. Lihat semua produk")
        print("3. Cek stok rendah")
        print("4. Simpan ke file")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_produk(produk)
        elif pilihan == "2":
            tampilkan_produk(produk)
        elif pilihan == "3":
            cek_stok_rendah(nama, stok)
        elif pilihan == "4":
            simpan_ke_file(nama, harga, stok)
        elif pilihan == "5":
            print("Alr, BYE MATE")
            break
        else:
            print("Pilihan tidak valid")
            

main()