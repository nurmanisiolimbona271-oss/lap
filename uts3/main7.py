from utils7 import pembulatan

bilangan = float(input("Masukkan Bilangan Desimal: "))
digit = int(input("Masukkan Jumlah Digit: "))

hasil = pembulatan(bilangan, digit)
print(hasil)