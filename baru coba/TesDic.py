import csv

def time(mikro):
    waktu = float(mikro)
    detik = waktu/1000000
    timeNew= round(detik)
    return timeNew

def main():
    with open("enp0s3-pvt-wednesday.pcap_Flow.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for nomor, x in enumerate(reader, start=1):
            waktuInteraksi=time(x["Flow Duration"])
            print(f"{nomor} {waktuInteraksi} Detik")
            if nomor == 5:
                break
            

main()       