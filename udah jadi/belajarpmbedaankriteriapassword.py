def cek_kekuatanPassword (password): #function mengecek password
    kriteria1 = len(password) == 8
    kriteria2 = any(c.isupper() for c in password)
    kriteria3 = any(c.isdigit() for c in password)
    jumlah_Kriteria = sum([kriteria1, kriteria2, kriteria3])

    if jumlah_Kriteria == 3:
        return "Password berkeamanan Kuat"
    elif jumlah_Kriteria == 2:
        return "Password berkeamanan sedang"
    else:
       return "Password berkeamanan lemah"

def log_password (password, hasil): #function memasukan data ke file txt
    with open ("password_log.txt", "a") as file:
        file.write(f"Password : {password} hasil : {hasil}\n")
    with open ("password_log.txt", "r") as file:
        isi_log = file.read()
        print(isi_log)

def main(): #executor utama
    password= input("Masukan Password (usahakan berisi 8 character, kombinasi angka dan huruf besar): ")
    hasil = cek_kekuatanPassword(password)
    print(f"==> {hasil}")

    log_password(password, hasil)

main()
