import random
import string

def generate_password(length):
    characters= string.ascii_letters + string.digits+string.punctuation
    password = ''.join(random.choice(characters)for i
    in range (length))
    return password
    
    # main program
length = int (input("enter rhe length of the password:
     "))
     print ("your generated password is :" ,
            generate_password(length))
     