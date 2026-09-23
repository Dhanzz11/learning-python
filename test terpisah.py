def check_bug(password, geser):
    x = ""
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
hasil = check_bug("Narendra", 3)
print(hasil)