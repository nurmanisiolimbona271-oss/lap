from utils8 import hitung_total

jumlah_konsumen = int(input("Masukkan Jumlah Konsumen: "))

for i in range(1, jumlah_konsumen + 1):
    data = input(
        f"Masukkan Harga Barang yang dibeli Konsumen {i}: "
    )

    # ubah input string menjadi list integer
    harga_barang = list(map(int, data.split()))

    total_pembayaran = hitung_total(harga_barang)

    print(f"Total Pembayaran Konsumen {i}: {total_pembayaran}")