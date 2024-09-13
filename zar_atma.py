import random

while True:
    print("Zar atmak için a tuşuna basınız")
    atma = input()
    if atma == "a":
        zar = random.randint(1, 6)
        print("Çıkan sayı:", zar)
    else:
        print("İşlem geçersiz")    