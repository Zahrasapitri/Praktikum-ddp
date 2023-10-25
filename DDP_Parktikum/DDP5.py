valuekendaraan =["sepeda motor","motocross","250","biru","2"]
valuekendaraan.append("33.350.000")
valuekendaraan.append("kx250")
valuekendaraan.insert(2,"kawasaki")
print (valuekendaraan)

#menghitung luas bangun datar

menghitung= input("PILIH OPRASI:\n 1. Hitung Luas Persegi \n 2. Hitung Luas Lingkaran \n 3. Hitung Luas Segitiga \n Pilihan: ")
match menghitung:
   case "1":
        sisi= int (input("masukan nilai sisi: "))
        Luas= sisi*sisi
        print(Luas)
   case "2":
        jari_jari= int (input("masukan nilai jari-jari: "))
        Luas= 3.14*jari_jari
        print(Luas)
   case "3":
        alas= int (input("masukan nilai alas: "))
        tinggi= int (input("masukan nilai tinggi: "))
        Luas= 0.5*alas*tinggi
        print(Luas)
   case _:
        print("salah pilih")