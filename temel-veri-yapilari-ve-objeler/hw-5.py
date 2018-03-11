"""
Kullanıcıdan iki tane sayı isteyin ve
bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = int(input("Sayı 1: "))
b = int(input("Sayı 2: "))

print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))