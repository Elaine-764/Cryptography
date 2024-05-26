from sympy import prime
import time

def collision_algorithm(E, pointP, pointQ, test_n):
    # Generate points for set A
    A = [i * pointP for i in range(1, test_n + 1)]
    
    # Generate points for set B
    B = [(pointQ + i * pointP) for i in range(1, test_n + 1)]
    
    # Choose random subsets from A and B
    
    # Calculate matching points
    for i in range(len(A) -1):
        for j in range(len(B) - 1):
            if A[i] == B[j]:
                if i > j: # because n_A = i - j must be a positive number
                    print(f"y = {i}, z = {j}")

# Define the elliptic curve parameters
p = prime(700)
E = EllipticCurve(GF(p), [2, 3])

# Define the base point P and the target point Q
pointP = E([256 , 5015 , 1])
pointQ = E([2211 , 3368 , 1])
test_n = 20000

# Run collision algorithm
start_time = time.time()
result = collision_algorithm(E, pointP, pointQ, test_n)
current_time = time.time()
duration = current_time - start_time
print(f"--- {duration} seconds ---")