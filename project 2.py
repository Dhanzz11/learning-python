import socket

def port_scanner(target, port): #function scanner

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hasil = sock.connect_ex((target, port))   # ini tetap pakai connect_ex, method asli
        sock.close()
        if hasil == 0:
            return f"Port {port} TERBUKA"
        else:
            return f"port {port} TERTUTUP"

def simpan_scanner (port, hasil): #function pencatat
    if "TERBUKA" in hasil:
        with open ("scanner.txt", "a") as file:
            file.write (f"port: {port} hasil: {hasil}")
        with open ("scanner.txt", "r") as file:
            isi_data = file.read()
            print(isi_data)

def main():
    target = input("Masukan ip : ")
    port_awal = int(input("Masukan batas awal : "))
    port_akhir = int(input("masukan batas akhir : "))

    for i in range (port_awal, port_akhir + 1):
        hasil = port_scanner(target, i)
        simpan_scanner(i, hasil)
        print(hasil)
        
main() 