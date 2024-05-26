from sympy import*
from random import randint

def get_input():
    i = input("Which program \n[s] set up system \t [e] encrypt \t [d] decrypt: \n")
    return i

def set_up():
    i = int(input("__th prime: "))
    p = int(prime(i))
    print("p =", p)

    g = randint(1, p-1)
    a = randint(1, p-1)
    A = int(pow(g, a, p))
    print(f"Public keys: \np = {p} \tg = {g} \tA = {A}")
    print(f"Private keys: \na = {a} ")

def encrypt():
    # get public keys
    p = int(input("p = "))
    g = int(input("g = "))
    A = int(input("A = "))

    # Input plaintext message
    plaintext = input("Your message: ").replace(" ","")
    
    b = len(str(p))//2
    if b % 2 == 1:
        max = b
    else:
        max = b-1

    c = []
    d = []
    for i in range(0, len(str(plaintext)), max):
        m = ""
        part = plaintext[i:i+max]
        for letter in part:
            m += str(ord(letter)-86)
        m = int(m)

        # Encryption
        k = randint(1, p-1)
        c.append(pow(g, k, p))
        d.append(m*pow(A, k, p) % p)
    print(f"c = {c} \nd = {d}")

def decrypt():
    n = int(input("the number of c_values: "))
    c = []
    for i in range(n):
        c.append(input("c-value: "))

    d = []
    for i in range(n):
        d.append(input("d-value: "))

    a = int(input("a = "))
    p = int(input("p = "))

    x = ""
    for i in range(len(c)):
        c_value = int(c[i])
        d_value = int(d[i])
        e = pow(c_value**a, -1, p) % p
        y = (e*d_value) % p
        x += str(y)

    # convert plaintext in algebraic cipher to English
    deciphered = ""
    for i in range(int(len(x)/2)):
        z = ""
        z += x[2*i]+x[2*i+1]
        z = int(z)
        deciphered += str(chr(z+86))

    print(f"Deciphered plaintext: {deciphered} \n")

def main():
    input = get_input()
    if input == "s":
        set_up()
    if input == "e":
        encrypt()
    if input == "d":
        decrypt()

main()