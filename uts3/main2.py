from utils2 import parse_list, total_pembayaran

data = input("Masukkan Daftar Harga Barang yang dibeli: ")

data = parse_list(data)

total = total_pembayaran(data)

print("Total Pembayaran:", total)