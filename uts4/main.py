import os 
from luas_bangun_datar import *

while True:
	os.system("clear")
	
	pil = int(input("pilihan : "))
	
	if pil == 1:
		sisi = int(input("masukkan sisi : "))
		print(luas_persegi(sisi))
		
	elif pil == 2 :
			panjang = int(input("masukkan panjang : "))
			lebar = int(input("masukkan lebar : "))
			print(luas_persegi_panjang(panjang,lebar))
	elif pil == 3 :
	  	   alas = int(input("masukkan alas : "))
	  	   tinggi = int(input("masukkan tinggi : "))
	  	   print(luas_segitiga(alas,tinggi))
	  	   
	elif pil == 4 :
	     jari_jari = int(input("masukkan jari_jari : "))
	
	elif pil == 5 :
          alas = int(input("masukkan alas : ")) 
          tinggi = int(input("masukka tinggi : "))
          print(luas_jajar_genjang(alas,tinggi))
          
	elif pil == 6 :
	    sisi_sejajar_a = int(input("masukkan sisi_sejajar_a : "))
	    sisi_sejajar_b = int(input("masukkan sisi_sejajar_b : "))
	    tinggi = int(input("masukkan tinggi : "))
	    print(luas_trapesium(sisi_sejajar_a,sisi_sejajar_b,tinggi))
	    
	elif pil == 7 :
	   	diagonal1 = int(input("masukkan diagonal1 : "))
	   	diagonal2 = int(input("masukkan diagonal : "))
	   	print(luas_belah_ketupat(diagonal1,diagonal2))
	   	
	elif pil == 8 :
	   	diagonal1 = int(input("masukkan diagonla1 : "))
	   	diagonal2 = int(input("masukkan diagonal2 : "))
	   	print(luas_layang_layang(diagonal1,diagonal2))
	   	
	elif pil == 9 :
	   	jari_jari = int(input("masukkan jari_jari : "))
	   	sudut = int(input("masukkan sudut : "))
	   	print(luas_juring_lingkaran(jari_jari,sudut))
	   	
	elif pil == 10 :
	   	jari_jari = int(input("masukkan jari_jari : "))
	   	print(luas_setengah_lingkaran(jari_jari))
	   
	   
     
	else:
		break

	input()