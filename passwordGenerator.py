import random

# --- global variables ---
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

special = ['!', '@', '#', '$', '%', '&', '*', '-', '_', ',', '.']

numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

options = [upper, lower, special, numeric]

def check(password, type):
    for char in password:
        if char in type:
            return True
    return False

def password_generator():
    password = ""

    length = random.randrange(8,20)

    for i in range(length):
        char = random.choice(options)

        password = password + random.choice(char)

        if len(password) > length/2:
            if check(password, lower) == False:
                password = password + random.choice(lower)
            elif check(password, upper) == False:
                password = password + random.choice(upper)
            elif check(password, special) == False:
                password = password + random.choice(special)
            elif check(password, numeric) == False:
                password = password + random.choice(numeric)
    return password

print(password_generator())