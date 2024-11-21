# Generating the keypair and printing out the keys

# generating keys in the command line with:
# ssh-keygen -t rsa -f "$(pwd)/ceu_key" -N ''

from pathlib import Path
from Crypto.PublicKey import RSA

#define our key files
pr_key_file = "ceu_key"  #private key
pub_key_file = "ceu_key.pub"  #public key

#checking if the keys really exist
assert Path(pr_key_file).exists(), f"Private key file {pr_key_file} does not exist!"
assert Path(pub_key_file).exists(), f"Public key file {pub_key_file} does not exist!"

#loading the private key from the file
with open(pr_key_file, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())

#extracting the public key from the private key and printing it out to share
public_key = private_key.publickey()
print(f"Public key:\n{public_key.export_key().decode('utf-8')}")

print(f"Private key:\n{private_key.export_key().decode('utf-8')}")