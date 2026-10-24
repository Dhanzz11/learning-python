import csv

layanan = {
        0:"Protocol(Bukan Port)", 
        22:"SSH", 
        53:"DNS", 
        67:"DHCP", 
        80:"HTTP", 
        123:"NTP", 
        443:"HTTPS", 
        5353:"mDNS", 
        8000:"Web Aplikasi", 
        8081:"Web Aplikasi", 
        8662:"Belum Dipastikan", 
        9000:"Belum Dipastikan", 
        9200:"Elasticsearch(dugaan)"
        }

protcl = {
        0:"lainnya", 
        6:"TCP", 
        17:"UDP"}

def jenis_Ip(ip):
    IP = ip.split('.')
    bagian1 = int(IP[0])
    bagian2 = int(IP[1])
    if bagian1 == 10:
        return "dalam"
    elif bagian1 == 192 and bagian2 == 168:
        return "dalam"
    elif bagian1 == 172 and bagian2 >= 16 and bagian2 <= 31:
        return "dalam"
    elif bagian1 == 0 or bagian1 == 255:
        return "khusus"
    elif 224 <= bagian1 <= 239:
        return "khusus"
    else :
        return "luar"

def nama_Layanan(portdst, portsrc):
    dst = int(portdst)
    src = int(portsrc)
    if dst in layanan:
        return layanan.get(dst)
    elif src in layanan:
        return layanan.get(src)
    else:
        return "Port Sementara"

def nama_Protocol(angka):
    return protcl.get(int(angka), "???")

def waktu(mikro):
    second = 1000000
    milsec = 1000
    flowDuration = float(mikro)
    if flowDuration < second:
        convertToSec = flowDuration/milsec
        time = round(convertToSec, 3)
        tipeTime = "Milidetik"
    else:
        convertToSec = flowDuration/second
        time = round(convertToSec, 3)
        tipeTime = "Detik"
    return f"{time} {tipeTime}"

def banyak_Data(byte):
    angka = float(byte)
    KB = 1_000
    MB = 1_000_000
    if angka < KB:
        return f"{round(angka)} Byte"
    elif angka < MB:
        return f"{round(angka/KB, 1)} KB"
    else:
        return f"{round(angka/MB, 1)} MB"

def kalimat(x):
    bagian = x["Timestamp"].split(" ")
    jam = bagian[1] + " " + bagian[2]

    sumber = jenis_Ip(x["Src IP"])
    tujuan = jenis_Ip(x["Dst IP"])
    LAYANAN = nama_Layanan(x["Dst Port"], x["Src Port"])
    cara = nama_Protocol(x["Protocol"])
    waktuInteraksi = waktu(x["Flow Duration"])
    dataDikirim = banyak_Data(x["Total Length of Fwd Packet"])
    dataDiterima = banyak_Data(x["Total Length of Bwd Packet"])

    kalimat = (f"{jam}, {x['Src IP']} ({sumber}) ===>> {x['Dst IP']} ({tujuan}), "
               f"Melalui {LAYANAN} ({cara}), selama {waktuInteraksi}, "
               f"Mengirim {dataDikirim} dan menerima {dataDiterima}.")

    if x["Stage"] != "Benign":
        kalimat = kalimat + f"[{x['Activity']} - {x['Stage']}]"

    return kalimat

def main():
    hitung_Stage = {}
    with open("enp0s3-pvt-wednesday.pcap_Flow.csv", "r", newline="") as file:
        with open("skrip.txt", "w", encoding="utf-8") as skrip:
            reader = csv.DictReader(file)
            for nomor, y in enumerate(reader, start=1):
                stage = y["Stage"]
                hitung_Stage[stage] = hitung_Stage.get(stage, 0) + 1
                if y["Stage"] != "Benign":
                    skrip.write(f"{nomor} {kalimat(y)}\n")
    for nama, jumlah in hitung_Stage.items():
        print(nama, jumlah)

main()