from getpass import getpass

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

def data_password(hasil):
    with open ("datapwe.txt", "w") as file:
        file.write(f"passwordLogin: {hasil}")

def hasilen(passen):
    with open(passen, "r") as file:
        for isi in file:
            pw = isi.split(" : ")[0].replace("passwordLogin: ", "")
        return pw

def main():
    password= getpass("Masukan Password: ")
    geser = 9
    sembunyikan = enkripsi(password, geser)
    #lagi1 = enkripsi(sembunyikan, geser)
    #lagi2 = enkripsi(lagi1, geser)
    dataasli = hasilen("datapwe.txt")
    if sembunyikan == dataasli:
        print("Hebat euy dah komplek")
    else:
        print("yahahaha gagal")

main()