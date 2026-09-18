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
    produk_tersimpan = set()

    # Baca data yang sudah ada
    try:
        with open("stock.txt", "r") as file:
            for baris in file:
                if baris.startswith("nama:"):
                    nama = baris.split(" harga:")[0].replace("nama: ", "")
                    produk_tersimpan.add(nama)
    except FileNotFoundError:
        pass

    # Tambahkan produk yang belum ada
    with open("stock.txt", "a") as file:
        for p in produk:
            if p["nama"] not in produk_tersimpan:
                file.write(
                    f"nama: {p['nama']} harga: {p['harga']} stok: {p['stok']}\n"
                )
                produk_tersimpan.add(p["nama"])

    # Tampilkan isi file
    with open("stock.txt", "r") as file:
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
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_produk(produk)
        elif pilihan == "2":
            tampilkan_produk(produk)
        elif pilihan == "3":
            cek_stok_rendah(produk)
        elif pilihan == "4":
            simpan_ke_file(produk)
        elif pilihan == "5":
            print("Alr, BYE MATE")
            break
        else:
            print("Pilihan tidak valid")
            

main()