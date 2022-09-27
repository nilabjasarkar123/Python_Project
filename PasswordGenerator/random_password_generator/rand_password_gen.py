import random
import secrets

from secrets import choice

upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['!', '@', '#', '$', '%', '&', '*']

passwordcreate = random.choice(upper_char) + random.choice(lower_char) + random.choice(num) + random.choice(special_char)

#print(passwordcreate)

pass_len = 10

passw = ''
for i in range(pass_len):
    passw += ''.join(secrets.choice(passwordcreate))
print(passw)
         
