import math
def generate_keys():
    # privately choose two primes
    p1 = 11
    p2 = 13

    # n is the modulus
    n = p1 * p2
    # phi totient function of a number such as x pow phi(n) mod n is 1
    phi = (p1 - 1) * (p2 - 1)

    # pick e such that e and phi are coprime
    # make sense because we want e*d -k*phi to equal to one, that's the one that gives us the original message
    e = 127

    # m pow e * d = m pow k * phi + 1 mod n
    # need to calculate d in order to be able to decrypt
    # d = (k * phi + 1) / e

    # d and k can be found from e * d - k * phi = 1
    # Bézouts coeficients for e and phi are d and k
    # why we can pass phi instead of the minus phi...lets say the minus will be in the k
    d, k = ext_euclidian_alg(e, phi)
    # we don't even care for the found k

    while d < 0:
        # private key d can be negative, so to make it we can just add phi
        # we can do that because e*d ≡1 mod phi...
        # and e*d ≡1 is what we want...we want such e and d that when you multiply them and mod phi it will be a one,
        # the one that means m to the power of one, the original message
        # so if we rotate more by phi it is still congruent as it just makes a full circle
        d += phi

    return (d, n), (e, n)



def ext_euclidian_alg(x, y):
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    old_r, r = x, y
    old_s, s = 1, 0
    old_t, t = 0, 1

    while True:
        if r == 0:
            break
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    print(f'Bézouts coefficients: {old_s} {old_t}')
    print(f'GCD: {old_r}')
    return old_s, old_t


def decrypt(key, text):
    message = []
    for letter in text:
        char = ord(letter)
        decrypted_char = chr(int(pow(char, key[0], key[1])))
        message.append(decrypted_char)
    return "".join(message)

def encrypt(key, text):
    encrypted_message = []
    for letter in text:
        char = ord(letter)
        encrypted_char = chr(int(pow(char, key[0], key[1])))
        encrypted_message.append(encrypted_char)
    return "".join(encrypted_message)

private_key, public_key = generate_keys()

message = 'Hello'
print(f"Message: {message}")

encrypted = encrypt(public_key, message)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(private_key, encrypted)
print(f"Decrypted: {decrypted}")
