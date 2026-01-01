import math

def volume_kubus(s):
    return s ** 3

def volume_balok(p, l, t):
    return p * l * t

def volume_prisma_segitiga(a, ts, tp):
    return 0.5 * a * ts * tp

def volume_tabung(r, t):
    return math.pi * r * r * t

def volume_kerucut(r, t):
    return (1/3) * math.pi * r * r * t

def volume_bola(r):
    return (4/3) * math.pi * r ** 3

def volume_limas_segiempat(s, t):
    return (1/3) * s * s * t

def volume_prisma_segiempat(p, l, t):
    return p * l * t

def volume_setengah_bola(r):
    return (2/3) * math.pi * r ** 3

def volume_kerucut_terpancung(R, r, t):
    return (1/3) * math.pi * t * (R*R + R*r + r*r)