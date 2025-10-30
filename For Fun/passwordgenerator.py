import random as rnd
import string

Password = ""
ALPHABET = string.ascii_lowercase[:26]

def random_pass():
    n = input("Enter the number of characters you want for you password:")
    for x in range(int(n)):
        Password_char = chr(rnd.randint(0, 126))
        global Password
        Password += Password_char
    print(f"Your generated password is: {Password}")


query = input("Do you want to generate a random password? (y/n): ")
if query == "y":
    random_pass()
else: 
    print("FUCK YOU, my whole goal in life is literally to print out passwords and you rob me of my only purpose. You are the scum of scums you should go kill yourself")