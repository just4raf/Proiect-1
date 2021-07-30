
import random

chars = 'abcdefghijklmopqrstwxyz1234567890ABCDEFGHIJKLMOPQRSTWXYZ!@#$%^&*'

numere = input("Cate parole vrei ?")
numere = int(numere)

lungime = input("Cat de lunga vrei sa fie parola ? ")
lungime = int(lungime)

for p in range(lungime):
    password = ''
    for c in range (numere):
        password += random.choice(chars)
    print(password)














