dico = dict(zip(
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
    range(0, 26)
))


def generateKey(m, k):
    global key
    key = " "
    if len(m) == len(k):
        key = k

    while len(k) < len(m):
        j = k
        k = j + k
    if len(k) > len(m):
        S = list(k)
        i = len(m)
        del (S[i:])
        key = key + str(S)
    print(key)


def chiffrement(m, k):
    global cipher
    cipher = " "
    Listm = list()
    Listk = list()
    som = list()
    for i in m:
        for cle, val in dico.items():
            if i == cle:
                Listm.append(val)
    #    print(Listm)
    for i in k:
        for cle, val in dico.items():
            if i == cle:
                Listk.append(val)
    #    print(Listk)
    for i in range(len(m)):
        t = (Listm[i] + Listk[i]) % 26
        som.append(t)
    #    print(som)
    for i in som:
        for cle, val in dico.items():
            if i == val:
                cipher = cipher + cle
    print(cipher)


def dechiffrement(m, k):
    L = list()
    P = list()
    som = list()
    clear = " "
    for i in m:
        for cle, val in dico.items():
            if i == cle:
                L.append(val)
    #    print(L)
    for i in k:
        for cle, val in dico.items():
            if i == cle:
                P.append(val)
    #    print(P)
    for i in range(len(L)):
        s = (L[i] - P[i]) % 26
        if s < 0:
            s = s + 26
        som.append(s)
    #    print(som)
    for i in som:
        for cle, val in dico.items():
            if i == val:
                clear = clear + cle
    print(clear)


M = "chiffrementdevegenere"
key1 = "fpbm"
print(M)
generateKey(M, key1)
chiffrement(M, key)
dechiffrement(cipher, key)
