print("""
*****************************
Kullanıcı Girişi
*****************************
""")

sys_username = "alp"
sys_pwd = "1234"

username = input("Userame:")
pwd = input("Sifre:")

if(username == sys_username and sys_pwd != pwd):
    print("Parola Hatalı")
elif(username != sys_username and sys_pwd == pwd):
    print("Username Hatalı")
elif (username != sys_username and sys_pwd != pwd):
    print("Username ve Şifre  Hatalı")
else:
    print("Başarılı Giriş")