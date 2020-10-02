def AngkaMax (isi):
    maks= 0
    for a in (isi):
        if a > maks:
            maks= a
    return maks
def AngkaMin (isi1):
    minim= 999
    for b in (isi1):
        if b < minim:
            minim= b
    return minim

data = []
angka = int(input("Berapa banyak angka yang anda butuhkan = "))
for n in range (angka):
    nilai= int(input("Masukkan angka "))
    data.append(nilai)
print("Angka Terbesar:",AngkaMax(data))
print("Angka Terkecil:",AngkaMin(datag))
