import hashlib
import sys
from encode import *
arg = sys.argv
def SuperHash(string):
    string = bytes(string, "utf-8")
    primo = hashlib.md5(string).hexdigest()
    secondo = hashlib.sha256(string=bytes(primo, 'utf-8')).hexdigest()
    terzo = hashlib.sha224(string=bytes(secondo, 'utf-8')).hexdigest()
    quarto = hashlib.sha512(string=bytes(terzo, 'utf-8')).hexdigest()
    quinto = hashlib.sha384(string=bytes(quarto, 'utf-8')).hexdigest()
    tot = encode(quinto,6)
    return tot
def SuperPasswordVerify(password,hash):
    if SuperHash(password) == hash:
        return True
    else:
        return False
try:
    if arg[1] == 'SuperHash':
        print(SuperHash(arg[2]))
    if arg[1] == 'SuperPasswordVerify':
        print(SuperPasswordVerify(arg[2],arg[3]))
except:
    pass
