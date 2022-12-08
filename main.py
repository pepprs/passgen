import string
import random

# Set of possible characters to use in the password
chars = string.ascii_letters + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*"

# Generate a random password
password = ''.join(random.choice(chars) for i in range(16))

# Print the password
print(password)
