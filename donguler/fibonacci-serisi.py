print("""
*****************************
Fibonacci Serisi Programı Hoş Geldiniz

Yeni bir sayıyı önceki iki sayının toplamı 

şeklince oluşturur

1,1,2,3,5,8,13,21,34

Çıkmak için 'q' basın

*****************************
""")

a = 1
b = 1

fibonacci = [a,b]

for i in range(10):

    a,b = b,a+b
    print("a: ",a,"b: ",b)
    fibonacci.append(b)

print(fibonacci)