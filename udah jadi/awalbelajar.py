def cek_Umur(nama, umur):
    if umur >= 18:
        return f"{nama} sudah dewasa"
    else:
        return f"{nama} masih kecil"

Orang = [
    {"nama": "Aprilia","umur": 20},
    {"nama": "Rose", "umur": 19},
    {"nama": "Sarah", "umur": 16},
]

for orang_ini in Orang:
    hasil = cek_Umur(orang_ini["nama"], orang_ini["umur"])
    print(hasil)

   