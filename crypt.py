# import bcrypt

# password="anass123"
# hashed = bcrypt.hashpw(password.encode("utf-16"), bcrypt.gensalt())

# print(hashed)

from hashlib import pbkdf2_hmac

salt = b"mon_slat"
stored_hash = b"votre_hachage_pbkdf2"
iterations = 200000




password="anass123"
hashed = pbkdf2_hmac('sha256', password.encode("utf-16"), salt, iterations)

print(hashed)