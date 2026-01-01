import os
from bangun_ruang import *

while True:
    print("=== MENU VOLUME BANGUN RUANG ===")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Tabung")
    print("5. Kerucut")
    print("6. Bola")
    print("7. Limas Segiempat")
    print("8. Prisma Segiempat")
    print("9. Setengah Bola")
    print("10. Kerucut Terpancung")
    print("0. Keluar")

    pil = int(input("Masukkan pilihan: "))

    if pil == 1:
        s = int(input("Masukkan sisi: "))
        print("Volume kubus =", volume_kubus(s))

    elif pil == 2:
        p = int(input("Masukkan panjang: "))
        l = int(input("Masukkan lebar: "))
        t = int(input("Masukkan tinggi: "))
        print("Volume balok =", volume_balok(p, l, t))

    elif pil == 3:
        a = int(input("Masukkan alas segitiga: "))
        ts = int(input("Masukkan tinggi segitiga: "))
        tp = int(input("Masukkan tinggi prisma: "))
        print("Volume prisma segitiga =", volume_prisma_segitiga(a, ts, tp))

    elif pil == 4:
        r = int(input("Masukkan jari-jari: "))
        t = int(input("Masukkan tinggi: "))
        print("Volume tabung =", volume_tabung(r, t))

    elif pil == 5:
        r = int(input("Masukkan jari-jari: "))
        t = int(input("Masukkan tinggi: "))
        print("Volume kerucut =", volume_kerucut(r, t))

    elif pil == 6:
        r = int(input("Masukkan jari-jari: "))
        print("Volume bola =", volume_bola(r))

    elif pil == 7:
        s = int(input("Masukkan sisi alas: "))
        t = int(input("Masukkan tinggi limas: "))
        print("Volume limas segiempat =", volume_limas_segiempat(s, t))

    elif pil == 8:
        p = int(input("Masukkan panjang alas: "))
        l = int(input("Masukkan lebar alas: "))
        t = int(input("Masukkan tinggi prisma: "))
        print("Volume prisma segiempat =", volume_prisma_segiempat(p, l, t))

    elif pil == 9:
        r = int(input("Masukkan jari-jari: "))
        print("Volume setengah bola =", volume_setengah_bola(r))

    elif pil == 10:
        R = int(input("Masukkan jari-jari besar: "))
        r = int(input("Masukkan jari-jari kecil: "))
        t = int(input("Masukkan tinggi: "))
        print("Volume kerucut terpancung =", volume_kerucut_terpancung(R, r, t))

    elif pil == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")

    input("\nTekan Enter untuk lanjut...")
    os.system("clear")  