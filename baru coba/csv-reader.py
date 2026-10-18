import csv



def jenisIp(ip):
    IP = ip.split('.')
    bagian1 = int(IP[0])
    bagian2 = int(IP[1])
    return bagian1, bagian2
    


def main():
    with open("enp0s3-pvt-wednesday.pcap_Flow.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for nomor, x in enumerate(reader, start=1):
            sumber = jenisIp(x["Src IP"])
            tujuan = jenisIp(x["Dst IP"])
            if sumber[1] and tujuan[1] == 10 or sumber[0] == 192 and sumber[1] or tujuan[0] == 172 and tujuan [1] <= 16 and tujuan[1] >= 31:
                tujuan = "dalam"
                sumber = "dalam"
            else:
                tujuan = "luar"
                sumber = "luar"
            print(nomor, sumber, "->", tujuan)
            if nomor == 5:
                break

main()
