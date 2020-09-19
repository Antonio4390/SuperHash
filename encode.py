def encode(Str,key):
    ris = ""
    for d in Str:
        ris+=chr(ord(d)+key)
    return ris
def decode(Str,key):
    ris = ""
    for d in Str:
        ris+=chr(ord(d)-key)
    return ris
