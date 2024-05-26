from sympy import*

def get_input():
    i = input("Which program \n[e] encrypt \t [d] decrypt: \n")
    return i


def main():

    type = get_input()

    if type == "e":
        m = input("Your message: ").replace(" ", "")
        s = int(input("Shift by: ")) 
        s = s % 26
        ciphered = ""
        for letter in m:
            if 97 <= ord(letter) <= (122-s):
                ciphered += chr(ord(letter)+s)
            if 122-s <= ord(letter) <= 122:
                ciphered += chr(ord(letter) - (-s%26))

        print(f"Ciphertext: {ciphered}")

    if type == "d":
        x = input("Ciphertext: ")
        x = x.lower()
        z = ""
        for letter in x:
            if 97 <= ord(letter) <= 122:
                z += letter

        for s in range (1,26):
            y = ""
            for letter in z:
                if letter == " ":
                    y += letter
                if 97+s <= ord(letter) <= 122:
                    y += chr(ord(letter)-s)
                if 97 <= ord(letter) < 97+s:
                    y = y + chr((122-96) + (ord(letter)-s))
            print (f"s = {s} \nPlaintext: {y}")

main()