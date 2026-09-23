def check_password(password):
    kriteria1 = len(password)==8
    kriteria2 = kriteria1 = len(password) == 8
    kriteria2 = any(c.isupper() for c in password)
    kriteria3 = any(c.isdigit() for c in password)
    jumlah_Kriteria = sum([kriteria1, kriteria2, kriteria3])

    if jumlah_Kriteria == 3:
        return "Password berkeamanan Kuat"
    elif jumlah_Kriteria == 2:
        return "Password berkeamanan sedang"
    else:
        return "Password berkeamanan lemah"
    
def enkripsi_pw(password, geser):
    x =""
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
            x = x + huruf_baru
        return x

def log_pw(password, engkep):
    with open ("logPassword.txt", "a") as file:
        file.write(f"Password: {password} disembunyikan:{engkep}\n")
    with open("logPassword.txt", "r") as file:
        isi_log = file.read()
        print(isi_log)

def main(): #executor utama
    password= input("Masukan Password (usahakan berisi 8 character, kombinasi angka dan huruf besar): ")
    hasil = check_password(password)
    geser = 3
    sembunyikan = enkripsi_pw(password, geser)
    log_pw(password, sembunyikan)
    print(f"==> {hasil}")

main()