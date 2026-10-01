import socket
import threading



def port_scanner(target, port): #function scanner
    lock = threading.Lock()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hasil = sock.connect_ex((target, port))   # ini tetap pakai connect_ex, method asli
    sock.close()
    if hasil == 0:
        status = f"Port {port} TERBUKA"
        with lock:
           print(status)
    else:
        status = f"port {port} TERTUTUP"
        with lock:
            print(status)

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

    threads = []

    for i in range (port_awal, port_akhir + 1):
        t = threading.Thread(target=port_scanner, args=(target, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

        
main() 