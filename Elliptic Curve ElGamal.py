from sympy import prime

def get_input():
    i = input("Which program \n[e] encrypt \t [d] decrypt: \n")
    return i


def encrypt():
    p = prime(700) #randomly chosen prime
    print(f"p = {p}")

    E=EllipticCurve(GF(p),[2,3])
    plot(E) 
    print(E) 
    print(f"E has {E.cardinality()} points")

    # Print all points on E
    for i in range(E.cardinality()-1): 
        print(E[i])

    m = "Badminton is a strange sport"
    m = m.replace(" ","").lower()
    ECmessage=[]

    # Converts alphabetical message to points on E
    for i in range(len(m)):
        letter = m[i]
        number = ord(letter)-96
        ECmessage.append(E[number])
    print(ECmessage)

    # Encryption
    P = E([256 , 5015 , 1])
    n_A = 10001
    Q_A = n_A*P
    print(f"Q_A = {Q_A}")

    k = 14750
    C = k*P
    D = []
    u = Q_A*k #intermediate step

    for i in range(len(ECmessage)):
        point = ECmessage[i]
        D.append(point+u)

    print(f"C = {C}")
    print(f"D = {D}")

def decrypt():
    p = prime(700)
    E = EllipticCurve(GF(p), [2, 3])
    n_A = 10001

    C = E.point([1191, 3243, 1])
    D = [(1469, 2861, 1), (5175, 603, 1), (3451, 3273, 1), (375, 268, 1), (3249, 1252, 1), 
        (5092, 1413, 1), (308, 2182, 1), (1484, 4431, 1), (5092, 1413, 1), (3249, 1252, 1), 
        (2813, 3764, 1), (5175, 603, 1), (2813, 3764, 1), (308, 2182, 1), (4763, 5013, 1), 
        (5175, 603, 1), (5092, 1413, 1), (1441, 30, 1), (4585, 1440, 1), (2813, 3764, 1), 
        (1849, 1461, 1), (1484, 4431, 1), (4763, 5013, 1), (308, 2182, 1)] #randomly generated message
    plaintext = ""

    for D_value in D:
        D_point = E.point(D_value)
        point = n_A * C
        point2 = -1 * point
        deciphered = D_point + point2
        for j in range(E.cardinality()):
            if E[j] == deciphered:
                letter = chr(j+96)
                plaintext += letter

    print(f"deciphered plaintext: {plaintext}")

def main():
    input = get_input()
    if input == "e":
        encrypt()
    if input == "d":
        decrypt()

main()