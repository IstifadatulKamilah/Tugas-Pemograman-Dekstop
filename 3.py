tinggi=float(input("Masukkan tinggi anda :"))
berat=float(input("Masukkan berat badan anda :"))
bmi=round(berat/(tinggi*tinggi),2)
print("Index Massa Tubuh Anda adalah :",bmi)

if bmi <18.5:
    print ("Berat badan kurang")
elif bmi >=18.5 and bmi <=22.9:
    print ("Berat badan normal")
elif bmi >=23 and bmi <=29.9:
    print("Berat badan berlebih (cenderung obesitas)")
elif bmi >=30:
    print ("obesitas")
