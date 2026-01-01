def hitung_total(harga_list):
    """
    Menghitung total dari daftar harga barang.
    """
    total = 0
    for harga in harga_list:
        total += harga
    return total