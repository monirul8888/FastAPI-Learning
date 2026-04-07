from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def hashPassword(password: str):
    return password_hash.hash(password)




