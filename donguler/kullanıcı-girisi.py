print("""
*****************************
Kullanıcı Girişi Dongu ile
*****************************
""")

sys_username = "alp"
sys_pwd = "1234"
sys_giris_hakki = 3

while True:
    username = input("Userame:")
    pwd = input("Sifre:")

    if (username == sys_username and sys_pwd != pwd):
        print("Parola Hatalı")
        sys_giris_hakki -=1
    elif (username != sys_username and sys_pwd == pwd):
        print("Username Hatalı")
        sys_giris_hakki -=1
    elif (username != sys_username and sys_pwd != pwd):
        print("Username ve Şifre  Hatalı")
        sys_giris_hakki -=1
    else:
        print("Başarılı Giriş")
        break

    if(sys_giris_hakki == 0):
        print("Giriş Hakkınız Bitti")
        break