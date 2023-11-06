import numpy as np
dico = dict(zip(
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
    range(0, 26)
))
def generate_matrix(m, k):
    while len(m) % len(k) != 0:
        m += " "
    global col, lig
    col = len(k)
    lig = len(m) // len(k)
    A = np.empty((lig, col), dtype='str')
    ligg, coll = 0, 0
    for i in m:
        A[ligg][coll] = i
        coll += 1
        if coll >= col:
            ligg += 1
            coll = 0
        if ligg == lig:
            break
    return A
def position(k, letter):
    for i in range(len(k)):
        if k[i] == letter:
            return i
def chiffrement(A, k):
    ch = ""
    for cle, val in dico.items():
        for i in range(len(k)):
            if k[i] == cle:
                for j in range(lig):
                    ch += A[j][position(k, k[i])]
    print(ch)
    return ch
def dechiffrement(A, c, k):
    sh = ""
    col = len(k)
    lig = len(c) // len(k)
    B = A
    z = 0
    for cle, val in dico.items():
        for i in k:
            if i == cle:
                for j in range(lig):
                    B[j][position(k, i)] = c[z]
                    z += 1
    for i in range(lig):
        for j in range(col):
            sh += B[i][j]
    print(sh)


# ce programme fonctionne seulement si la clè ne contient pas des lettres identiques comme "delivrance"
M = str(input("donner le message :"))
key = str(input("donner la cle :"))
mx = generate_matrix(M, key)
cipher = chiffrement(mx, key)
dechiffrement(mx, cipher, key)