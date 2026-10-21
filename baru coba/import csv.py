import csv
protocol= set()

with open("enp0s3-pvt-wednesday.pcap_Flow.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for nomor, x in enumerate(reader, start=1):
        angka = int(x['Protocol'])
        protocol.add(angka)
    print(sorted(protocol))