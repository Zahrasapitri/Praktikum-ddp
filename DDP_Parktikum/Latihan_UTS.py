def hitung_biaya_perjalanan():
    harga = 0
    jarak_tempuh = 0

    print("Nama Kendaraan: ")
    nama_kendaraan = input()

    print("Jenis Bensin (Pertalite / Pertamax / Pertamax Turbo): ")
    jenis_bensin = input().lower()

    if jenis_bensin == "pertalite":
        harga = 10000
        jarak_tempuh = 12
    elif jenis_bensin == "pertamax":
        harga = 14000
        jarak_tempuh = 13
    elif jenis_bensin == "pertamax turbo":
        harga = 17000
        jarak_tempuh = 13.5
    else:
        print("Jenis bensin tidak valid.")
        return

    print("Kota Tujuan (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")
    kota_tujuan = input().lower()

    jarak_kota_tujuan = 0
    if kota_tujuan == "jakarta":
        jarak_kota_tujuan = 20
    elif kota_tujuan == "bekasi":
        jarak_kota_tujuan = 35.7
    elif kota_tujuan == "depok":
        jarak_kota_tujuan = 5
    elif kota_tujuan == "tangerang":
        jarak_kota_tujuan = 99
    elif kota_tujuan == "bogor":
        jarak_kota_tujuan = 120.6
    else:
        print("Kota tujuan tidak valid.")
        return

    pemakaian_bensin = (jarak_kota_tujuan / jarak_tempuh)
    total_harga = pemakaian_bensin * harga

    print("\nNama Kendaraan:", nama_kendaraan)
    print("Jenis Bensin:", jenis_bensin.capitalize())
    print("Kota Tujuan:", kota_tujuan.capitalize())
    print("Pemakaian bensin:", f"{pemakaian_bensin:.2f} liter")
    print("Total Harga dari bensin:", f"Rp {total_harga:.2f}")

hitung_biaya_perjalanan()

print()


def pesanan_restoran():
    print("Masukkan Nama Pembeli:")
    nama_pembeli = input()

    print("Masukkan No HP Pembeli:")
    no_hp_pembeli = input()

    print("Pesan Makanan atau Minuman? (makanan / minuman):")
    jenis_pesanan = input().lower()

    if jenis_pesanan == "makanan":
        print("Menu Makanan:")
        print("Nasi Goreng - Rp. 15.000")
        print("Mie Goreng - Rp. 12.000")
        print("Ayam Geprek - Rp. 18.000")
    elif jenis_pesanan == "minuman":
        print("Menu Minuman:")
        print("Aneka Jus - Rp. 15.000")
        print("Soft Drink - Rp. 10.000")
        print("Sweet Ice Tea - Rp. 5.000")
    else:
        print("Jenis pesanan tidak valid.")
        return

    pesanan = input("Masukkan pesanan: ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    harga = 0
    if pesanan.lower() == "nasi goreng":
        harga = 15000
    elif pesanan.lower() == "mie goreng":
        harga = 12000
    elif pesanan.lower() == "ayam geprek":
        harga = 18000
    elif pesanan.lower() == "aneka jus":
        harga = 15000
    elif pesanan.lower() == "soft drink":
        harga = 10000
    elif pesanan.lower() == "sweet ice tea":
        harga = 5000
    else:
        print("Pesanan tidak valid.")
        return

    total_harga = jumlah_pesanan * harga

    print("\nNama Pembeli:", nama_pembeli)
    print("No HP Pembeli:", no_hp_pembeli)
    print("Menu yang dipesan:", pesanan)
    print("Jumlah Pesanan:", jumlah_pesanan)
    print("Harga yang harus dibayarkan: Rp", total_harga)

pesanan_restoran()
print()

for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)




