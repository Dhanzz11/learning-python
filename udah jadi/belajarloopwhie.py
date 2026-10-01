while True:
    print("1. Pilih makanan")
    print("2.Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        while True:
            print("==== MAKAN ====")
            print("1. Nasi Gonning")
            print("2. Mie Goth Mommy")
            print("===============")
            print("==== MINUM ====")
            print("3. Es Teh Ketek Mommy")
            print("4. Susu Segar Mommy")
            sub_p = input("Pilih Makan: ")

            if sub_p == "1":
                sub_pm = input("Pilih Minum: ")
                if sub_pm == "3":
                    print(f"menu Nasi Gonning dan Es Teh Ketek Mommy sedang disiapkan")
                    break
                elif sub_pm == "4":
                    print(f"menu Nasi Gonning dan Susu Segar Mommy sedang disiapkan")
                    break
                else:
                    print("Pilih minuman yang ada")
                break
            elif sub_p == "2":
                sub_pm = input("Pilih Minum: ")
                if sub_pm == "3":
                    print(f"menu Mie Goth Mommy dan Es Teh Ketek Mommy sedang disiapkan")
                    break
                elif sub_pm == "4":
                    print(f"menu Mie Goth Mommy dan Es Teh Ketek Mommy sedang disiapkan")
                    break
                else:
                    print("Pilih minuman yang ada")
            else:
                print("pilih makanan yang ada")


    elif pilihan == "2":
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid")