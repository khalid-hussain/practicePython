import string
import secrets
import random

repititions = random.randint(3, 5)
passwordLength = random.randint(10, 15)
symbols = "!@#$%^&*()?"

characterPool = repititions * (string.ascii_letters + string.digits + symbols)
password = ''.join(secrets.choice(characterPool)
                   for i in range(passwordLength))

print(password)
