dico = dict(zip(
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),
    range(0, 26)
))

def chiffrer(m, k):
    L = list()
    c = " "
    for i in m:
        for cle, val in dico.items():
            if i == cle:
                var = (val + k) % 26
                L.append(var)
    for i in L:
        for cle, val in dico.items():
            if i == val:
                c = c + cle
    print(c)
    return c

def dechiffrer(c, k):
    L = list()
    ch = " "
    for i in c:
        for cle, val in dico.items():
            if i == cle:
                var = (val - k) % 26
                if var < 0:
                    var = var + 26
                L.append(var)
    for i in L:
        for cle, val in dico.items():
            if i == val:
                ch = ch + cle
    print(ch)
    return ch


message = "cesar"
cipher = chiffrer(message, 3)
dechiffrer(cipher, 3)
