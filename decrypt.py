from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64


def decrypt(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        data = encrypted_file.read()

    salt = data[:16]
    encrypted_data = data[16:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(key))
    cipher = Cipher(algorithms.AES(key[:32]), modes.CFB8(salt), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    return decrypted_data


if __name__ == '__main__':
    print(decrypt("mydataaaa.txt.enc", b'my_secret_key'))
