import math,string
import EuclideanAlgorithm as ea

#SIMILAR EXAMPLE TO RSA ALGORITHM IMPLEMENTATION
#YOU CAN GENERATE YOUR KEYS USING GENERATING ALGORITHMS

public_a = 8
bob_r = 9
alice_r = 3
mod_n = 29

bob_K = int(math.pow(public_a,bob_r) % mod_n)
alice_K= int(math.pow(public_a,alice_r) % mod_n)

def encryptionStarts(makeCipher):
    print ("Bob : Hey Alice it is my number -->", bob_K)
    print ("Kaan: Hey Bob it is my number -->", alice_K)
    bob_K2 = int((math.pow(alice_K,bob_r) % mod_n))
    print ("Ssshh!!! It's Burak, my encryption key --> ", bob_K2)

    enc_plain_list = []
    for i in range (0,makeCipher.__len__(),1):
        encrypted_plaintext = int(((bob_K2)*(makeCipher[i])) % mod_n)
        enc_plain_list.append(encrypted_plaintext)
    return enc_plain_list

def decryptionStarts(decryptCipher):
    print ("Hey Alice, You can solve this encrypted text, right? --> ", decryptCipher , "\n-----------------")
    print ("Got it Bob!, I think I can!!")
    alice_K1 = int((math.pow(bob_K,alice_r) % mod_n))
    mod_inv = ea.Gcd(alice_K1,mod_n) #you can use your xgcd function
    dec_plain_list = []
    dec_plain = []
    for i in range (0,decryptCipher.__len__(),1):
        decrypted = int((mod_inv * decryptCipher[i]) % mod_n)
        dec_plain_list.append(decrypted)
        dec_plain.append(string.ascii_lowercase[dec_plain_list[i]-1])

    print ("I thought you mean that?,didn't you? --> ", dec_plain)

def main():
    plaintext = input("Enter plaintext: ")
    plaintext = plaintext.lower()
    output = []
    for character in plaintext:
        number = ord(character) - 96
        output.append(number)
    for_decrypt = encryptionStarts(output)
    decryptionStarts(for_decrypt)

main()
input("Press Enter to exit.")