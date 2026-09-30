def log_perubahan(nama_produk, field, nilai_lama, nilai_baru):
    with open("database_produktest.txt", "a") as file:
        file.write(f"{nama_produk}: {field} diubah dari {nilai_lama} jadi {nilai_baru}\n")

def cari_produk(produk, nama_cari):
    for p in produk:
        if p["Produk"] == nama_cari:
            return p
    return

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
        with open("datastoktest.txt", "r") as file:
                for baris in file:
                    baris = baris.strip()
                    nama = baris.split(" -- ")[0].replace("Produk : ", "")
                    sisa = baris.split(" -- ")[1] 
                    harga = int(sisa.split("|| Stok : ")[0].replace("Rp", ""))
                    stok = int(sisa.split("|| Stok : ")[1])
                    daftar_stok.add(stok)
    except FileNotFoundError:
        pass

    with open("datastoktest.txt", "w") as file:
        for p  in produk:
            if p["Stok"] not in produk:
                file.write(f"Produk : {p['Produk']} -- Rp{p['harga']} || Stok : {p['Stok']}\n")
                daftar_stok.add(p['Stok'])

    log_perubahan(nama_cari, "Stok", stok_lama, stok_baru)
    
def main():
    testbaca = bacastok("datastoktest.txt")
    edit_stok(testbaca)
main()