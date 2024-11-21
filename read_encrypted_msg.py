from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#define our key files
pr_key_file = "ceu_key"  #private key
pub_key_file = "ceu_key.pub"  #public key

#checking if the keys really exist
assert Path(pr_key_file).exists(), f"Private key file {pr_key_file} does not exist!"
assert Path(pub_key_file).exists(), f"Public key file {pub_key_file} does not exist!"

#loading the private key from the file
with open(pr_key_file, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())

# Decrypting the received message using the private key.

#opening the encrypted message I have received
with open('encrypted_message.bin', "rb") as f:
    rec_encrypted_msg = f.read()

#create a cipher object using the private key for decryption
private_key_cipher = PKCS1_OAEP.new(private_key)

#decrypt the message using the private key and print out the result
decrypted_message = private_key_cipher.decrypt(rec_encrypted_msg)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")

#write the decrypted message into a simple txt file
with open('decrypted_message.txt', "w", encoding = 'utf8') as f:
    f.write(decrypted_message.decode('utf-8'))