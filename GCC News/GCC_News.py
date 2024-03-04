import hashlib
import base64
import json
import time
import random
import hashlib
from Crypto.Util.number import bytes_to_long, isPrime
import math

def hash_string_sha256(message):
    message_bytes = message.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message_bytes)
    hashed_message = sha256_hash.digest()
    return int.from_bytes(hashed_message, byteorder='big')

def generate_key(username):
    length = lambda x : len(bin(x)[2:])
    s = bytes_to_long(username.encode())
    random.seed(s)
    e = 0x1001
    phi = 0
    while math.gcd(phi,e) != 1:
        n = 1
        factors = []
        while length(n) < 2048:
            temp_n = random.getrandbits(48)
            if isPrime(temp_n):
                n *= temp_n
                factors.append(temp_n)
        phi = 1
        for f in factors:
            phi *= (f - 1)
    d = pow(e, -1, phi)
    return (n,e), (n,d)

def generate_signature(message, private_key):
    n, d = private_key
    hashed_message = hash_string_sha256(message)
    signature = pow(hashed_message, d, n)   
    return signature

users_f = {
    'GCC': ['securePassword', False]
}
users_t = {
    'GCC': ['securePassword', True]
}
public_key_users = {}
username = 'GCC'

message_f = base64.b64encode(str({username : [users_f[username][1]]}).encode()).decode()
message_t = base64.b64encode(str({username : [users_t[username][1]]}).encode()).decode()
pv_key, pub_key = generate_key(username)
signature_f = generate_signature(message_f, pv_key)
signature_t = generate_signature(message_t, pv_key)

def login(password, username, users, signature):
    if username not in users:
        return None
    if password != users[username][0]:
        return None
    public_key, private_key = generate_key(username)
    public_key_users[username] = public_key
    signature = generate_signature(str({username : [users[username][1]]}), private_key)
    return signature


original_link = "http://worker02.gcc-ctf.com:11848/news?token=51744648718937296723564044885354410460297897176849813617484933999885703039365028439574873901586445289713451647000581971518735294222874720912094608250768986430071020593519695387515700215772349288006024410793237270489508282953201500917969954701909229532673077829470878657476006964246930663163026092167288567340255639102679344949060371617131750343136916827751618936655514141602720018530512275633390524592348282051114466159239143158343517954832711356304526128710651675345182760411208270377401448992996886126386389582024321843490173500712374459871253473196361990599426660355938739876122350028414141158059833344764345566682&message=eydHQ0MnOiBbRmFsc2VdfQ%3D%3D"
new_link =      "http://worker02.gcc-ctf.com:11848/news?token=51744648718937296723564044885354410460297897176849813617484933999885703039365028439574873901586445289713451647000581971518735294222874720912094608250768986430071020593519695387515700215772349288006024410793237270489508282953201500917969954701909229532673077829470878657476006964246930663163026092167288567340255639102679344949060371617131750343136916827751618936655514141602720018530512275633390524592348282051114466159239143158343517954832711356304526128710651675345182760411208270377401448992996886126386389582024321843490173500712374459871253473196361990599426660355938739876122350028414141158059833344764345566682&message=eydHQ0MnOiBbRmFsc2VdfQ%3D%3D"
signature_t = login(users_t[username][0], username, users_t, signature_t)
signature_f = login(users_f[username][0], username, users_f, signature_f)

print(f"http://worker02.gcc-ctf.com:11848/news?token={signature_t}&message={message_t},\nIs it the same as the original link? {signature_t == original_link}")