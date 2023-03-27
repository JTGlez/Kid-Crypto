# Algoritmo Kid Krypto.
import fileinput as fp

def setup(a, b, A, B):
    m = (a * b) - 1
    e = (A * m) + a
    d = (B * m) + b
    n = ((e * d)-1)//m
    return n, e, d

def encrypt(plaintext, public_key):
    n, e = public_key
    xe = plaintext * e
    y = xe % n
    return y

def decrypt(ciphertext, private_key, public_key):
    n, e = public_key
    d = private_key
    yd = ciphertext * d
    x = yd % n
    return x

#Recuperando las entradas en una lista.
inputs = []

for entrada in fp.input():
    inputs.append(entrada.strip())

mode = inputs[0]
a = inputs[1]
b = inputs[2]
aM = inputs[3]
bM = inputs[4]
plaintext = inputs[5]

n, e, d = setup(a, b, aM, bM)
public_key = (n, e)
private_key = d


if (mode == 'E'):
    ciphertext = encrypt(plaintext, public_key)
    print(ciphertext)
else:
    decrypted_plaintext = decrypt(plaintext, private_key, public_key)
    print(decrypted_plaintext)
