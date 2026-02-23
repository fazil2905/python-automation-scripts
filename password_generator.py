import random
import string

print("===PASSWORD GENERATOR===")

length = int(input("Enter the desired password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print(f"Generated password: {password}")
