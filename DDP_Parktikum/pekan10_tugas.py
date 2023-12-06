def lulus_saja(data): 
    lulus = []
    for siswa in data:
        if siswa["nilai"] > 65:
            lulus.append(siswa["nama"])
    return lulus

hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

lulus = lulus_saja(hasil_akhir)
print(lulus)
print()


def balikan(buah):
    balikan = []
    for i in range(len(buah) -1, -1, -1):
        balikan.append(buah[i])
    return balikan


buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
balikan = balikan(buah)
print(balikan)
print()


def duplikasi(buah2an):
    duplikasi_buah2an = []
    for buah in buah2an:
        duplikasi_buah2an.append(buah)
        duplikasi_buah2an.append(buah)
    return duplikasi_buah2an

buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
duplikasi_buah2an = duplikasi(buah2an)
print(duplikasi_buah2an)
print()


def hanya_konsonan(string):
    konsonan = set("bcdfghjklmnpqrstvwxyz")
    hasil = ""
    for karakter in string:
        if karakter in konsonan:
            hasil += karakter
    return hasil

print(hanya_konsonan("nurul fikri"))