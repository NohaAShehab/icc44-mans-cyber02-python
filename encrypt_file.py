from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64

def encrypt_file(file_path, key):

    # 1- read file
    try:
        with open(file_path, 'rb') as fileobject:
            data = fileobject.read()
            print(data)
    except Exception as e:
        return False
    else:
        # return fileobject
        salt = os.urandom(16)
    # 2- encrypt file ?
        """ prepare encryption object """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,  # Set key length to 32 bytes (256 bits)
            backend=default_backend()
        )
        print(kdf)
        # generate key :: key binary
        key = base64.urlsafe_b64encode(kdf.derive(key))
        # generate cipher object

        cipher = Cipher(algorithms.AES(key[:32]), modes.CFB8(salt),
                        backend=default_backend())  # Adjust key size to 32 bytes
        # encrupt the file
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        print(encrypted_data)

        with open(file_path + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(salt + encrypted_data)

if __name__ == "__main__":
    encryption_key = b'my_secret_key'
    res= encrypt_file("mydataaaa.txt", encryption_key)
    print(res)