from utils6 import hitung_total, hitung_pajak, total_setelah_pajak


input_harga = input("Masukkan Daftar Harga Barang yang dibeli: ")
daftar_harga = list(map(int, input_harga.split()))

total = hitung_total(daftar_harga)
pajak = hitung_pajak(total)
total_akhir = total_setelah_pajak(total, pajak)

print("Total Pembayaran:", total)
print("Pajak:", pajak)
print("Total Pembayaran Setelah Pajak:", total_akhir)