def data_pw(datapw):
    passw = set()
    with open(datapw, "r") as file:
        for isi in file:
            pw = isi.split(" : ")[0].replace("Password: ", "")
        return pw

password = input("masukan password: ")
data = data_pw("datapw.txt")
if data == password:
    print ("selamat datang puq")
else:
    print("ah mau apanya kau?")