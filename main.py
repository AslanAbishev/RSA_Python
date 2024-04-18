import random
import math

def generate_primes():
    primes = set()

    # Method to fill the primes set using Sieve of Eratosthenes
    sieve = [True] * 250
    sieve[0] = False
    sieve[1] = False
    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            sieve[j] = False

    # Filling the prime numbers
    for i in range(len(sieve)):
        if sieve[i]:
            primes.add(i)

    # Pick two distinct random primes p and q
    p = random.choice(list(primes))
    primes.remove(p)
    q = random.choice(list(primes))

    return p, q

def setkeys():
    global public_key, private_key, n, p, q
    p, q = generate_primes()

    n = p * q
    fi = (p - 1) * (q - 1)

    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1

    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = e

    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1

    private_key = d

def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = []
    for letter in message:
        encrypted_text.append(pow(ord(letter), e, n))
    return encrypted_text

def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = ''
    for num in encrypted_text:
        decrypted += chr(pow(num, d, n))
    return decrypted

if __name__ == '__main__':
    setkeys()

    # Take user input for the message
    message = input("Enter the message: ")

    # Encrypt the message
    encoded = encrypt(message)

    print("\nGenerated primes (p and q):", p, q)
    print("\nPublic key (e, n):", public_key, n)
    print("\nPrivate key (d, n):", private_key, n)
    print("\nOriginal message:")
    print(message)
    print("\nEncoded message (encrypted by public key):")
    print(' '.join(map(str, encoded)))

    # Decrypt the message
    decoded = decrypt(encoded)
    print("\nDecoded message (decrypted by private key):")
    print(decoded)
