def data_pw(datapw):
    with open(datapw, "r") as file:
        isi_data=file.read()
    return isi_data

password = input("masukan password: ")
data = data_pw("datapw.txt")
if data == password:
    print ("selamat datang puq")
else:
   print("ah mau apanya kau?")