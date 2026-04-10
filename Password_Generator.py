import string
import random

# random_parameters concatenates the strings constants that the for loops will use to generate the password.
generated_password = ""
random_parameters = string.ascii_letters + string.digits + string.punctuation 

#For loop that iterate 8 times using random strings and updates generated_password variable creating the password.
for i in range(10):
    generated_password = generated_password + random.choice(random_parameters)

print(generated_password)
