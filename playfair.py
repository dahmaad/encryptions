import numpy as np


def matrix(Key):
    A = np.empty(25, dtype='str')
    A = A.reshape(5, 5)
    alphabets = "abcdefghijklmnopqrstuvxyz"
    k = Key + alphabets
    S = list()
    for i in k:
        if i not in S:
            S.append(i)
    for i in range(min(25, len(S))):
        A[i // 5][i % 5] = S[i]
    print(A)
    return A


def find_letter_position(Mx, letter):
    for row in range(5):
        for col in range(5):
            if Mx[row][col] == letter:
                return row, col


def chiffrement(M, Mx):
    global ciphertext
    ciphertext = ""
    for i in range(0, len(M) - 1, 2):
        letter1, letter2 = M[i], M[i + 1]
        row1, col1 = find_letter_position(Mx, letter1)
        row2, col2 = find_letter_position(Mx, letter2)
        if row1 == row2:
            if Mx[row1][col1 % 5] == Mx[row2][(col2 - 1) % 5]:
                ciphertext += Mx[row1][(col1 + 1) % 5] + Mx[row2][(col2 + 2) % 5]
            elif Mx[row1][col1 % 5] == Mx[row2][(col2 + 1) % 5]:
                ciphertext += Mx[row1][(col1 + 2) % 5] + Mx[row2][(col2 + 2) % 5]
            ciphertext += Mx[row1][(col1 + 1) % 5] + Mx[row2][(col2 + 1) % 5]
        elif col1 == col2:
            if Mx[row1 % 5][col1] == Mx[(row2 + 1) % 5][col2]:
                ciphertext += Mx[(row1 + 2) % 5][col1] + Mx[(row2 + 2) % 5][col2]
            elif Mx[row1 % 5][col1] == Mx[(row2 - 1) % 5][col2]:
                ciphertext += Mx[(row1 + 1) % 5][col1] + Mx[(row2 + 2) % 5][col2]
            ciphertext += Mx[(row1 + 1) % 5][col1] + Mx[(row2 + 1) % 5][col2]
        else:
            ciphertext += Mx[row1][col2] + Mx[row2][col1]
    print(ciphertext)
    return ciphertext


def dechiffrement(C, Mx):
    cleartext = ""
    for i in range(0, len(C) - 1, 2):
        letter1, letter2 = C[i], C[i + 1]
        row1, col1 = find_letter_position(Mx, letter1)
        row2, col2 = find_letter_position(Mx, letter2)
        if row1 == row2:
            if Mx[row1][col1 % 5] == Mx[row2][(col2 - 1) % 5]:
                cleartext += Mx[row1][(col1 - 1) % 5] + Mx[row2][(col2 - 2) % 5]
            elif Mx[row1][col1 % 5] == Mx[row2][(col2 + 1) % 5]:
                cleartext += Mx[row1][(col1 - 2) % 5] + Mx[row2][(col2 - 2) % 5]
            cleartext += Mx[row1][(col1 - 1) % 5] + Mx[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if Mx[row1 % 5][col1] == Mx[(row2 + 1) % 5][col2]:
                cleartext += Mx[(row1 - 2) % 5][col1] + Mx[(row2 - 2) % 5][col2]
            elif Mx[row1 % 5][col1] == Mx[(row2 - 1) % 5][col2]:
                cleartext += Mx[(row1 - 1) % 5][col1] + Mx[(row2 - 2) % 5][col2]
            cleartext += Mx[(row1 - 1) % 5][col1] + Mx[(row2 - 1) % 5][col2]
        else:
            cleartext += Mx[row1][col2] + Mx[row2][col1]
    print(cleartext)
    return cleartext

key = str(input("enter key : "))
M = str(input("enter message :"))
x = matrix(key)
if len(M) % 2 == 0:
    chiffrement(M, x)
    dechiffrement(ciphertext, x)
else:
    M += "x"
    chiffrement(M, x)
    dechiffrement(ciphertext, x)
