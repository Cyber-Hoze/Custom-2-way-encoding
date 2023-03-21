import base64
import zlib
import os
from colorama import Fore, Style
os.system("cls")
def stage_1(message, secret_key):
    base_encoded_message = base64.b64encode(message.encode("utf-8")).decode("utf-8")
    encrypted_message = ""
    for i in range(len(base_encoded_message)):  
        key_char = secret_key[i % len(secret_key)]
        encrypted_char = chr((ord(base_encoded_message[i]) + ord(key_char)) % 256)
        encrypted_message += encrypted_char
    encrypted_message = base64.b64encode(encrypted_message.encode('utf-8')).decode('utf-8')
    return encrypted_message
def decode_stage_1(encrypted_message, decrypt_secret_key):
    encrypted_message = base64.b64decode(str(encrypted_message).encode('utf-8')).decode('utf-8')
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        key_char = decrypt_secret_key[i % len(decrypt_secret_key)]
        decrypted_char = chr((ord(encrypted_message[i]) - ord(key_char) + 256) % 256)
        decrypted_message += decrypted_char
    decoded_message = base64.b64decode(decrypted_message.encode("utf-8")).decode("utf-8")
    return decoded_message
def encode_message(key):
    return base64.b64encode(zlib.compress(base64.b64encode(str(key[::-1]).encode("utf-8")))).decode("utf-8")
def decode_message(encoded_message):
    return base64.b64decode(str(zlib.decompress(base64.b64decode(str(encoded_message).encode("utf-8"))).decode("utf-8"))).decode('utf-8')[::-1]
if __name__ == "__main__":
    print(Fore.WHITE + Style.BRIGHT)
    message = "139.162.199.106:41337"
    x = input(f"Use hardcoded message (\"{message}\")?  ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE})\n --->  ")
    if x in ["y", "Y"]:
        pass
    else:
        os.system("cls")
        message = input("Enter message: ")
    secret_key = "MBs0TjRwdc*G8mRph&YKL*5!^1l8urC5VkR^9QvX"
    f = encode_message(secret_key)
    ff = decode_message(f)
    e = stage_1(message, ff)
    ee = decode_stage_1(e, ff)
    print(f"{Style.BRIGHT}{Fore.GREEN}Encoded secret key: {Fore.CYAN}{ff}{Fore.GREEN}{Style.NORMAL}  ---->  {Fore.RED}{f}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Encoded Message: {Fore.CYAN}{ee}{Fore.GREEN}{Style.NORMAL}  ---->  {Fore.RED}{e}")