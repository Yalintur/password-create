import random 
sifrem  = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("Kaç haneli bir sifre istiyorsun?"))
for i in range(x):
    parola = ""
    for i in range(x):
        parola += random.choice(sifrem)

print(parola)
