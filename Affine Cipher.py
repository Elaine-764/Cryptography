from sympy import*

def get_input():
    i = input("Which program \n[e] encrypt \t [d] decrypt: \n")
    return i


def main():

    type = get_input()

    if type == "e":
        p = int(prime(100))
        print(f"p = {p}")
        k1 = int(input("k_1 = "))
        k2 = int(input("k_2 = "))

        m = input("Your message: ")
        ciphered = ""
        for letter in m:
            ciphered += str(ord(letter)-86)
        print(f"Encoded message: {ciphered}")
        ciphered = int(ciphered)

        c = (k1*ciphered + k2) % p
        print(f"Ciphertext: {c}")

    if type == "d":
        p = prime(100)
        c = int(input("Ciphertext: "))
        for i in range(1, p):
            for j in range(1, p):
                inverse = pow(i, -1, p)
                deciphered = ((c-j)*inverse) %p
                deciphered = str(deciphered)
                plaintext = ""
                for x in range(0, len(deciphered), 2):
                    a = int(deciphered[x:x+1])
                    plaintext += chr(a+86)

                print(f"k1 = {i} \tk2 = {j} \n Plaintext: {deciphered}, {plaintext} \n")

main()