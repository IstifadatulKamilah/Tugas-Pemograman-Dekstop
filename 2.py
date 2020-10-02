def menu():
    print("------Menghitung Luas dan Keliling Segitiga------")
    print("1. Luas")
    print("2. Keliling")
    choose=int(input("Masukkan pilihan anda ="))
    if choose== 1:
        print(luas())
    elif choose== 2:
        print(keliling())
    else:
        print("yang anda masukkan tidak ada di pilihan")

def luas ():
    print ("---------------------")
    print ("~~~Menghitung Luas Segitiga~~~")
    a=int(input("Masukkann panjang alas ="))
    t=int(input("Masukkan tinggi segitiga ="))
    luas =(0.5*a*t)
    return luas

def keliling ():
    print("---------------------")
    print("~~~Menghitung Keliling Segitiga~~~")
    a=int(input("Masukkan sisi 1="))
    b=int(input("Masukkan sisi 2="))
    c=int(input("Masukkan sisi 3="))
    kel=(a+b+c)
    return kel
menu()
