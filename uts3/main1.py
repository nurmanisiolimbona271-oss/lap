from utils1 import menghitung_nilai_terbesar, menghitung_nilai_terkecil, parse_list

data = input("Masukkan Beberapa Nilai: ")

data = parse_list(data)

nilai_terbesar = menghitung_nilai_terbesar(data)
nilai_terkecil = menghitung_nilai_terkecil(data)

print("Nilai Terbesar:", nilai_terbesar)
print("Nilai Terkecil:", nilai_terkecil)
