import re
# import hashlib
# import bcrypt

def detectar_cifrado(password):
    if re.match(r'^[0-9a-f]{32}$', password):
        return "MD5 (Inseguro)"
    elif re.match(r'^[0-9a-f]{40}$', password):
        return "SHA-1 (Inseguro)"
    elif re.match(r'^[0-9a-f]{64}$', password):
        return "SHA-256"
    elif password.startswith('$2b$') or password.startswith('$2a$'):
        return "Bcrypt (Seguro)"
    elif password.startswith('$pbkdf2-sha256$'):
        return "PBKDF2 (Seguro)"
    else:
        return "Desconocido"