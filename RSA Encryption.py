from sympy import*

def get_input():
    i = input("Which program \n[s] set up system \t [e] encrypt \t [d] decrypt: \n")
    return i

def set_up():
    
    i = int(input("p: __th prime: "))
    p = prime(i)
    j = int(input("q: __th prime: "))
    q = prime(j)
    N = q * p
    M = (q-1)*(p-1)

    # pick value of e
    for k in range(-5, 6):
        print(f"{k}*M: {factorint(k*M+1)}")
    e = int(input("e = "))

    print(f"Public keys: \tN = {N} \t e = {e}")
    print(f"Private keys: \tp = {p} \t q = {q} \t M = {M}")

def encrypt():

    # input system
    N = int(input("N = "))
    e = int(input ("e = "))
    if len(str(N)) % 2 == 0:
        max = len(str(N))/2 - 1
    if len(str(N)) % 2 == 1:
        max = len(str(N))//2
    max = int(max)

    message = input("Your message: ").lower().replace(" ","")

    # turn message to algebraic cipher
    ciphertext = []
    for i in range(0, len(message), max):
        part = message[i:i+max]
        algebraic = ""
        for letter in part:
            algebraic += str(ord(letter)-86)
        algebraic = int(algebraic)
        print(algebraic)
        
        cipher = pow(algebraic, e, N)
        ciphertext.append(cipher)
    
    print(f"Ciphertext: {ciphertext}")

def decrypt():
    N = 1190951292451
    M = 1190946600000
    e = 497753 
    #N = int(input("N = "))
    #M = int(input("M = "))
    #e = int(input ("e = "))

    # compute the inverse of e
    d = pow(e, -1, M)

    # get ciphertext
    #n = int(input("How many ciphertexts: "))
    #ciphertext = []
    #for i in range(n):
        #ciphertext.append(int((input("cipher: "))))
    ciphertext = [206077946527, 687481810416, 162690461155]

    plaintext = ""
    for i in range(len(ciphertext)):
        cipher = int(ciphertext[i])
        algebraic = pow(cipher, d, N)
        algebraic = str(algebraic)
        print(algebraic)

        for j in range(0, len(algebraic), 2):
            part = ""
            part += algebraic[j:j+2]
            print(part)
            part = int(part)
            plaintext += chr(part+86)
    print(f"Plaintext: {plaintext}")

def main():
    type = get_input()
    
    if type == "s":
        set_up()
    if type == "e":
        encrypt()
    if type == "d":
        decrypt()

main()
