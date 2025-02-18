"Main"
import string
from UC3MCare import VaccineManager


#GLOBAL VARIABLES
Letters = string.ascii_letters + string.punctuation + string.digits
Shift = 3


def Encode(word):
    "funcion codificar"
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (Letters.index(letter) + Shift) % len(Letters)
            encoded = encoded + Letters[x]
    return encoded

def Decode(word):
    "funcion descodificar"
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (Letters.index(letter) - Shift) % len(Letters)
            encoded = encoded + Letters[x]
    return encoded

def Main():
    "funcion principal"
    mng = VaccineManager()
    res = mng.READ_ACCESS_REQUIEST_FROM_JSON("test.json")
    strRes = res.__str__()
    print(strRes)
    EncodeRes = Encode(strRes)
    print("Encoded Res "+ EncodeRes)
    DecodeRes = Decode(EncodeRes)
    print("Decoded Res: " + DecodeRes)


if __name__ == "__main__":
    Main()
