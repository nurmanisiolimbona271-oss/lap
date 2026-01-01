from utils9 import hitung_rata_rata

jumlah_mahasiswa = int(input("Masukkan Jumlah Mahasiswa: "))

for i in range(1, jumlah_mahasiswa + 1):
    nilai = list(map(int, input(f"Masukkan Nilai Mahasiswa {i}: ").split()))
    rata_rata = hitung_rata_rata(nilai)
    print(f"Rata - Rata Nilai Mahasiswa {i}: {rata_rata}")