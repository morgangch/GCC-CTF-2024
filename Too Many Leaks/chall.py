#!/usr/bin/env python3

import binascii
from Crypto.Util.number import getStrongPrime
import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_flag(secret_key):
    sha1 = hashlib.sha1()
    sha1.update(str(secret_key).encode('ascii'))
    key = sha1.digest()[:16]
    iv = os.urandom(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(flag,16))
    print("{ ciphertext : " + ciphertext.hex() + ", iv : " + iv.hex() + "}")
    return ciphertext, iv
# Generate parameters

p = getStrongPrime(512)
print(f"{p=}")
g = 2

# Alice calculates the public key A
a = getStrongPrime(512)
A = pow(g,a,p)
print(f"{A=}")

# Bob calculates the public key B
b = getStrongPrime(512)
B = pow(g,b,p)
print(f"{B=}")

# Calculate the secret key
s = pow(B,a,p)

# What ?!
mask = ((1 << 256) - 1 << 256) + (1 << 255)
r1 = s & mask
print(f"{r1=}")

# Charlie arrives and sync with Alice and Bob
c = getStrongPrime(512)
print(f"{c=}")
AC = pow(g,a+c,p)
s2 = pow(AC,b,p)
print(f"{AC=}")
r2 = s2 & mask
print(f"{r2=}")

ciphertext = b'\x89\xc3r!\x0b\xe2\xa7\xb3\x136b\x06\xf7Bo\x94\x11W\x00\x94\x93\xd0\x0f\xcb\x18\xb4g%\x019A;n\xa1\xad\xa60.\x19\x16\xb6\xc0*o\x93_N\xd4'
iv = b'\xc7\xd1\x92\xfbr\xb5)\xac\xf7\xb5}H\x8c\x18$f'

def decrypt_flag(ciphertext, iv, secret_key):
    print(f"{ciphertext=}, {iv=}, {secret_key=}")
    sha1 = hashlib.sha1()
    sha1.update(str(secret_key).encode('ascii'))
    key = sha1.digest()[:16]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext)

    return decrypted_message

# Pad the ciphertext before decryption

decrypted_message = decrypt_flag(ciphertext, iv, s)
hex_representation = ' '.join(format(byte, '02x') for byte in decrypted_message)
print(f"{decrypted_message=}")