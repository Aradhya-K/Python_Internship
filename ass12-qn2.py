import random
import string

def random_alpha_char():
    return random.choice(string.ascii_letters)

def random_alpha_string(length=None):
    if length is None:
        length = random.randint(1, 100)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def random_fixed_length_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

print("Random alphabetical character:", random_alpha_char())
print("Random alphabetical string of arbitrary length:", random_alpha_string())
print("Random alphabetical string of length 10:", random_alpha_string(10))
print("Random alphabetical string of fixed length 5:", random_fixed_length_string(5))