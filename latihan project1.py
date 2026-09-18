def tambah_produk(produk):
    nama = input("Produk tambahan: ")
    harga = int(input("harga: "))
    stok = int(input("banyak stok produk: "))
    produk_baru = {"nama": nama, "harga": harga, "stok": stok}
    produk.append(produk_baru)

def tampilkan_produk(produk):
    for nomor, p in enumerate(produk, start=1):
        print(f"{nomor}. {p['nama']}  - {p['harga']} (stok: {p['stok']})")


def cek_stok_rendah(produk):
    for p in produk:
        if p ["stok"] < 5:
           print(f"{p['nama']} tersisa {p['stok']} item, segera pesan stok tambahan")
        else:
           print("semua aman")


def simpan_ke_file(produk):
    with open("stock.txt", "a") as file:
        for p in produk:
            file.write(f"nama: {p['nama']} harga: {p['harga']} stok: {p['stok']}\n")
    with open ("stock.txt", "r") as file:
        isi_data = file.read()
        print(isi_data)

    

def main():
    produk = []
    
    while True:
        print("=== MENU INVENTARIS ===")
        print("1. Tambah produk")
        print("2. Lihat semua produk")
        print("3. Cek stok rendah")
        print("4. Simpan ke file")
        print("5. Keluar\n")
        pilihan = input("Pilih menu: \n")

        if pilihan == "1":
            tambah_produk(produk)
            break
        elif pilihan == "2":
            tampilkan_produk(produk)
            break
        elif pilihan == "3":
            cek_stok_rendah(produk)
            break
        elif pilihan == "4":
            simpan_ke_file(produk)
            break
        elif pilihan == "5":
            print("Alr, BYE MATE")
            break
        else:
            print("Pilihan tidak valid")
            

main()