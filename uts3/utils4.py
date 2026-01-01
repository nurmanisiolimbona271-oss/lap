def hitung_total(harga_list):
    return sum(harga_list)


def hitung_diskon(total):
    # Diskon 10%
    return total * 0.10


def hitung_total_setelah_diskon(total, diskon):
    return total - diskon