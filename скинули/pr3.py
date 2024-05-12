# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x

# def module_inv(x, y):
#     gcd, a, b = extended_gcd(x, y)
#     if gcd != 1:
#         return None 
#     else:
#         return a % y

# x = 15
# y = 26
# mod_inv = module_inv(x, y)
# print(f"Значение {x} по модулю {y} равно {mod_inv}")
# from egcd import egcd
# print(egcd(15, 26))
# print('wellplayed'[::-1])
# from cryptography.fernet import Fernet
# fermat_key = Fernet.generate_key()
# print('fermat key = ', fermat_key.decode())
# from cryptography.fernet import Fernet
# encryption_key = Fernet.generate_key()
# with open('encrypt.key', 'wb') as key_file:
#     key_file.write(encryption_key)
# print('encryption_key = ', encryption_key)
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'azimzshot')
print(token)
d = f.decrypt(token)
print(d)