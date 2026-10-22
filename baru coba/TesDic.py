import csv

def measure(byte):
    angka = float(byte)
    MB = 1_000_000
    KB = 1_000
    if angka < KB:
        return f"{round(angka)} Byte"
    elif angka < MB:
        return f"{round(angka/1000, 1)} KB"
    else:
        return f"{round(angka/1000000, 1)} MB"
    
def main():
    with open("enp0s3-pvt-wednesday.pcap_Flow.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for nomor, x in enumerate(reader, start=1):
            ukuran = measure(x["Total Length of Fwd Packet"])
            ukuran2 = measure(x["Total Length of Bwd Packet"])
            print(f"{nomor} {ukuran} dikirim | {ukuran2} diterima")
            if nomor == 10:
                break
            

main()       