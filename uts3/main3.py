from utils3 import hitung_rata_rata, cek_kelulusan
 
nilai_input = input("Masukkan Daftar Nilai Tugas Mahasiswa: ")
nilai_list = list(map(int, nilai_input.split()))

standar = int(input("Masukkan Standar Kelulusan: "))


rata_rata = hitung_rata_rata(nilai_list)
keterangan = cek_kelulusan(rata_rata, standar)

print("Nilai Rata - Rata:", rata_rata)
print("Keterangan:", keterangan)