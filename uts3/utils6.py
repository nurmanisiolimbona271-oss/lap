def hitung_total(daftar_harga):
    return sum(daftar_harga)


def hitung_pajak(total, batas=50000, persen=0.01):
    if total > batas:
        return total * persen
    else:
        return 0


def total_setelah_pajak(total, pajak):
    return total + pajak