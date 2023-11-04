import numpy as np
def generate_matrix(m):
    A = np.empty(36, dtype='str')
    A = A.reshape(6, 6)
    for i in range(min(36, len(m))):
        A[i // 6][i % 6] = m[i]
    return A

def chiffrement(Mx):
    global ciphertext
    ciphertext = ""
    for j in range(6):
        for i in range(6):
            ciphertext += Mx[i][j]
    print(ciphertext)
    return ciphertext


def dechiffrement(c):
    generate_matrix(c)
    chiffrement(generate_matrix(c))


M = str(input("enter 36 characters :"))
X = generate_matrix(M)
chiffrement(X)
dechiffrement(ciphertext)

