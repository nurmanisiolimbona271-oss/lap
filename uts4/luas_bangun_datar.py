
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
    
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def luas_segitiga(alas, tinggi):
    luas =  0.5 * alas * tinggi
    return luas

def luas_lingkaran(jari_jari):
    luas =  math.pi * jari_jari ** 2
    return luas

def luas_jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    return luas

def luas_trapesium(sisi_sejajar_a, sisi_sejajar_b, tinggi):
    luas = 0.5 * (sisi_sejajar_a + sisi_sejajar_b) * tinggi
    return luas

def luas_belah_ketupat(diagonal1, diagonal2):
    luas = 0.5 * diagonal1 * diagonal2
    return luas

def luas_layang_layang(diagonal1, diagonal2):
    luas = 0.5 * diagonal1 * diagonal2
    return luas
    
def luas_juring_lingkaran(jari_jari, sudut):
    """
    sudut dalam derajat
    """
    luas = (sudut / 360) * math.pi * jari_jari ** 2
    return luas

def luas_setengah_lingkaran(jari_jari):
    luas = 0.5 * math.pi * jari_jari ** 2
    return luas