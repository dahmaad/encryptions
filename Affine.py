from sympy import mod_inverse

dico = dict(zip(
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
    range(0, 26)
))


def chiffrer(M, k1, k2):
    L = list()
    S = list()
    global SH
    SH = " "
    for i in M:
        for cle, val in dico.items():
            if i == cle:
                y = ((k1 * val) + k2) % 26
                S.append(y)
    for i in S:
        for cle, val in dico.items():
            if i == val:
                SH = SH + cle
    print(SH)
    return SH


def dechiffrer(SH, k1, k2):
    l = list()
    sh = " "
    for i in SH:
        for cle, val in dico.items():
            if i == cle:
                y = (mod_inverse(k1, 26) * (val - k2)) % 26
                if y < 0:
                    y = y + 26
                l.append(y)
    for i in l:
        for cle, val in dico.items():
            if i == val:
                sh = sh + cle
    print(sh)


p = 3
q = 4
C = "entrez le message à chiffrer"
chiffrer(C, p, q)
dechiffrer(SH, p, q)
