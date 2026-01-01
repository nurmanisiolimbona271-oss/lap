def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)


def cek_kelulusan(rata_rata, standar):
    if rata_rata >= standar:
        return "Lulus"
    else:
        return "Tidak Lulus"