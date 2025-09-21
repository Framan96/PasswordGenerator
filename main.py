import hashlib
import re
import string

password_map = {}
def Strengthchecker(password):
    length = len(password)
    has_lower = bool(re.search(r'[a-z]',password))
    has_capital = bool(re.search(r'[A-Z]',password))
    has_digit = bool(re.search(r'[0-9]',password))
    has_special = bool(re.search(r'[!@#$%^&*()_]',password))
    score = has_capital+has_digit+has_lower+has_special
    if length>= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >=2:
        return "Medium"
    else:
        return "Weak"


def Generate_password(password:str,length:int=16):
    if password in password_map:
        return password_map[password]
    hash_bytes = hashlib.sha512(password.encode()).digest()
    charset = string.ascii_letters + string.digits + string.punctuation

    strong_pw = ''.join(charset[b%len(charset)] for b in hash_bytes)[:length]

    password_map[password] = strong_pw
    return strong_pw

def password_manager(password:str):
    strength = Strengthchecker(password)
    print(f"strength:{strength}")
    strong_pw = Generate_password(password)
    print(f"Generated Strong password: {strong_pw}")
    return strong_pw