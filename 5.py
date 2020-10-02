username=("IstifadatulKamilah")
passwordku=("milamila01")
          

def masuk(user,password):
    if user != username and password != passwordku:
        stop = False
    else:
        stop = True
    return stop


a= 3
for i in range (0,a):
    userbaru = input("username = ")
    passwordbaru = input ("password = ")
    stop = (masuk(userbaru,passwordbaru))
    if stop == True :
        print ("Selamat Anda Berhasil Masuk")
        break
    else :
        print ("Username dan Password Anda Salah")
