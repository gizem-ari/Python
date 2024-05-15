# Decimal to binary and binary to decimal

print("     HOS GELDINIZ!!!")
menu = 1
while menu == 1 or menu == 2 or menu == 3:
    print("\n\n1] İkilik tabandan onluk tabana cevirme islemi\n"
          "2] Onluk tabandan ikilik tabana cevirme islemi\n"
          "3] CIKIS")
    menu = int(input("Lutfen yapmak istediginiz islemi secin:"))
    onluk_sayi = 0

    if menu == 1:  # İkilik tabandan onluk tabana cevirme
        gecerli_mi = 1
        sayi = int(input("Lutfen ikilik tabana uygun bir sayi giriniz!(0,1):"))
        sayi9 = sayi
        while sayi9 != 0:
            kalan9 = sayi9 % 10
            sayi9 = sayi9 // 10
            if kalan9 != 0 and kalan9 != 1:
                print("hatali sayi girdiniz !")
                sayi = int(input("lutfen ikilik tabanda bir sayi giriniz:"))
                sayi9 = sayi

        basamak_sayi = 0
        sayi = str(sayi)
        for _ in sayi:
            basamak_sayi += 1

        for i in sayi:
            if i == "1" or i == "0":
                i = int(i)
                onluk_sayi = onluk_sayi + i * 2 ** (basamak_sayi - 1)
                basamak_sayi = basamak_sayi - 1

            else:
                print("\nLutfen gecerli bir sayi giriniz!!(0/1 formatında)\n")
                gecerli_mi = 0
                break
        if gecerli_mi == 1:
            print("Onluk tabana cevrilmis hali:", onluk_sayi)

    elif menu == 2:  # onluk tabandan ikilik tabana cevirme
        sayi = int(input("Lutfen onluk tabana uygun bir sayi giriniz:"))
        print("ikilik tabana cevrilen sayi:")
        sayi2 = ''
        while sayi != 0:
            kalan = sayi % 2
            sayi = sayi // 2
            kalan = str(kalan)
            sayi2 = kalan + str(sayi2)
        print(sayi2)

    elif menu == 3:
        print("CIKIS ISLEMI YAPILIYOR!")
        menu = 0  # while döngüsünden cikmak icin 0'a esitledim
    else:
        print("Lutfen gecerli bir sayi giriniz!!(1/2/3)")
        menu = 1
