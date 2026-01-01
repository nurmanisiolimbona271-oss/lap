from utils4 import hitung_total, hitung_diskon, hitung_total_setelah_diskon

harga_input = input("Masukkan Daftar Harga Barang yang dibeli: ")
harga_list = list(map(int, harga_input.split()))

total = hitung_total(harga_list)
diskon = hitung_diskon(total)
total_akhir = hitung_total_setelah_diskon(total, diskon)

print("Total Pembayaran:", total)
print("Diskon:", diskon)
print("Total Pembayaran Setelah Diskon:", total_akhir)